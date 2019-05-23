import socket

HOST = '127.0.0.1'
PORT = 8484
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print('aguardando conexão...')

conn1, addr1 = s.accept()
print ('consagrado no ip ' + addr1[0] + ' se conectou.' ), addr1

close = False

while not close:
    try:
        data = conn1.recv(1024)
    except socket.error:
        print ('Deu ruim...')
    if data:
        print (data.decode('utf-8'))
        conn1.send('data'.encode())
        close = True