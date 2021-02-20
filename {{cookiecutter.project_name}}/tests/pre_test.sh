#!/bin/bash
set -eu

compose_namespace="{{cookiecutter.project_name | lower}}tests"

# Remove services from previous tests
(
cd ../docker || exit 127
docker-compose -p "$compose_namespace" \
  down --volumes
)

# Start all services required for testing
(
cd ../docker || exit 127
docker-compose -p "$compose_namespace" \
  -f docker-compose.yml \
  -f docker-compose.test.yml \
  up --build --detach
)

# Give the systems time to start up
sleep 5
