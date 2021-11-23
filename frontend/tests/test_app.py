from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Tasks

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app


    def setUp(self):
        db.create_all()
        db.session.add(Tasks(desc="Run unit tests"))
        db.session.commit

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase): # Testing successful route response
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_create_get(self):
        response = self.client.get(url_for('create_task'))
        self.assertEqual(response.status_code, 200)

    def test_read_get(self):
        response = self.client.get(url_for('read_task'))
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for('update_task', id=1))
        self.assertEqual(response.status_code, 200)

class TestRead(TestBase):

    def test_read_home_tasks(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b"Run unit tests", response.data) # In is there
    
    def test_read_tasks_dict(self):
        response = self.client.get(url_for('read_task'))
        self.assertIn(b"Run unit tests", response.data)
    
class TestCreate(TestBase):
    def test_create_task(self):
        response = self.client.post(
            url_for('create_task'),
            data={"desc": "Testing create task"},
            follow_redirects=True
            )
        self.assertIn(b"Testing create task", response.data)
        test_create = Tasks.query.filter_by(desc="Testing create task").first()
        self.assertEqual(test_create.desc, "Testing create task")

class TestUpdate(TestBase):
    def test_update_task(self):
        response = self.client.post(
            url_for('update_task', id=1),
            data={"desc": "Testing update task"},
            follow_redirects=True
            )
        self.assertIn(b"Testing update task", response.data)

class TestDelete(TestBase):
    def test_delete_task(self):
        response = self.client.get(
            url_for("delete", id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"Run unit tests", response.data) # NotIn meaning deleted

class TestComp(TestBase):
    def test_comp_task(self):
        response = self.client.get(
            url_for("status", id=1),
            follow_redirects=True
        )
        self.assertEqual(Tasks.query.get(1).comp, True)

class TestIncomp(TestBase):
    def test_Incomp_task(self):
        response = self.client.get(
            url_for("status_incomp", id=1),
            follow_redirects=True
        )
        self.assertEqual(Tasks.query.get(1).comp, False)
