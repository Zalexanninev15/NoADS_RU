@echo off
wsl -e bash -c "python3 ./rules_collector.py; python3 ./hosts_collector.py"
pause
