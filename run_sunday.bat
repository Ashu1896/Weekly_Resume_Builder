@echo off
cd /d "d:\Resume_Builder"
echo ==========================================
echo Starting Sunday Resume Automation Trigger
echo Current Time: %date% %time%
echo ==========================================
python run_weekly.py >> sunday_run.log 2>&1
echo Run completed. Check sunday_run.log for details.
