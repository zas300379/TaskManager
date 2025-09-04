#!/bin/bash
echo "🚀 Starting Docker..."
cp .env.docker .env
docker-compose up -d --build
echo "✅ Done! App: http://localhost:8000"
