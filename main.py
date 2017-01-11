import socket

sock = socket.socket()

x = int(input("Insert port: "))
sock.bind(("", x))

sock.listen(10)

def ret_http(conn, addr, data):
	conn.send(b"HTTP/1.1 200 OK\r\n")
	conn.send(b"Host: " + addr[0].encode("utf-8") + b"\r\n")
	conn.send(b"Content-Type: text/html; charset=UTF-8\r\n")
	conn.send(b"Connection: close\r\n")
	conn.send(b"Content-Length:" + bytes(len(data)) + b"\r\n\r\n")

	conn.send(data.encode("utf-8"))

while True:
	conn, addr = sock.accept()
	print(addr[0], " joined")
	ret_http(conn, addr, "Your ip: " + addr[0])