import socket
import ssl

# Connection Info -> Server
hostname = "localhost"
port = 8443

# Locations for OPENSSL created certs/keys
keyfile = '/file/location1'
certfile = '/file/location2'

# Specifying secure protocol
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile, keyfile)
context.check_hostname = False

# Bind socket for listening, decodes message into regular string.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
   with context.wrap_socket(sock, server_side=True) as ssock:
      ssock.bind((hostname, port))
      ssock.listen(1)
      print ('--- Server now active ---')
      conn, addr = ssock.accept()
      with conn:
         print(addr , "has connected!")
         while True:
            msg, addr = ssock.accept()
            message = (conn.recv(1024))
            print (message.decode())
