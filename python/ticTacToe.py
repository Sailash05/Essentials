import os
a=['a','b','c','d','e','f','g','h','i']
play=1
class game:
    def __init__(self,ls):
        self.ls=ls
        self.running=True        print(self.ls[0],'|',self.ls[1],'|',self.ls[2])
        print(self.ls[3],'|',self.ls[4],'|',self.ls[5])
        print(self.ls[6],'|',self.ls[7],'|',self.ls[8]) 
    def result(self,winn):
        self.winn=winn
        if self.winn=="X":
            print("Winner is player X")
            self.running=False
        elif self.winn=="O":
            print("Winner is player O")
            self.running=False
    def answer(self):
        if self.ls[0]==self.ls[1] and self.ls[1]==self.ls[2]:
            self.win=self.ls[0]
            self.result(self.win)
        elif self.ls[3]==self.ls[4] and self.ls[4]==self.ls[5]:
            self.win=self.ls[3]
            self.result(self.win)
        elif self.ls[6]==self.ls[7] and self.ls[7]==self.ls[8]:
            self.win=self.ls[6]
            self.result(self.win)
        elif self.ls[0]==self.ls[3] and self.ls[3]==self.ls[6]:
            self.win=self.ls[0]
            self.result(self.win)
        elif self.ls[1]==self.ls[4] and self.ls[4]==self.ls[7]:
            self.win=self.ls[1]
            self.result(self.win)
        elif self.ls[2]==self.ls[5] and self.ls[5]==self.ls[8]:
            self.win=self.ls[2]
            self.result(self.win)
        elif self.ls[0]==self.ls[4] and self.ls[4]==self.ls[8]:
            self.win=self.ls[0]
            self.result(self.win)
        elif self.ls[2]==self.ls[4] and self.ls[4]==self.ls[6]:
            self.win=self.ls[2]
            self.result(self.win)
        else:
            if self.player==1:
                self.start_game(2)
            elif self.player==2:
                self.start_game(1)       
    def display(self):
        print(self.ls[0],'|',self.ls[1],'|',self.ls[2])
        print(self.ls[3],'|',self.ls[4],'|',self.ls[5])
        print(self.ls[6],'|',self.ls[7],'|',self.ls[8])
        self.answer()
    def printing(self,index):
        self.index=index
        if self.player==1:
            self.ls[self.index]="X"
            self.display()
        else:
            self.ls[self.index]="O"
            self.display()
    def checking(self,position,i):
        self.position=position
        self.i=i
        ab=len(self.ls)
        while self.i<ab:
            if self.ls[i]==self.position:
                self.printing(i)
                break
            else:
                self.i+=1
                self.checking(self.position,self.i)
        else:
            if self.running:
                print("Wrong input")
                print(self.ls[0],'|',self.ls[1],'|',self.ls[2])
                print(self.ls[3],'|',self.ls[4],'|',self.ls[5])
                print(self.ls[6],'|',self.ls[7],'|',self.ls[8])
                self.start_game(self.player)
            else:
                pass
    def start_game(self,player):
        self.player=player
        xyz=0
        if self.running:
            if self.player==1:
                self.pos=input("Player x : ")
                os.system('clear')
                self.checking(self.pos,xyz)
            else:
                self.pos=input("Player O : ")
                os.system('clear')
                self.checking(self.pos,xyz)   
b=game(a)
b.start_game(play)
