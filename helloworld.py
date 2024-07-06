import socket
import os


host = "192.160.0.196"

if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP

    sniffer  = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

    sniffer.bind()