#!/bin/bash


URL="http://localhost:5001/api/timeline_post"

NAME="Jordan Test"
EMAIL="jordan@test.com"
CONTENT="Automated curl test post"

echo "Creating timeline post..."

curl -X POST $URL \
-d "name=$NAME" \
-d "email=$EMAIL" \
-d "content=$CONTENT"

echo ""

echo "Checking timeline posts..."

curl $URL
