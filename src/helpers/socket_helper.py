import socket


def get_host_name():
    return str(socket.gethostname())


def get_host_ip():
    return str(socket.gethostbyname(socket.gethostname()))
