import socket
import threading
import os
import datetime

print('')

family = socket.AF_INET
protocol = socket.SOCK_DGRAM
print('~'*(23) + 'ChatAPP Using Python' + '~'*(23) + '\n')

socket1 = socket.socket(family , protocol)
server_ip1 = input('Enter your ip : ')
server_port1 = int(input('Enter your port number : '))
#server_ip1 = "192.168.43.130"
#server_port1 = 5555
socket1.bind((server_ip1 , server_port1))

socket2 = socket.socket(family , protocol)
server_ip2 = input('Enter other end ip : ')
server_port2 = int(input('Enter other end port number : '))
#server_ip2 = "192.168.43.56"
#server_port2 = 5555


print('')

def time():

   t = str(datetime.datetime.now())
   t = t.split(' ')[1][:5]
   return t

def receive():
  while 1:
    
    buffer_size = 1024
    msg = socket1.recvfrom(buffer_size)
    print(msg[0].decode())
    t_ = time()
    print('__'*(34) + t_ + '\n')

def send():
  while 1:
    
    msg = input()
    socket2.sendto(msg.encode() , (server_ip2 , server_port2))
    t_ = time()
    print('__'*(34) + t_ + '\n')

print('~'*(29) + 'ChatApp' + '~'*(29) + '\n')

receiveThread = threading.Thread(target = receive)
sendThread = threading.Thread(target = send)

receiveThread.start()
sendThread.start()




