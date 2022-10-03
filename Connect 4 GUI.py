import time
import os
import tkinter as tk
import random
import speech_recognition as sr

RowNum=6
ColNum=7

def playerSpeakRow(recog, mic):
	if not isinstance(recog, sr.Recognizer):
    	raise TypeError("recog must be Recognizer instance")

	if not isinstance(mic, sr.Microphone):
    	raise TypeError("mic must be Microphone instance")

	wordCheck = False
	speechWorks = True
	returnNum = 0

	while(wordCheck == False):

    	if(speechWorks == True):
        	print("Player __ Choose a Row 1-7")

    	speechWorks = True

    	with mic as source:
        	recog.adjust_for_ambient_noise(source)
        	audio = recog.listen(source)

    	try:
        	resp = recog.recognize_google(audio)
    	except sr.RequestError:
        	speechWorks = False
    	except sr.UnknownValueError:
        	speechWorks = False

    	if(speechWorks == True):
        	if (resp == "1"):
            	returnNum = '1'
            	wordCheck = True
        	elif (resp == "2"):
            	returnNum = '2'
            	wordCheck = True
        	elif (resp == "3"):
            	returnNum = '3'
            	wordCheck = True
        	elif (resp == "4"):
            	returnNum = '4'
            	wordCheck = True
        	elif (resp == "5"):
            	returnNum = '5'
            	wordCheck = True
        	elif (resp == "6"):
            	returnNum = '6'
            	wordCheck = True
        	elif (resp == "7"):
            	returnNum = '7'
            	wordCheck = True
        	else:
            	print("Response not accepted, please try again")

	return returnNum

class Connect4(tk.Tk):
	def __init__(self, *args, **kwargs):
    	tk.Tk.__init__(self, *args, **kwargs)
    	self.canvas = tk.Canvas(self, width=350, height=300, borderwidth=0, highlightthickness=0)
    	self.canvas.pack(fill="both", expand="true")

    	self.help=tk.Label(self, text="Press button and speak row you would like to place in")
    	self.help.pack()
   	 
    	self.player=tk.Label(self, text="Player 1")
    	self.player.pack()

    	x = tk.Button(self, text ="Take Turn", command = self.Validation)
    	x.pack()

    	self.valid=tk.Label(self, text="", foreground="red")
    	self.valid.pack()

    	self.reset=tk.Button(self, text="Reset game",command=self.resetGame)
   	 
    	self.rect = {}
    	self.oval = {}
    	self.title("Connect 4")
    	self.rows = 200
    	self.columns = 200
    	self.cellwidth = 50
    	self.cellheight = 50

   	 
    	for column in range(ColNum):
        	for row in range(RowNum):
            	x1 = column*self.cellwidth
            	y1 = row * self.cellheight
            	x2 = x1 + self.cellwidth
            	y2 = y1 + self.cellheight
            	self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill = "black", tags="rect")
            	self.oval[row,column] = self.canvas.create_oval(x1+2,y1+2,x2-2,y2-2,fill = "white", tags="oval")

	def Move(self, color, col):
    	self.canvas.itemconfig("rext", fill="red")
    	col =int(col)-1

    	row=self.Row(col)
    	itemId=self.oval[row,col]
    	self.canvas.itemconfig(itemId, fill=color)

    	if self.Winner(color):
        	self.reset.pack()

	def resetGame(self):
    	self.canvas.itemconfig("oval", fill="white")
    	self.player["text"]="Player 1"
    	self.reset.pack_forget()
    	self.help["text"]="Press enter when number has been chosen)"

	def Color(self, col):
    	playerTurn=self.player.cget("text")
    	if playerTurn=="Player 1":
        	color="yellow"
        	self.player["text"]="Player 2"
    	else:
        	color="red"
        	self.player["text"]="Player 1"
    	self.Move(color, col)

	def Row(self, col):
    	for y in range(RowNum-1, -1, -1):
        	itemId=self.oval[y, col]
        	if self.canvas.itemcget(itemId, "fill")=="white":
            	return y


	def Validation(self):
    	recog = sr.Recognizer()
    	mic = sr.Microphone()

    	Validation = playerSpeakRow(recog,mic)
    	col = Validation
 

    	if Validation=="":
        	self.valid["text"]="Please enter something into the entry box"
       	 
       	 
    	elif int(Validation) <=ColNum and int(Validation) >=1:
        	self.Color(col)
   	 
    	else:
        	self.valid["text"]="That move is invalid, please try again"
        	self.valid.after(2000, lambda: self.valid.config(text=""))


	def Winner(self, color):


    	for x in range(RowNum):
        	Total=0
        	for y in range(ColNum):
            	itemId=self.oval[x, y]
            	poscolor=self.canvas.itemcget(itemId, "fill")
            	if(poscolor == color):
                	Total+=1
            	else:
                	Total=0
            	if(Total==4):
                	self.help["text"]="Winner is:"
                	self.player["text"]=color
                	return True
   	 

    	for y in range(ColNum):
        	Total=0
        	for x in range(RowNum):
            	itemId=self.oval[x, y]
            	poscolor=self.canvas.itemcget(itemId, "fill")
            	if(poscolor == color):
                	Total+=1
            	else:
                	Total=0
            	if(Total==4):
                	self.help["text"]="Winner is:"
                	self.player["text"]=color
                	return True
   	 


    	MarkerValues = [[] for _ in range(ColNum + RowNum - 1)]
    	for x in range(RowNum):
        	for y in range(ColNum):
            	itemId=self.oval[x, y]
            	MarkerValues[x+y].append(self.canvas.itemcget(itemId, "fill"))
    	for d in MarkerValues:
        	Total = 0
        	for pdc in d:
            	if(pdc == color):
                	Total+=1
            	else:
                	Total=0
            	if(Total==4):
                	self.help["text"]="Winner is:"
                	self.player["text"]=color
                	return True
#  	Diagonal (/)
    	MarkerValues = [[] for _ in range(ColNum + RowNum - 1)]
    	for x in range(RowNum):
        	for y in range(ColNum):
            	itemId=self.oval[x, y]
            	y = ColNum - y - 1
            	MarkerValues[x+y].append(self.canvas.itemcget(itemId, "fill"))
    	for d in MarkerValues:
        	Total = 0
        	for pdc in d:
            	if(pdc == color):
                	Total+=1
            	else:
                	Total=0
            	if(Total==4):
                	self.help["text"]="Winner is:"
                	self.player["text"]=color
                	return True
    	return False

if __name__ == "__main__":
	app = Connect4()
	app.mainloop()



