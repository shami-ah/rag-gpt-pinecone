@echo off
echo Starting your AI App...
docker-compose up --build
start http://localhost:8501