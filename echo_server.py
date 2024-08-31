#!/usr/bin/env python3

import socket
import time
import errno

hostname = socket.gethostname()


local_ip = socket.gethostbyname(hostname)

HOST = local_ip    # Standard loopback interface address (localhost)
PORT = 6502        # Port to listen on (non-privileged ports are > 1023)


import socket

print("Echo Server Started at: "+hostname + " / "+local_ip+":"+str(PORT))

while True:
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print("connected by" + str(addr))
            while True:
                try:
                    
                    data = conn.recv(1024)
                    if data != b'':
                        print(f'Server Received: {data}  --> sending back')
                        conn.sendall(data)
                    else:
                        break
                except Exception as error:
                    print(error)
                    if error.errno in [errno.EPIPE, errno.ECONNRESET]:
                        break
    print("disconnected.")
    
                    
