import subprocess

list_dir = subprocess.Popen(["lscpu", "ls"])
list_dir.wait()
