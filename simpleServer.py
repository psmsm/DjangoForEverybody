from socket import *
 cdef createServer():
    server_socket = socket(AF_INET, SOCK_STREAM)

    try:
        server_socket.bind(('localhost', 2120))
        server_socket.listen(5)

        while(1):
            # socket object usable to send and receive data on the connection
            client_socket, address = server_socket.accept() 

            rd = client_socket.recv(5000).decode() # bytes->str
            pieces = rd.split('\n')

            if len(pieces) > 0:
                print(pieces[0])

            # header
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html;\r\n"
            data += "\r\n"
        
            # data
            data += "<html><body>Hello World</body></html>\r\n\r\n"

            client_socket.sendall(data.encode('utf-8'))
            client_socket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down..\n")
    except Exception as exc:
        print("Error: \n")
        print(exc)

    server_socket.close()

print("Access http://localhost:2120")
createServer()