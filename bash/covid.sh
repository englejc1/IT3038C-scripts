#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
HOSPITAL=$(echo $DATA | jq '.[0].hospitalizedCurrently')
DEATH=$(echo $DATA | jq '.[0].death')
UPDATED=$(echo $DATA | jq '.[0].lastModified')

echo "On $TODAY, there were $POSITIVE positive COVID cases, with $HOSPITAL people being hospitalized, and $DEATH deaths. This data was last updated on $UPDATED."
