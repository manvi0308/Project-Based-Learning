#!/bin/bash

cat soccer_scores.csv | cut -d "," -f 2 | tail -n +2 | sort | uniq -c
