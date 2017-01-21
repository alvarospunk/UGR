#coding=utf-8
import subprocess
import time

aux = []

with open("/etc/ssh/sshd_config", "r") as file:
	for line in file:
		if ("#PasswordAuthentication yes") or ("PasswordAuthentication no") in line:
			line = "PasswordAuthentication yes\n"
		aux.append(line)

with open("/etc/ssh/sshd_config", "w") as file:
	for line in aux:
		file.write(line)

command = ['service', 'ssh', 'restart'];
subprocess.call(command, shell=False)

print("Acceso por contraseña habilitado")
time.sleep(30)

aux2 = []

with open("/etc/ssh/sshd_config", "r") as file:
	for line in file:
		if "PasswordAuthentication yes"in line:
			line = "#PasswordAuthentication yes\n"
		aux2.append(line)

with open("/etc/ssh/sshd_config", "w") as file:
	for line in aux2:
		file.write(line)

subprocess.call(command, shell=False)

print("Acceso cerrado")
