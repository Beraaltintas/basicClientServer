import socket

client_socket = socket.socket()
client_socket.connect(("localhost", 50001))
mesaj = input("Mesajınızı giriniz: ")
#cikis_mesaji = "exit"
client_socket.send(bytes(mesaj ,'utf-8'))
client_socket.close()