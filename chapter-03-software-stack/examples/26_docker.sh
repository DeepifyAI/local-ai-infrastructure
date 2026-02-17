#!/bin/bash
docker compose up -d

# Check status
docker compose ps

# View logs
docker compose logs -f ollama

# Stop everything
docker compose down
