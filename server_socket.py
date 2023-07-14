import socket
#server 1 tane çalıştırılabiliyor

#soket oluşturuluyor
server_socket = socket.socket()

#soket bağlantısı yapılıyor
server_socket.bind(("localhost", 50001))

#5e kadar client kabul edilebilir
server_socket.listen(5)
print( "Server is listening...")

while True:
    clienet_socket, address = server_socket.accept()
    print("Connection from: " + str(address))
    gelen_mesaj = clienet_socket.recv(1024).decode() #1024 byte alıyoruz max
    print("Gelen mesaj: " + gelen_mesaj)
    
    clienet_socket.close()
    
    if gelen_mesaj =='exit':
        break
    
print("Server is closing...")