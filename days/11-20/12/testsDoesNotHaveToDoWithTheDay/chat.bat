@echo off
set /p choice="Go to your website [Y/n]: "

if "%choice%"=="Y" (
    start https://fishin.me/leopi/
) else if "%choice%"=="n" (
    echo Stopping the process.
) else (
    echo Invalid choice.
)

pause