#!/bin/bash
echo "🧪 Running tests..."
docker-compose exec app gauge run tests/specs/
