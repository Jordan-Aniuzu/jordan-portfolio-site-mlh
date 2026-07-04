#!/bin/bash
# NOTES FOR DOCUMENTAITON: redeploy-site.sh
# Redeploys the Flask site with the latest changes from GitHub's main branch.
#
# Usage: ~/redeploy-site.sh

set -e

PROJECT_DIR="$HOME/mlh-fellowship-portfolio-site"
VENV_DIR="venv"
TMUX_SESSION="flask-server"

# P1. Kill all existing tmux sessions (so any old Flask server is stopped)
tmux kill-server 2>/dev/null || true

# P2. cd into the project folder
cd "$PROJECT_DIR"

# 3. Pull latest changes from GitHub main branch
git fetch && git reset origin/main --hard

# P4. Enter the venv and install/update python dependencies
source "$VENV_DIR/bin/activate"
pip install -r requirements.txt
deactivate

#P5. Start a new detached tmux session that cds into the project dir,
#    activates the venv, and starts the Flask server
tmux new-session -d -s "$TMUX_SESSION" \
  "cd $PROJECT_DIR && source $VENV_DIR/bin/activate && flask run --host=0.0.0.0"

echo "Redeploy complete. Flask server running in tmux session '$TMUX_SESSION'."
