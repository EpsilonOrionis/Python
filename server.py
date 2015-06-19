import socket
import sys
 
HOST = ''   # Symbolic name, meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
 
# Bind socket to local host and port
try:
    s.bind((HOST, PORT))

# Handle exception socket error
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

# Prompt the following message 
print ('Socket bind complete')
 
# Start listening on socket
s.listen(10)
print ('Socket now listening')
 
# Now keep talking with the client
while 1:

    # Wait to accept a connection - blocking call
    conn, addr = s.accept()
    print ('New client connected')

# Close the socket
s.close()
