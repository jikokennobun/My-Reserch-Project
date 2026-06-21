@echo off
setlocal

set "REPLY_MODE=%~1"
if "%REPLY_MODE%"=="" set "REPLY_MODE=QueueOnly"
set "AI_CHAT_CHANNEL_ID=%~2"

cd /d "%~dp0..\.."
if not exist "records\logs" mkdir "records\logs"

echo [%date% %time%] Starting Self-Manzokubun event responder. ReplyMode=%REPLY_MODE%>>"records\logs\self-manzokubun-event-responder.out.log"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0start-self-manzokubun-event-responder-scheduled.ps1" -ReplyMode "%REPLY_MODE%" -ChannelId "%AI_CHAT_CHANNEL_ID%" >>"records\logs\self-manzokubun-event-responder.out.log" 2>>"records\logs\self-manzokubun-event-responder.err.log"
echo [%date% %time%] Self-Manzokubun event responder stopped. ExitCode=%ERRORLEVEL%>>"records\logs\self-manzokubun-event-responder.out.log"
