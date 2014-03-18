#official version stable release pytle0_1_0
#author rohit
#roit.shetty@gmail.com
from turtle import *#imports LOGO
from Tkinter import*#imports GUI 
#global defs 
global k
global c
global num
global t
global path
global i
global ini 
global p
global ofris
global copy
global isa
global var
global a
#global decs
ini=1
copy=[]
p=[]
i=0
num=0
path=[]
path.append("stop")
k=[]
a = Pen()    # Creates a graphics window
#module for calculating wts the number in tabs
def enter():
	global k
	global num
	num=0
	i=0
	n=len(k)
	while i<n:
		num=(num*10)+k[i]
		i=i+1
	print num
	i=0
	while i<n:
		k[i]=0
		i=i+1
	return()
#module for executing the recorded macro
def ent():
	global p
	global p1
	global path
	global ini
	j=0
	global num
	global copy
	num=0
	p1.destroy()
	i=0
	n=len(p)#finding entered num
	while i<n:
		num=(num*10)+p[i]
		i=i+1
	print num
	del p		
	p=[]	
	t=0	
	q=len(path)
	i=0
	r=0#copy that respective paths to copy[]
	while i<q:
		if path[i]=="stop":
			r=r+1
		if num==r:
			t=0
			w=i
			while path[w+1]!="stop":
				copy.append(path[w+1])
				w=w+1
			break			
		i=i+1
	print copy
	c=len(copy)
	a1=0
	h=0
	j=0
	print ini,type(ini)
	ini=int(ini)
	print ini,type(ini)
	for k in range(ini):#forlooped variable
		while a1<c:#executing
			if copy[a1]=="up":
				a.forward(copy[a1+1])
				a1=a1+1
			elif copy[a1]=="left":
				a.left(copy[a1+1])
				a1=a1+1
			elif copy[a1]=="right":
				a.right(copy[a1+1])
				a1=a1+1
			elif copy[a1]=="cir":
				a.circle(copy[a1+1])
				a1=a1+1
			elif copy[a1]=="back":
				a.left(180)
				a1=a1+1
			else:
				a.forward(0)
				a1=a1+1
		a1=0
	del copy			
	copy=[]
#module for looping entity
def ll():
	global inti
	global ini
	ini=inti.get()
	print ini
	global q	
	q.destroy()
#looping enteryfield
def loop():
	global q
	global var
	global inti
	q=Toplevel()
	w=Button(q,text="ok",command=ll)
	w.grid(row=2,column=1)
	inti = IntVar()
	inti = Entry(q)
	inti.grid(row=1,column=1)	
	print var.get()
#records macro
def rec():
	global i
	i=1
# number padding for parent
def d1():
		global k
		k.append(1)
def d2():
		global k
		k.append(2)
def d3():
		global k
		k.append(3)
def d4():
		global k
		k.append(4)
def d5():
		global k
		k.append(5)
def d6():
		global k
		k.append(6)
def d7():
		global k
		k.append(7)
def d8():
		global k
		k.append(8)
def d9():
		global k
		k.append(9)

def d0():
		global k
		k.append(0)
#number padding for parent ends
#toplevel module number padding
def p11():
		global p
		p.append(1)
def p2():
		global p
		p.append(2)
def p3():
		global p
		p.append(3)
def p4():
		global p
		p.append(4)
def p5():
		global p
		p.append(5)
def p6():
		global p
		p.append(6)
def p7():
		global p
		p.append(7)
def p8():
		global p
		p.append(8)
def p9():
		global p
		p.append(9)
		
def p0():
		global p
		p.append(0)
#toplevel module number padding ends
#predefined commands 
def up():
	global num
	global i
	global path
	
	print enter()
	if i==1:
		path.append("up")
		path.append(num)
	a.forward(num)
	print path
def stop():
	global i
	i=0
	m=len(path)
	path.append("stop")
def back():
	global path
	global i
	if i==1:
		path.append("back")
	a.left(180)
	print path
def left():
	global num
	global i
	global path
	if i==1:
		path.append("left")
	print enter()
	if i==1:
		path.append(num)
	a.left(num)
	num=0
	print path
def right():
	global i
	global num
	global path
	if i==1:
		path.append("right")
	
	print enter()
	if i==1:
		path.append(num)
	a.right(num)
	num=0
	print path
def cir():
	global i
	global num
	global path
	if i==1:
		path.append("cir")
	print enter()
	if i==1:
		path.append(num)
	a.circle(num)
	num=0
	print path
def ope():
	global i
	global path	
	if i==1:
		path.append("ope")
	a.up()
	print path
def close():	
	global i
	global path
	if i==1:
		path.append("close")
	a.down()
	print path
#predefined commands 
#graphics for toplevel
def exe(): 
	i=0
	global var
	global isa
	global var
	global p1
	isa=0
	n=len(path)
	p1=Toplevel()
	q=Button(p1,text="1",bg="sky blue",width=2,height=2,command=p11)
	b=Button(p1,text="2",bg="sky blue",width=20,height=2,command=p2)
	d=Button(p1,text="3",bg="sky blue",width=2,height=2,command=p3)
	e=Button(p1,text="4",bg="sky blue",width=2,height=2,command=p4)
	f=Button(p1,text="5",bg="sky blue",width=20,height=2,command=p5)
	g=Button(p1,text="6",bg="sky blue",width=2,height=2,command=p6)
	r=Button(p1,text="7",bg="sky blue",width=2,height=2,command=p7)
	s=Button(p1,text="8",bg="sky blue",width=20,height=2,command=p8)
	t=Button(p1,text="9",bg="sky blue",width=2,height=2,command=p9)
	h=Button(p1,text="0",bg="sky blue",width=20,height=2,command=p0)
	en=Button(p1,text="entery",bg="sky blue",width=20,height=2,command=ent)
	var = IntVar()
	c = Checkbutton(p1, text="FOR LOOP?",variable=var, command=loop)
	c.grid(row=5,column=1)
	en.grid(row=4,column=1)
	q.grid(row=1, column=0)
	b.grid(row=1, column=1)
	d.grid(row=1, column=2)
	e.grid(row=2, column=0)
	f.grid(row=2, column=1)
	g.grid(row=2, column=2)
	r.grid(row=3, column=0)
	s.grid(row=3, column=1)
	t.grid(row=3, column=2)
	h.grid(row=4, column=1)
	while i<n:
		if path[i]=="stop":
			isa=isa+1
		i=i+1
	isa=isa-1
	ia="you have these many choices",isa
	w = Label(p1,text=ia,font="Times,5,bold")
	w.grid(row=0,column=1)
def help():
	w=Toplevel()
	s=Label(w,text="PYTLE",font="Times,BOLD,U",fg="red").pack()
	s=Label(w,text="What in the world is PYTLE??",font="Times,50,BOLD",fg="black").pack()
	s=Label(w,text="pytle is an turtle/python based software",font="Times,50,BOLD",fg="blue").pack()
	s=Label(w,text="created by me,Rohit Shetty,contact me at roit.shetty@gmail.com",font="Times,50,BOLD",fg="blue").pack()
	s=Label(w,text="WHAT IS TURTLE USEFULL FOR?? ",font="Times,50,BOLD",fg="black").pack()
	s=Label(w,text="PYTLE uses turtle that was developed for a robot named TURTLE ",font="Times,50,BOLD",fg="blue").pack()
	s=Label(w,text="later it was used in Pc's to teach begginers ",font="Times,50,BOLD",fg="blue",).pack()
	s=Label(w,text="about programming,kids,math students and was named LOGO",font="Times,50,BOLD",fg="blue").pack()
	s=Label(w,text="  today LOGO is succesfull in its aim this pytle allows you to graphically",font="Times,50,BOLD",fg="blue").pack()
	s=Label(w,text=" teach logic and concepts to kids and adult alike without worrying about the ",font="Times,50,BOLD",fg="blue").pack()		
	s=Label(w,text="programming concepts however the user is adviced to learn programming",font="Times,50,BOLD",fg="blue").pack()
	s=Label(w,text=" HOW TO USE IT ??",font="Times,50,BOLD",fg="black").pack()
	s=Label(w,text="Enter the number using mouse and pad ",font="Times,50,BOLD",fg="blue").pack()
	s=Label(w,text=" and the corresponding choice for command",font="Times,50,BOLD",fg="blue").pack()
	s=Label(w,text=" HOW TO EXECUTE ONE STEP AGAIN AND AGAIN??",font="Times,50,BOLD",fg="black").pack()
	s=Label(w,text=" First click STOP RECORD and perform the operations,now click on STOP,",font="Times,50,BOLD",fg="black").pack()
	s=Label(w,text=" and click EXECUTE it will display the number of macros recorded..",font="Times,50,BOLD",fg="blue").pack()
	s=Label(w,text="enter the choice and if you want to repeat the task click ",font="Times,50,BOLD",fg="blue").pack()
	s=Label(w,text=" on for loop button and enter your choice....enjoy ",font="Times,50,BOLD",fg="blue").pack()
	z=Button(w,text="Ok Thanks",bg="sky blue",command=(w.destroy)).pack()
#graphics for root
c=Tk()
z=Button(c,text="frwd",bg="pink",command=up)
z.grid(row=0, column=3)
q1=Button(c,text="left",bg="pink",command=left)
q1.grid(row=1, column=3)
w=Button(c,text="right",bg="pink",command=right)
w.grid(row=2, column=3)
x1=Button(c,text="Back",bg="pink",command=back)
x1.grid(row=3, column=3)
o=Button(c,text="open",bg="pink",command=ope)
o.grid(row=4, column=3)
o1=Button(c,text="close",bg="pink",command=close)
o1.grid(row=5, column=3)
record=Button(c,text="record",bg="red",command=rec)
record.grid(row=5, column=0)
stop=Button(c,text="stop",bg="red",command=stop)
stop.grid(row=5,column=2)
exe=Button(c,text="execute",bg="blue",fg="red",command=exe)
exe.grid(row=6,column=1)
q=Button(c,text="1",bg="sky blue",width=2,height=2,command=d1)
b=Button(c,text="2",bg="sky blue",width=2,height=2,command=d2)
d=Button(c,text="3",bg="sky blue",width=2,height=2,command=d3)
e=Button(c,text="4",bg="sky blue",width=2,height=2,command=d4)
f=Button(c,text="5",bg="sky blue",width=2,height=2,command=d5)
g=Button(c,text="6",bg="sky blue",width=2,height=2,command=d6)
r=Button(c,text="7",bg="sky blue",width=2,height=2,command=d7)
s=Button(c,text="8",bg="sky blue",width=2,height=2,command=d8)
t=Button(c,text="9",bg="sky blue",width=2,height=2,command=d9)
h=Button(c,text="0",bg="sky blue",width=2,height=2,command=d0)
cir=Button(c,text="Circle",bg="pink",command=cir)
help=Button(c,text="HELP",bg="red",command=help).grid(row=7,column=3)
exit=Button(c,text="EXIT",bg="red",command=(c.destroy)).grid(row=8,column=3)
q.grid(row=0, column=0)
b.grid(row=0, column=1)
d.grid(row=0, column=2)
e.grid(row=1, column=0)
f.grid(row=1, column=1)
g.grid(row=1, column=2)
r.grid(row=2, column=0)
s.grid(row=2, column=1)
t.grid(row=2, column=2)
h.grid(row=3, column=1)
cir.grid(row=6, column=3)
c.mainloop()
#end---
