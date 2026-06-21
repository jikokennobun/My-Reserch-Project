@echo off
setlocal
cd /d "%~dp0\..\.."
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0set-discord-bot-config.ps1" -GuildId 1514540747662033027 -ChannelId 1515810167726411926
echo.
echo If the script says it saved the config, you can close this window.
pause
