#!/bin/bash

echo "Deploy Stage"

ssh jenkins@dev-jenkins docker stack deploy --compose-file docker-compose.yaml todo-list