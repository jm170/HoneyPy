#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
from datetime import datetime

def honeypot(host, port):
    try:
        # Create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Bind the socket to the host and port
        server_socket.bind((host, port))
        
        # Start listening for incoming connections
        server_socket.listen(5)
        
        print(f"Honeypot listening on {host}:{port}")
        
        while True:
            # Accept incoming connections
            client_socket, addr = server_socket.accept()
            print(f"Connection from: {addr[0]}:{addr[1]}")
            
            # Get current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Log the connection details along with timestamp
            with open("honeypot3.log", "a") as log_file:
                log_file.write(f"[{timestamp}] Connection from: {addr[0]}:{addr[1]}\n")
            
            # Close the client socket
            client_socket.close()
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the server socket
        server_socket.close()

if __name__ == "__main__":
    # Specify the host and port to listen on
    HOST = "0.0.0.0"  # Listen on all available interfaces
    PORT = 3389  # Specify a port of your choice
    
    # Start the honeypot
    honeypot(HOST, PORT)
