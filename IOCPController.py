# interface graphique de visualisation de données de x plane

#lit le fichier et liste les variables

#bouton connecter: lance la connexion au serveur
#					enregistre les variable sur le serveur
#		commence a mettre a jour la grille



from tkinter import *

# use customize font
MYFONT = ("Helvetica", 15)

class IOCPController(Tk):
	''' Main window'''
	def __init__(self):
		''' init, titre et taille'''
		# fichier datos en entree
		Tk.__init__(self)
		self.title("IOCPController")
		self.initialize()
		self.geometry("600x800")

		# vars
		self.serverIP = 0
		self.serverPort = 0

	def initialize(self):
		'''definition du contenue de la fenetre'''

		# top frame, content: labels and buttons
		self.frame1 = Frame(self, borderwidth=2, relief=GROOVE)
		self.frame1.pack(side=TOP)
		# middle frame, content xplane vars and values
		self.frame2 = Frame(self,borderwidth=2, relief=GROOVE,bg = '#fff')
		self.frame2.pack(side=TOP)
		self.frame2.columnconfigure(0,minsize=300)
		self.frame2.columnconfigure(1,minsize=200)
		# bottom frame, content: quit button
		self.frame3 = Frame(self,borderwidth=2, relief=GROOVE)
		self.frame3.pack(side=BOTTOM)


		# labels, entry and buttons
		self.labIP = Label(self.frame1,text="IP Serveur:",font=MYFONT)
		self.labPort = Label(self.frame1,text="Port:",font=MYFONT)
		self.but = Button(self.frame3, text="Quitter",font=MYFONT, command= self.destroy)
		self.but.pack(side=RIGHT)
		self.but1 = Button(self.frame1,text="Connect",font=MYFONT ,command= self.but1_click)
		self.entIP = Entry(self.frame1, width = 15,font=MYFONT)
		self.entPort = Entry(self.frame1, width = 5,font=MYFONT)

		self.la = Label(self.frame2, text="NAME").grid(row=0, column=0,sticky = W)
		self.lo = Label(self.frame2, text="VALUE").grid(row=0, column=1,sticky = E)
		self.grille = Grid()
	


		# packing
		self.labIP.pack(side=LEFT)
		self.entIP.pack(side=LEFT)
		self.labPort.pack(side=LEFT)
		self.entPort.pack(side=LEFT)
		self.but1.pack(side=LEFT)


		# add menu to open file and display them in the grid

	def but1_click(self):
		'''try to connect to the iocp server'''
		print(" cliqué ")
		if self.but1["text"] == "Connect":
			self.but1["text"] = ".Stop ."
			print("IP: ",self.entIP.get()," Port: ",self.entPort.get())
			self.serverIP = self.entIP.get()
			# error if a letter is enter for port-----------------------
			self.serverPort = int(self.entPort.get())
			print(self.serverPort)
			# do something
		else:
			self.but1["text"] = "Connect"
			print("Stop connection to the server")
			#close connection with the server
		

if __name__ == "__main__":
	fen = IOCPController()
	fen.mainloop()


		
