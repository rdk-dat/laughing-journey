import psutil
import datetime

with open("proc_log.txt", "a") as f:
    f.write(f"\n===== {datetime.datetime.now()} =====\n")
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        f.write(str(proc.info) + "\n")
