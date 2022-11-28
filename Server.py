import socket
import sys
s= socket.socket()
print("Socket successfully created")
port = 12345
s.bind(('',port))
print(f"Socket binded to {port}")
s.listen(5)
print("Socket is listening")
while True:
  c, addr = s.accept()
  print("Got connection from ",addr)
  c.send("Thankyou for connecting".encode())
  c.close()
  break
