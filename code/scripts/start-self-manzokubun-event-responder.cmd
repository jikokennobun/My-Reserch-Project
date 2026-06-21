@echo off
setlocal
cd /d "%~dp0..\.."
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0start-self-manzokubun-event-responder.ps1" -ReplyMode QueueOnly
echo.
echo Self-Manzokubun event responder stopped.
pause
