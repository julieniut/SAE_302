import socket

fichier = "data.txt"
lignes = []
with open(fichier, "r", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.rstrip()  # supprime la fin de ligne
        lignes.append(ligne)  # ajoute la ligne à la liste
        #print(ligne)

host=ligne
port=10000

client_socket = socket.socket()
client_socket.connect((host, port))

message="je suis le client"
print("Serveur est connecté")
while message !="disconnet":
    message = input("saisir le message ")
    client_socket.send(message.encode())
    print("Message envoyé")

    message = client_socket.recv(1024).decode()
    print(f"Envoyé du serveur, {message}")


client_socket.close()
print("deconnecter")