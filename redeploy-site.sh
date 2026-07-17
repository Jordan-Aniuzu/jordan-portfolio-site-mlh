#!/bin/bash
set -e

PROJECT_DIR="$HOME/mlh-fellowship-portfolio-site"
VENV_DIR="venv"

cd "$PROJECT_DIR"

git fetch && git reset origin/main --hard

source "$VENV_DIR/bin/activate"

pip install -r requirements.txt

deactivate

sudo systemctl restart myportfolio

echo "Redeploy complete. myportfolio service restarted."
