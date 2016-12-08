# interface graphique de visualisation de données de x plane

#lit le fichier et liste les variables

#bouton connecter: lance la connexion au serveur
#					enregistre les variable sur le serveur
#		commence a mettre a jour la grille



from tkinter import *

# use customize font

#define MYFONT = ("Helvetica", 15)

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
		self.serverIP = StringVar()
		self.serverPort = IntVar()

	def initialize(self):
		'''definition du contenue de la fenetre'''

		# top frame, content: labels and buttons
		self.frame1 = Frame(self, borderwidth=2, relief=GROOVE)
		self.frame1.pack(side=TOP)
		# middle frame, content xplane vars and values
		self.frame2 = Frame(self,borderwidth=2, relief=GROOVE)
		self.frame2.pack(side=TOP)
		# bottom frame, content: quit button
		self.frame3 = Frame(self,borderwidth=2, relief=GROOVE)
		self.frame3.pack(side=BOTTOM)


		# labels, entry and buttons
		self.labIP = Label(self.frame1,text="IP Serveur:")
		self.labPort = Label(self.frame1,text="Port:")
		self.but = Button(self.frame3, text="Quitter", command= self.destroy)
		self.but.pack(side=RIGHT)
		self.but1 = Button(self.frame1,text="Connect", command= self.but1_click)
		self.entIP = Entry(self.frame1, width = 15)
		self.entPort = Entry(self.frame1, width = 5)

		self.la = Label(self.frame2, text="APU").grid(row=0, column=0)
		self.lo = Label(self.frame2, text="ON").grid(row=0, column=1)
		self.grille = Grid()


		# packing
		self.labIP.pack(side=LEFT)
		self.entIP.pack(side=LEFT)
		self.labPort.pack(side=LEFT)
		self.entPort.pack(side=LEFT)
		self.but1.pack(side=LEFT)

	def but1_click(self):
		'''try to connect to the iocp server'''
		print(" cliqué ")
		print("IP: ",self.entIP.get()," Port: ",self.entPort.get())
		
		if self.but1["text"] == "Connect":
			self.but1["text"] = ".Stop ."
			# do something
		else:
			self.but1["text"] = "Connect"
			#close connection with the server
		

if __name__ == "__main__":
	fen = IOCPController()
	fen.mainloop()


		
