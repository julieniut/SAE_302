import socket , platform, psutil, os

host='0.0.0.0'
port=10000

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)

print("en attente du client")
conn, address = server_socket.accept()
print("Client connecter",{address})


message="je suis le serveur"

while message !="kill":
    #Réception des messages
    msg = conn.recv(1024)
    message= msg.decode()
    print(message)

    message_split= message.split()[0]
    try:
       message_split1 = message.split(":")[1]
    except:
        pass



    #traitement des Messages
    if message == "CPU":
        print(f"Processor: {platform.processor()}")
        conn.send(platform.processor().encode() )

    if message == "CPU%":
        print(f"cpu pourcent {psutil.cpu_percent()}")
        test=str(f"cpu {psutil.cpu_percent(4)} %")
        conn.send(test.encode())

    if message == "IP":
        print(server_socket.getsockname()[0])
        test=str(f"IP {server_socket.getsockname()[0]} ")
        conn.send( test.encode())

    if message == "RAM":
        print(f"Memory :{psutil.virtual_memory()}")
        test = str(psutil.virtual_memory())
        conn.send(test.encode())

    if message == "OS":
        print(f"System: {platform.platform()}")
        conn.send(platform.platform().encode())

    if message =="Name":
        print(f"Node Name: {platform.node}")
        conn.send(platform.node().encode())

    if message == "pythonV":
        print(f"Processor: {platform.python_version()}")
        conn.send(platform.python_version().encode())


    if message == "disconnet":
        fermeture = "Fermeture de la socket client"
        conn.send(fermeture.encode())
        #conn.close()
        print(fermeture)

    if message == "reset":
        reply="le serveur redémarre"
        conn.send(reply.encode())
        conn.close()
        print("Fermeture de la socket client")
        server_socket.close()
        print("Fermeture de la socket server")
        server_socket = socket.socket()
        server_socket.bind((host, port))
        server_socket.listen(1)
        conn, address = server_socket.accept()
        print("Client connecter", {address})

    if message_split == "mkdir":
        message=message.split()[1]
        commande = os.popen(f"mkdir {message}").read()
        reply= f"dossier {message}  créer"
        conn.send(reply.encode())

    if message == "Ping":
        commande = os.system("Ping 8.8.8.8")
        if commande==0:
         commande="Ping effectué sans erreur"
         conn.send(commande.encode())
        else:
            commande = "Ping effectué avec erreur"
            conn.send(commande.encode())

    if message_split == "ping":
        ping = os.popen(message).read()
        print(ping)
        conn.send(ping.encode())

    if message_split == "Powershell":
        power = os.popen(message).read()
        print(power)
        conn.send(power.encode())

    try:
        if message == f"DOS:{message_split1}":
          DOS = os.popen(message_split1).read()
          print(DOS)
          conn.send(DOS.encode())
    except:
        pass


    if message == 'connection information':
        hostname = socket.gethostname()
        address = socket.gethostbyname(hostname)
        message = str(f" \n Hostname : {hostname} \n IP: {address}")
        conn.send(message.encode())

    if message == 'get-process':
        process = os.popen('wmic process get description, processid').read()
        process = f'\n {process}'
        conn.send(process.encode())

    if message == 'help':
        a= " \n CPU \n CPU% \n IP \n RAM \n OS \n Name \n connection information \n pythonV \n DOS:dir \n mkdir {nom du dossier} \n disconnet \n reset \n Ping \n ping {address IP} \n Powershell {commande} \n get-process"
        conn.send(a.encode())
    else:
        #j'envoie un message
        reply = "Vérifier la saisie de la commandes \n (Voir DOC) "
        conn.send(reply.encode())
        print("MESSAGE reply envoyer")


conn.close()
print("Fermeture de la socket client")
server_socket.close()
print("Fermeture de la socket server")



