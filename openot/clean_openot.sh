#!/usr/bin/env bash

docker stop openot_hackedweb_1
docker stop openot_openplc_1 
docker rm openot_hackedweb_1
docker rm openot_openplc_1 
docker image rm openot_openplc
docker image rm openot_hackedweb
