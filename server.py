#Servidor TCP
import socket
from threading import Thread

def conexao(conn,cli):
	msg_recv = ''
	while True:
		msg_recv = conn.recv(2048)
		if not msg_recv:
			break
		print '\nMensagem: ' + msg_recv
		msg_send = '-> ' + msg_recv.upper()
		conn.send(msg_send)
	print '\nFinalizando conexao do cliente ' + cli
	conn.close()

CONNECTIONS = []

HOST = ''
PORT = 5001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)

server_socket.bind(orig)
server_socket.listen(10)

while True:
	conn, cliente = server_socket.accept()
	print '\nConectado por ' + str(cliente[0]) + ', ' + str(cliente[1])
	t = Thread(target=conexao, args=(conn,cliente,))
	t.start()
