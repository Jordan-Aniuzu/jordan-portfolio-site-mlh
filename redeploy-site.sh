#!/bin/bash
set -e

PROJECT_DIR="$HOME/mlh-fellowship-portfolio-site"
VENV_DIR="venv"
TMUX_SESSION="flask-server"

tmux kill-server 2>/dev/null || true

cd "$PROJECT_DIR"

git fetch && git reset origin/main --hard

source "$VENV_DIR/bin/activate"
pip install -r requirements.txt
deactivate

tmux new-session -d -s "$TMUX_SESSION" \
  "cd $PROJECT_DIR && source $VENV_DIR/bin/activate && flask run --host=0.0.0.0"

echo "Redeploy complete. Flask server running in tmux session '$TMUX_SESSION'."
