import subprocess

list_dir = subprocess.Popen(["./build", "ls"])
list_dir.wait()
