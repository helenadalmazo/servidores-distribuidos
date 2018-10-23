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
		msg_send = msg_recv
		conn.send(msg_send)
	print '\nFinalizando conexao do cliente ' + cli
	conn.close()

HOST = ''
PORT = 5001

print 'Digite o numero da porta que o server deve ouvir: '
msg_port = int(raw_input())

PORT = msg_port

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)

server_socket.bind(orig)
server_socket.listen(10)

print '\nServer disponivel'
while True:
	conn, cliente = server_socket.accept()
	print '\nConectado por ' + str(cliente[0]) + ', ' + str(cliente[1])
	t = Thread(target=conexao, args=(conn,cliente,))
	t.start()
