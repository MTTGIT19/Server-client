import socket
import ssl

# Connection info
hostname = "localhost"
port = 8443

# Specifying secure protocol, using OPENSSL created certs/keys
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('/file/location2')
context.check_hostname = False

# Connecting to Server and sending data, in this case a message
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        ssock.connect((hostname, port))
        message = 'Super Secret Luggage Combination: 1-2-3-4-5'
        ssock.sendall(message.encode())
        print ("Sending Secure Message")
        ssock.close()
