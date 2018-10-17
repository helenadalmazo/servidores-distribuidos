#Cliente TCP
import socket

server = []

def search_servers():
	arq = open('servers.txt', 'r')
	for linha in arq :
		server_info = linha.split(',')

		name = server_info[0]
		address = server_info[1].replace(" ", "")
		port = server_info[2].replace(" ", "").replace("\n", "")

		try:
			print "Trying connection... Server name: " + name + ", Address: " + address + ", Port: " + port
			dest = (address, int(port))
			global client_socket
			client_socket.connect(dest)
			print "CONNECTION ESTABLISHED\n"
			global server
			server = (name, address, port)
			break;
		except Exception as e:
			print "CONNECTION FAILED: " + str(e) + "\n"
		#	print type(e)
		#	print e.args
		#	print e
	arq.close()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

search_servers()

print "\n Para sair use CTRL+X"

msg_send = ''
#Oct	Dec		Char	Hex		Key		Coments
#\030	24		CAN  	\x18	^X		(Cancel)
while msg_send != '\x18':

	msg_send = raw_input()

	try:
		client_socket.send(msg_send)
		msg_recv = client_socket.recv(1024)
	except Exception as e:
		print "Unexpected error: " + str(e)
		print "Searching new server..."
		search_servers()
		continue

	print server[0] + ": " + msg_recv + "\n"

client_socket.close()
