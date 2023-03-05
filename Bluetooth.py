import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# Bind the socket to a specific address and port
server_sock.bind(("", bluetooth.PORT_ANY))

# Listen for incoming connections
server_sock.listen(1)

port = server_sock.getsockname()[1]

# Make the service visible
uuid = "00001101-0000-1000-8000-00805F9B34FB"
bluetooth.advertise_service(server_sock, "MyServer",
                            service_id=uuid,
                            service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                            profiles=[bluetooth.SERIAL_PORT_PROFILE],
                            )

print("Waiting for connection on RFCOMM channel", port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from", client_info)

try:
    while True:
        data = client_sock.recv(1024)
        if len(data) == 0:
            break
        print("received", data)
        client_sock.send("Thank you for sending message")
except IOError:
    pass

print("disconnected")

client_sock.close()
server_sock.close()
