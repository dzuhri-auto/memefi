@echo off
echo Update bot..

git stash
git pull
git stash pop

echo Done update bot..
echo Starting bot, please wait..

python3 main.py
pause
