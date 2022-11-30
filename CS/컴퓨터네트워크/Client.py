#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:22:42 2022

@author: chaehanbin
"""

import socket
IP = "192.168.35.253"
PORT = 7777
address = (IP,PORT)

client = socket.socket()
client.connect(address)
print('1. ----- Server is connected -----')
while True:
    client.send(input().encode()) # encode 문자->바이트
    print('2. ----- Message send -----')
    
    rxmsg = client.recv(1024)
    print('3. ----- message recieved -----')
    print("RX:",rxmsg.decode())
    
client.close()
