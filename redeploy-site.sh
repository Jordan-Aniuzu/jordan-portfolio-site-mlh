#!/bin/bash

cd
cd mlh-fellowship-portfolio-site/

git fetch && git reset origin/main --hard

source venv/bin/activate
pip install -r requirements.txt

sudo systemctl restart myportfolio
