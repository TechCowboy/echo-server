import socket
import time
import datetime

hostname = socket.gethostname()

PORT = 6502

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((hostname, PORT))
    print("Connected to "+hostname)
    while True:
        time.sleep(3)
                   
        print("Sending data")
        
        now = datetime.datetime.now()
        current_time = now.strftime('%Y %m %d %H:%M:%S')
        current_time = bytearray(current_time.encode("ascii")) 
        s.sendall(current_time)
        print("Recieving data")
        data = s.recv(1024)
        print('Echoing: ', repr(data))