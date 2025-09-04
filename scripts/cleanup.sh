#!/bin/bash
echo "🧹 Cleaning up..."
rm -f .env
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete
