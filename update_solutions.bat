@echo off
python process_submissions.py
git add .
git commit -m "Added solutions"
rem git push