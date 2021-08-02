import socket
import sys
import threading
import time

# IPV4
address_family = socket.AF_INET

# UDP
protocol = socket.SOCK_DGRAM

#Receiver function
def Receiver(ip1, port1, friend_name):
	s = socket.socket(address_family, protocol)
	#socket binding
	s.bind((ip1, port1))
	while True:
		msg = s.recvfrom(1024)	
		print("\n\t\t\t{0} said : ".format(friend_name), end = "")		
		print(msg[0].decode())
		time.sleep(0.3)

#Sender function
def Sender(ip2, port2, your_name):
	s = socket.socket(address_family, protocol)
	while True:
		#Enter your message
		text = input("You said : ")
		s.sendto(text.encode(), (ip2,port2))
		time.sleep(0.2)

your_name = input("Enter your name : ")
#Your IP address
ip2 = ""
port2 = int(input("Enter your Port number : "))

friend_name = input("\nEnter your Friend's name : ")
#Friend's IP address
ip1 = ""
port1 = int(input("Enter Friend's Port number : "))

x1 = threading.Thread(target=Receiver, args=(ip1, port1, friend_name))
x2 = threading.Thread(target=Sender, args=(ip2, port2, your_name))

x1.start()
x2.start()