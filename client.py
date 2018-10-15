#Cliente TCP
import socket

SERVER = '127.0.0.1'
PORT = 5001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (SERVER, PORT)

client_socket.connect(dest)

print "\n Para sair use CTRL+X"

msg_send = ''
#Oct	Dec		Char	Hex		Key		Coments
#\030	24		CAN  	\x18	^X		(Cancel)
while msg_send != '\x18':

	msg_send = raw_input()
	client_socket.send(msg_send)

	msg_recv = client_socket.recv(1024)
	print msg_recv + "\n"

client_socket.close()
