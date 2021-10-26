import subprocess

list_dir = subprocess.Popen(["lscpu", "-l"])
list_dir.wait()
