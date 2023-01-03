from tkinter import *
import socket , platform, psutil, os

root = Tk()
root.title("SAE 3.02 LOSSER Julien")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"



host='0.0.0.0'
port=10000

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)

print("en attente du client")
conn, address = server_socket.accept()
print("Client connecter",{address})
message="je suis le serveur"


# Send function
def send():
		send = "You -> " + e.get()
		txt.insert(END, "\n" + send)
		user = e.get().lower()

		if (user == "ram"):
			print(f"Memory :{psutil.virtual_memory()}")
			test = str(psutil.virtual_memory())
			txt.insert(END,"\n",test)

		if (user == "ip"):
			print(server_socket.getsockname()[0])
			test = str(f" {server_socket.getsockname()[0]} ")
			txt.insert(END, test )

		elif (user == "cpu"):
			print(f"Processor: {platform.processor()}")
			test = str(f" {platform.processor()} ")
			txt.insert(END, test)

		elif (user == "cpu%"):
			print(f"{psutil.cpu_percent()}")
			test = str(f" {psutil.cpu_percent(4)} %")
			txt.insert(END, test)

		elif (user == "os"):
			print(f"System: {platform.platform()}")
			test = str(f" {platform.platform()} ")
			txt.insert(END, test)

		elif (user == "name"):
			print(f"Node Name: {platform.node}")
			test = str(f" {platform.node()} ")
			txt.insert(END, test)

		elif (user == "pythonv"):
			print(f"python version: {platform.python_version()}")
			test = str(f" {platform.python_version()} ")
			txt.insert(END, test)

		elif (user == "disconnet"):
			test = "Fermeture de la socket client"
			txt.insert(END, test)

		elif (user == "reset"):
			reply = "le serveur redémarre"
			txt.insert(END,reply)
			print("Fermeture de la socket client")
			server_socket.close()
			print("Fermeture de la socket server")
			server_socket = socket.socket()
			server_socket.bind((host, port))
			server_socket.listen(1)
			conn, address = server_socket.accept()
			print("Client connecter", {address})

		elif (user == "mkdir"):
			message = message.split()[1]
			commande = os.popen(f"mkdir {message}").read()
			reply = f"dossier {message}  créer"
			txt.insert(END, reply)

		elif user == "ping":
			commande = os.system("Ping 8.8.8.8")
			if commande == 0:
				commande = "Ping effectué sans erreur"
				txt.insert(END, commande)
			else:
				commande = "Ping effectué avec erreur"
				txt.insert(END, commande)

		elif (user == "connection information"):
			hostname = socket.gethostname()
			address = socket.gethostbyname(hostname)
			message = str(f" \n Hostname : {hostname} \n IP: {address}")
			txt.insert(END, message)

		elif user== 'get-process':
			process = os.popen('wmic process get description, processid').read()
			process = f'\n {process}'
			txt.insert(END, process)

		elif user == 'help':
			a = " \n CPU \n CPU% \n IP \n RAM \n OS \n Name \n connection information \n pythonV  \n disconnet \n reset \n Ping \n Powershell {commande} \n get-process"
			txt.insert(END, a)

		else:
			txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")

		e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
			command=send).grid(row=2, column=1)

root.mainloop()
