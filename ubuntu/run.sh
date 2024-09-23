#!/bin/bash
echo "Update bot.. "
git stash
git pull
git stash pop

echo "Finish update"

echo "Starting bot.."
python3 main.py
