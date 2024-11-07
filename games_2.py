# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:09:09 2023

@author: nikita
"""

import tkinter as T
#from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

def clik(n):
    
    if n==0:
        kb.start()
    if n==1:
        s.start()
    if n==2:
        xo.start()
    if n==3:
        tag.start()
    if n==4:
        sw.start()
    
'''Class KB START'''
class KB:
    #K=0,B=0,N=0#Cows, Bulls, Number of tryes
    #genr_str="" сгенерированная строка
    def genr(self):
        self.genr_str=""
        n=random.randint(0,9)
        for i in range(5):
            while str(n) in self.genr_str:
                n=random.randint(0,9)
            self.genr_str+=str(n)
    
    def cplay(self,a):
        self.play()
    
    def play(self):
        K=0
        B=0
        in_s=self.into.get()
        for i in in_s:
            n=self.genr_str.find(i)
            if n==in_s.find(i):
                B+=1
            elif n!=-1:
                K+=1
        self.N+=1
        t=self.tryes
        ttk.Label(t, text=in_s).grid(row=self.R,column=0)
        ttk.Label(t, text=K).grid(row=self.R,column=1)
        ttk.Label(t, text=B).grid(row=self.R,column=2)
        self.R+=1
        self.into.delete(0,len(in_s))
        if B==5:
            self.into.destroy()
            ttk.Button(t,text="Play again?", command=self.create).grid(row=self.R, column=1)   
        self.wnd.focus_set()
    def LEN(self,a):
        if len(self.into.get())>=5:
            return "break"
    def create(self):#create window view
        self.genr()
        for i in list(self.wnd.children.values()):
            i.destroy()
        self.wnd.geometry('200x500')
        self.wnd.title("Cow & Bull")
        
        self.into = ttk.Entry(self.wnd)#, textvariable = self.in_s.get()
        self.into.bind('<Return>', self.cplay)
        self.into.bind('<Key>', self.LEN)
        self.into.pack()
        self.b_ok = ttk.Button(self.wnd,text="OK", command = self.play)#
        self.b_ok.pack()
        #cow = ttk.Label(wnd,textvariable=in_str).pack()
        self.tryes=ttk.Frame(self.wnd)
        self.tryes.pack()
        self.R=0#row -> number of tryes(row)
        t=ttk.Label(self.tryes, text="tryes")
        t.grid(row=self.R,column=0)
        c=ttk.Label(self.tryes, text="cows")
        c.grid(row=self.R,column=1)
        b=ttk.Label(self.tryes, text="bulls")
        b.grid(row=self.R,column=2)
        self.R+=1
        self.into.focus_set()
        '''self.columns = ("try", "Cow","Bull")
        self.tryes = ttk.Treeview(self.wnd,columns = self.columns)
        self.tryes.pack()'''
    def start(self):
        self.N=0
        self.wnd=T.Toplevel()#T.Tk()
        self.create()

'''Class KB END'''
    
'''Class Story START'''
class Story:
    def show(self,i):
        #destroy buttons
        for k in list(self.wnd.children.values()):
            if k.widgetName == "ttk::button":
                k.destroy()
        s=""
        ways=[]
        for j in self.story:
            n=len(self.story)
            if j[0]==str(i):
                s=j[1]
                ways=j[2:n]
        ttk.Label(self.wnd,text=s).pack()
        if str(i).find("end")!=-1: #"You complete your story/ its your n ending from 4. Whana find anather one?"
                    ttk.Button(self.wnd,width=15,text="Start from the begining", command=self.create).pack()
                
        for n in ways:#вывод путей/выбора 
            if n!="" and n!="\n":
                start=n.find("(")
                end=n.find(")")
                _n=n[start+1:end]
                _s=n[:start]
                ttk.Button(self.wnd,text=_s, command = lambda k = _n:self.show(k)).pack(fill="x")#, command= lambda k = int(_n):self.show(_n)
        
    def create(self):
        for i in list(self.wnd.children.values()):
            i.destroy()
        self.wnd.geometry('1000x500')
        self.wnd.title("Spooky Story")
        self.show(1)
    def start(self):
        self.wnd=T.Toplevel()#T.Tk()
        self.create()
    def __init__(self):
        file = open("C:\\Users\\Admin\\Documents\\SimpleGames_py\\story.txt", 'r', encoding="UTF-8")#+проверка на открытие
        story_list=file.readlines()
        
        #parsing
        self.story=[]
        for s in story_list:
            t=s.split("#")
            self.story.append(t)
        file.close()
        #self.create()
'''Class Story END'''   

'''Class XO START'''  
class XO:
    figure=False
    mov_win=["012","345","678","036","147","258","048","246"]
    mov_x=""
    mov_o=""
    def chekWin(self,s):
        k=0;
        if len(s)<3:
            return False
        for i in self.mov_win:
            k=0
            for j in i:
                if s.find(j)!=-1:
                    k+=1
            if k==3:
                return True
            else:
                return False
            
    def click(self,a):
        if a.y<60:
            if a.x<60:
                m=0
                x=0
                y=0
            elif a.x>60 and a.x<110 :
                m=1
                x=60
                y=0
            elif  a.x>110:
                m=2
                x=110
                y=0
        elif a.y>60 and a.y<110:
            if a.x<60:
                m=3
                x=0
                y=60
            elif a.x>60 and a.x<110 :
                m=4
                x=60
                y=60
            elif  a.x>110:
                m=5
                x=110
                y=60
        elif a.y>110:
            if a.x<60:
                m=6
                x=0
                y=110
            elif a.x>60 and a.x<110 :
                m=7
                x=60
                y=110
            elif  a.x>110:
                m=8
                x=110
                y=110
        if self.figure:
            self.figure=False
            self.pole.create_oval(x+5,y+5,x+50,y+50)
            self.mov_o+=str(m)
            win=self.chekWin(self.mov_o)
        else:
            self.figure=True
            self.pole.create_line(x+5,y+5,x+50,y+50)
            self.pole.create_line(x+5,y+50,x+50,y+5)
            self.mov_x+=str(m)
            win=self.chekWin(self.mov_x)
        
    def create(self):
        for i in list(self.wnd.children.values()):
            i.destroy()
        self.wnd.geometry('200x200')
        self.wnd.title("TicTacToe")
        self.pole=T.Canvas(self.wnd, width=170, height=170,bg='white')#ширина
        self.pole.create_line(5,55,165,55, width=5)
        self.pole.create_line(5,110,165,110, width=5)
        self.pole.create_line(60,5,60,165, width=5)
        self.pole.create_line(110,5,110,165, width=5)
        self.pole.pack()
        self.pole.bind('<Button-1>',self.click)
        self.mov_x=""
        self.mov_o=""
        
    def start(self):
        self.wnd=T.Toplevel()#T.Tk()
        self.create()
'''Class XO END'''  

'''Class TAG START'''   
class TAG:
    right_pos=[]
    cur_pos=[]
    btn=[]
    
    def move(self, n, event):
        if "Event" in str(n):
            n=0
    # 1)ищем пустое место
        id0=self.cur_pos.index(0)
        r=T.Grid.grid_info(self.btn[id0])["row"]
        c=T.Grid.grid_info(self.btn[id0])["column"]
    # ) ищем возможные ходы
        if n==0:
            if event=='u' and r!=3:
                n=id0+4
            if event=='d'and r!=0:
                n=id0-4
            if event=='l'and c!=3:
                n=id0+1
            if event=='r'and c!=0:
                n=id0-1
        elif n!=id0+4 and n!=id0-4 and n!=id0+1 and n!=id0-1:
            n=id0
        
        posN=T.Grid.grid_info(self.btn[n])   #
    # 2)проверка возможных ходов
        t=False
        if posN["row"]==r+1 and posN["column"]==c:
            t=True
        elif posN["row"]==r-1 and posN["column"]==c:
            t=True
        elif posN["row"]==r and posN["column"]==c+1:
            t=True
        elif posN["row"]==r and posN["column"]==c-1:
            t=True
    # 3)двигаем пустое место
        if t:
            self.cur_pos[id0]=self.cur_pos[n]
            self.cur_pos[n]=0
            self.btn[id0]["text"]=self.btn[n]["text"]
            self.btn[id0]["state"]="available"
            self.btn[n]["text"]=""
            self.btn[n]["state"]="disabled"
        #else: shake()
        #check()
        ch=0
        for i in range(len(self.right_pos)):
            if self.right_pos[i]==self.cur_pos[i]:
                ch+=1
        if ch>14:
            print("WIN")
            self.win = messagebox.askyesno(title="WIN", message="Congrats!!!\nYou complete Tag! Start new game?")
            if self.win: 
                self.create()
            else: 
                self.wnd.destroy()
            
    def create(self):
        #5_90_5
        for i in list(self.wnd.children.values()):
            i.destroy()
        self.wnd.geometry('500x500')
        self.wnd.title("15")
        
        self.wnd.bind('<Up>',lambda a=0:self.move(a,'u'))
        self.wnd.bind('<Down>',lambda a=0:self.move(a,'d'))
        self.wnd.bind('<Left>',lambda a=0:self.move(a,'l'))
        self.wnd.bind('<Right>',lambda a=0:self.move(a,'r'))
        r=0
        c=0
        j=0
        
        random.shuffle(self.cur_pos)
        self.btn.clear()
        for i in self.cur_pos:
            self.btn.append(ttk.Button(self.wnd,width=5,text=i, command = lambda j = j:self.move(j,"")))
            if i==0 :
                self.btn[j]["text"]=""
                self.btn[j]["state"]="disabled"
            self.btn[j].grid(row=r,column=c)
            j+=1
            c+=1
            if c==4:
                r+=1
                c=0
        self.rest_btn=ttk.Button(self.wnd,width=5,text="restart", command=self.create).grid()
        self.wnd.focus_set()
    def start(self):
        self.wnd=T.Toplevel()#T.Tk()
        self.create()
    def __init__(self):
        for i in range(1,16):
            self.right_pos.append(i)
        self.right_pos.append(0)
        self.cur_pos.extend(self.right_pos)
'''Class TAG END''' 

'''Class SeaWar START'''   
class SeaWar:
    S="[4444] x {}\n[333] x {}\n[22] x {}\n[1] x {}"
    btn=[]#array with buttons of enemy_pole
    btn0=[]#array with buttons of my_pole
    my_ships=[]# 10x10 arr with ships on pole #пока не трогаем, это на новый год
    enemy_ships=[]# 10x10 arr with ships on pole
    ships=[4,3,3,2,2,2,1,1,1,1]
    num_ships=[4,3,2,1]#index+1=size, element=count
    num_enemy=[[1,1,1,1],[2,2,2],[3,3],[4]]#index+1=size, element=count
    I=0#index of first clic
    cls=0 #clics
    PLAY=False
    turn=True
    
    def shot(self,indx):
        if not self.PLAY:# 
            messagebox.showwarning(title="Warning!", message="You should put ALL you ships on a battlefield first!")
            self.wnd.focus_set()            
            return
        if self.plr_shot(indx):
            return
        else:
            self.turn=True
            while self.turn:
                self.turn=self.comp_shot()
    def plr_shot(self, indx):
        t=False
        n=self.enemy_ships[indx]#size of ship
        if n!=0:
            self.btn[indx]["text"]="x"
            s=self.num_enemy[n-1]
            for i in range(len(s)):
                if s[i]:
                    s[i]-=1#есть нюанс - если ударили не в продолжение а в другой корабль
                    if not s[i]:
                        s.remove(0)
                        ss=str(self.enemy_ships).replace(",","").replace(" ","").replace("[", "")
                        cery=[-10,10]
                        cerx=[-1,1]
                        k=indx
                        a=0
                        b=0
                        while len(cerx):
                            if ss[k] == ss[k+cerx[0]]:
                                k+=cerx[0]
                                b=k
                            elif ss[k] == ss[k+cery[0]]:
                                k+=cery[0]
                                b=k
                            else:
                                if not a:
                                    a=k
                                if not b:
                                    b=k
                                cerx.remove(cerx[0])
                                cery.remove(cery[0])
                        self.dis_cerc(a,b,self.btn)# how to count begin/end?
                    t=True
                    break
        self.btn[indx]["state"]="disabled"
        self.ships_info.set(self.S.format(len(self.num_enemy[3]),len(self.num_enemy[2]),len(self.num_enemy[1]),len(self.num_enemy[0])))
        return t
        
    
    def comp_shot(self):
        n = random.randint(0,99)
        k=False
        if self.btn[n]["text"] !="":
            k = True
        self.btn0[n]["text"]="X"
        self.btn0[n]["state"]="disabled"
        return k
        
    def chose(self, indx):
        a=0
        b=0
        self.cls+=1
        if self.cls==1:#begin of the ship
            self.I=indx
        else:#count size of the ship(a/b) and its coords(r/c)
            r=int(indx/10)
            c=indx%10
            
            r0=int(self.I/10)
            c0=self.I%10
            
            if c0<c:
                a=c-c0
            else:
                a=c0-c
            ###
            if r0<r:
                b=r-r0
            else:
                b=r0-r
            ### 
            if a>4 or b>4:# if you try to put unnormal size ship
                self.cls=0
                return
                
            if self.I>indx:
                self.I=indx
                    
            if a==0 and b==0 and self.num_ships[0]:#self.check_num_sh(1)
                self.btn0[self.I]["text"]=1
                #self.my_ships[self.I]=1
                self.num_ships[0]-=1
                self.dis_cerc(self.I,self.I, self.btn0)
            elif a==0 and self.num_ships[b]:#vertical position  self.check_num_sh(b+1)
                for i in range(b+1):
                    self.btn0[self.I+10*i]["text"]=b+1
                    #self.my_ships[self.I+10*i]=b+1
                self.num_ships[b]-=1
                self.dis_cerc(self.I, self.I+(b)*10,self.btn0)
            elif b==0 and self.num_ships[a]:#horizontal position self.check_num_sh(a+1)
                for i in range(a+1):
                    self.btn0[self.I+1*i]["text"]=a+1    
                self.num_ships[a]-=1
                self.dis_cerc(self.I,self.I+a, self.btn0)
            if self.num_ships.count(0)==4:
                self.PLAY=True
            self.cls=0
            self.ships_info0.set(self.S.format(self.num_ships[3],self.num_ships[2],self.num_ships[1],self.num_ships[0]))#self.four,self.three,self.two,self.one
            
    def dis_cerc(self, begin, end, ar):#ar
        x=begin%10
        y=int(begin/10)
        x0=end%10
        y0=int(end/10)
        i=begin
        #Проверяем края
        if x==x0:#vertical -1 +1
            #self.num_ships[y0-y]-=1
            if y!=0:
                ar[i-10]["state"]="disabled"#self.btn0
                if x!=9 and x0!=9:
                    ar[i-9]["state"]="disabled"
                if x!=0 and x0!=0:
                    ar[i-11]["state"]="disabled"
            while y<=y0:
                if x!=0:
                    ar[i-1]["state"]="disabled"
                if x!=9:
                    ar[i+1]["state"]="disabled"
                i+=10
                y+=1
            i-=10
            if y<=9:
                ar[i+10]["state"]="disabled"
                if x!=0 and x0!=0:
                    ar[i+9]["state"]="disabled"
                if x!=9 and x0!=9:
                    ar[i+11]["state"]="disabled"
        if y==y0:#horizontal-10 +10
            #self.num_ships[x0-x]-=1
            if x!=0:
                ar[i-1]["state"]="disabled"
                if y!=9 and y0!=9:
                    ar[i+9]["state"]="disabled"
                if y!=0 and y0!=0:
                    ar[i-11]["state"]="disabled"
            while x<=x0:
                if y!=0:
                    ar[i-10]["state"]="disabled"
                if y!=9:
                    ar[i+10]["state"]="disabled"
                i+=1
                x+=1
            i-=1
            if x<=9:
                ar[i+1]["state"]="disabled"
                if y!=0 and y0!=0:
                    ar[i-9]["state"]="disabled"
                if y!=9 and y0!=9:
                    ar[i+11]["state"]="disabled"

    def genrPole(self):#geners pole with enemy ships
        _pol=[]
        ships=self.ships#
        
        for i in range(100):
            _pol.append(True)#True=Empty/False=Can't Put Ship here
            self.enemy_ships.append(0)
            self.my_ships.append(0)
            
        for i in ships:
            t=True
            while t:
                x=random.randint(0,9)
                y=random.randint(0,9)
                _x=0
                _y=0
                n=y*10+x
                if _pol[n]:
                    axle=[0,1,2,3]
                #Проверяем на выход за границы
                    while t:
                        t=False
                        l=random.choice(axle)
                        if l==0 and y-i-1>=0:
                            _y=-1
                        elif l==1 and x+i-1<=9:
                            _x=1
                        elif l==2 and y+i-1<=9:
                            _y=1
                        elif l==3 and x-i-1>=0:
                            _x=-1
                        else:
                            axle.remove(l)
                            t=True
                    k=0
                #Проверяем на возможность размещения
                    for j in range(i):
                        a=(y+_y*j)*10+x+_x*j
                        if _pol[a]:
                            k+=1
                
                #Размещаем корабли на поле и запрещаем размещать рядом
                    if k==i: 
                        
                        for j in range(i):
                            n=(y+_y*j)*10+x+_x*j
                            self.enemy_ships[n]=i
                            cerc=[-11,-10,-9,-1,0,1,9,10,11]
                            if x==0:
                                cerc.remove(-11)
                                cerc.remove(-1)
                                cerc.remove(9)
                            if x==9:
                                cerc.remove(11)
                                cerc.remove(1)
                                cerc.remove(-9)
                            if y==0:
                                cerc.remove(-10)
                                if x!=9:
                                    cerc.remove(-9)
                                if x!=0:
                                    cerc.remove(-11)
                            if y==9:
                                cerc.remove(10)
                                if x!=0:
                                    cerc.remove(+9)
                                if x!=9:
                                    cerc.remove(11)
                            for k in cerc:
                                try:
                                    _pol[n+k]=False
                                except:
                                    print(n,k)
                            
                    else:
                        t=True
            

    def create(self):
        for i in list(self.wnd.children.values()):
            i.destroy()
        self.wnd.geometry('700x500')
        self.wnd.title("Sea Battle")
        self.pole=ttk.Frame(self.wnd)
        self.pole.pack()
        k=0
        self.btn.clear()
        self.btn0.clear()
        self.genrPole()
        for i in range(10):
            for j in range(10):
                k=i*10+j
                self.btn.append(ttk.Button(self.pole,width=3,command = lambda k = k:self.shot(k)))               
                self.btn[k].grid(row=i,column=j)
        self.spliter=ttk.Button(self.pole, width=3, state="disabled").grid(row= 0, column=11)
        k=0
        for i in range(10):
            for j in range(10):
                k=i*10+j
                self.btn0.append(ttk.Button(self.pole,width=3, command = lambda k = k:self.chose(k) ))#              
                self.btn0[k].grid(row=i,column=j+12)
                
        self.ships_info0=T.StringVar(self.wnd,self.S.format(self.num_ships[3],self.num_ships[2],self.num_ships[1],self.num_ships[0]))
        self.ships_info=T.StringVar(self.wnd,self.S.format(len(self.num_enemy[3]),len(self.num_enemy[2]),len(self.num_enemy[1]),len(self.num_enemy[0])))
        self.info0=ttk.Label(self.wnd, text="You need to put ships:").pack(anchor = "e",ipadx="30")
        self.info_r=ttk.Label(self.wnd, textvariable=self.ships_info0).pack(anchor = "e",ipadx="30")
        self.info=ttk.Label(self.wnd, text="You need to crash ships:").pack(anchor = "w",ipadx="30")
        self.info_l=ttk.Label(self.wnd, textvariable=self.ships_info).pack(anchor = "w",ipadx="30")
        
        '''
        self.play()
            if !self.one and !self.two and !self.three and !self.four:
                
        '''
    def start(self):
        self.wnd=T.Toplevel()#T.Tk()
        self.wnd.focus_set()
        self.create()
'''Class SeaWar END''' 


#MAIN#          
main_wind = T.Tk()
main_wind.title("Games2.0")
main_wind.geometry('500x500')
kb=KB()
s=Story()
xo=XO()
tag=TAG()
sw=SeaWar()
btn_kb = ttk.Button(main_wind,width=10,text="Cow & Bull", command = kb.start)#lambda n = 0:clik(n)
btn_kb.pack()
btn_story = ttk.Button(main_wind,width=10,text="Story",command = lambda n = 1:clik(n)).pack()
btn_xo = ttk.Button(main_wind,width=10,text="Tic Tac Toe", command = lambda n = 2:clik(n)).pack()
btn_15 = ttk.Button(main_wind,width=10,text="Tag", command = lambda n = 3:clik(n)).pack()
btn_sw = ttk.Button(main_wind,width=10,text="SeaWar", command = sw.start).pack()#lambda n = 4:clik(n)


main_wind.mainloop()

