#!/usr/bin/python

import socket


ip = raw_input("Enter the ip: ")
port = input("Enter the port: ")

s 

#creating a TCP network socket ->
# socket.socket(socket.AF_NET,socket.SOCK_STREAM)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if s.connect_ex((port, host)):
	print("Port", port , " is closed") 
else:
	print("port", port " is open")

