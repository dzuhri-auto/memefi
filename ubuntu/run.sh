#!/bin/bash
echo "Update bot.. "
git stash
git pull
git stash pop

echo "Finish update"
echo ""
echo "Starting bot, please wait.."
python3 main.py
