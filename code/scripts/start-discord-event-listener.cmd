@echo off
setlocal
cd /d "%~dp0..\.."
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0watch-discord-message-events.ps1" -AiReplyMode QueueOnly
echo.
echo Discord event listener stopped.
pause
