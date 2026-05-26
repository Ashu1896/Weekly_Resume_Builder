# schedule_task.ps1
# PowerShell script to register the Sunday Resume Builder automation task in Windows Task Scheduler.

$TaskName = "Weekly_Sunday_ATS_Resume_Optimization"
$BatchPath = "d:\Resume_Builder\run_sunday.bat"

# Ensure the batch file exists
if (-not (Test-Path $BatchPath)) {
    Write-Error "Error: Launcher batch file not found at $BatchPath"
    exit 1
}

# Define the action: Run the sunday.bat trigger script
$Action = New-ScheduledTaskAction -Execute $BatchPath -WorkingDirectory "d:\Resume_Builder"

# Define the trigger: Weekly on Sunday at 8:00 AM
$Trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 8:00AM

# Define settings: Run as soon as possible if a scheduled start is missed, and stop the task if it runs longer than 1 hour
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Hours 1)

# Register the scheduled task
Write-Host "Registering scheduled task '$TaskName' to run every Sunday at 8:00 AM..."
try {
    Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -Description "Automated Sunday ATS Resume Engineering, Quality Check, and Email Notification Pipeline" -Force -ErrorAction Stop
    Write-Host "Task successfully registered!" -ForegroundColor Green
    Write-Host "To test or run the task manually, execute: Start-ScheduledTask -TaskName '$TaskName'" -ForegroundColor Cyan
} catch {
    Write-Error "Failed to register scheduled task: $_"
    Write-Host "Please ensure you are running this PowerShell terminal as an Administrator." -ForegroundColor Red
}
