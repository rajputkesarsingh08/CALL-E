#!/bin/bash

echo "=========================================="
echo "       CampusConnect AI Backend"
echo "=========================================="

echo ""

cd "$(dirname "$0")/backend" || exit 1

if [ ! -d ".venv" ]; then
    echo "Virtual environment not found."
    echo "Creating virtual environment..."

    python3 -m venv .venv
fi

echo ""
echo "Activating virtual environment..."

source .venv/bin/activate

echo ""
echo "Installing dependencies..."

pip install -r requirements.txt

echo ""
echo "Starting FastAPI backend..."
echo ""
echo "Backend:"
echo "http://localhost:8000"
echo ""
echo "Health:"
echo "http://localhost:8000/api/health"
echo ""

uvicorn app.main:app --reload --port 8000
