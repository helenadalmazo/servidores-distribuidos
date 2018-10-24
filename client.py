#Cliente TCP
import socket

client_socket = ''
server = []

def search_servers():
	arq = open('servers.txt', 'r')
	for linha in arq :
		server_info = linha.split(',')

		name = server_info[0]
		address = server_info[1].replace(" ", "")
		port = server_info[2].replace(" ", "").replace("\n", "")

		try:
			# print "Trying connection... Server name: " + name + ", Address: " + address + ", Port: " + port
			global client_socket
			client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client_socket.settimeout(0.5)
			dest = (address, int(port))
			client_socket.connect(dest)
			# print "CONNECTION ESTABLISHED\n"
			
			global server
			server = (name, address, port)
			arq.close
			return True
		except Exception as e:
			e
			# print "CONNECTION FAILED: " + str(e) + "\n"
			# print type(e)
			# print e.args
			# print e
	arq.close()
	return False

print "\n Para sair use CTRL+X\n"
print "Buscando servidores disponiveis, por favor aguarde...\n"

ok = search_servers()

retry_send = False
msg_send = ''
#Oct	Dec		Char	Hex		Key		Coments
#\030	24		CAN  	\x18	^X		(Cancel)
while msg_send != '\x18':

	if ok is False:
		print "Todos os servidores estao indisponiveis. Tente novamente mais tarde.\n"

	if retry_send is False:		
		msg_send = raw_input()

	try:
		client_socket.send(msg_send)
		msg_recv = client_socket.recv(1024)
		retry_send = False
	except Exception as e:
		# print "Unexpected error: " + str(e)
		# print "Searching new server..."
		ok = search_servers()
		if ok:
			retry_send = True
		continue

	print str(server) + ": " + msg_recv + "\n"

client_socket.close()
