#!/bin/bash

URL="http://localhost:5000/api/timeline_post"

RANDOM_ID=$RANDOM
NAME="TestName_$RANDOM_ID"
EMAIL="Test_$RANDOM_ID@gmail.com"
CONTENT="This is test $RANDOM_ID"

echo "Testing"
curl $URL

RESPONSE=$(curl --request POST $URL -d "name=$NAME&email=$EMAIL&content=$CONTENT")
POST_ID=$(echo "$RESPONSE" | grep -o '"id":[0-9]*' | grep -o '[0-9]*')

curl $URL | grep -q "$CONTENT" && echo "Found!" || echo "Not found!"

curl --request DELETE "$URL/$POST_ID"

curl $URL
