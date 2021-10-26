import subprocess

list_dir = subprocess.Popen(["ls", "ls"])
list_dir.wait()
