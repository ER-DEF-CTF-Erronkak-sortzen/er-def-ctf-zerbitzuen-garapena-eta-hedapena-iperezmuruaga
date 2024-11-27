#!/usr/bin/env bash

docker-compose -f "$SERVICES_PATH/openot/docker-compose.yml" up -d --build