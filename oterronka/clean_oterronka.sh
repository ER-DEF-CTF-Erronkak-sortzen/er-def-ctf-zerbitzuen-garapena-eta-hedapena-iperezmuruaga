#!/usr/bin/env bash

docker stop oterronka_OpenPLCRuntime_1 
#docker stop pasapasa_web_1
docker rm oterronka_OpenPLCRuntime_1 
#docker rm pasapasa_web_1
docker stop oterronka_OpenPLCWebBrowser_1 
#docker stop pasapasa_web_1
docker rm oterronka_OpenPLCWebBrowser_1 
#docker rm pasapasa_web_1
docker stop oterronka_PLCBezeroa_1 
#docker stop pasapasa_web_1
docker rm oterronka_PLCBezeroa_1 
#docker rm pasapasa_web_1
docker stop oterronka_web_1 
docker rm oterronka_web_1
