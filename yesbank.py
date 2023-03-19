from tkinter import *
import pymysql
from tkinter import messagebox
from PIL import ImageTk,Image
def search():
    acn=int(t5.get().lower())
    ab=pymysql.connect(host='localhost',user='root',password='',db='bank')
    cursor=ab.cursor()
    stmt=("SELECT * FROM acc WHERE acc_no="+ str(acn)+"")
    a=cursor.execute(stmt)
    if a==1:
        row=cursor.fetchone()
        t1.delete(0,"end")
        t2.delete(0,"end")
        t3.delete(0,"end")
        t1.insert(0,row[0])
        t2.insert(0,row[1])
        t3.insert(0,row[2])
        messagebox.showinfo("search","record found successfully")
    else:
        t1.delete(0,"end")
        t2.delete(0,"end")
        t3.delete(0,"end")
        messagebox.showinfo("search","record not found")

    cursor.close()
    ab.commit()
    ab.close()



def adddata():    
    enm=str(t1.get().lower())
    accno=int(t2.get().lower())
    sal=int(t3.get().lower())
    ab=pymysql.connect(host="localhost",user='root',password='',db='bank')
    cursor=ab.cursor()
    stmt=("insert into acc(acc_no,name,bal)VALUES("+str(accno)+",'"+enm+"',"+str(sal)+")")
    check_acc_no=f"select acc_no from acc"
    messagebox.showinfo("SUCCESSFUL","Record inserted successfully")
    cursor.execute(stmt)
    cursor.close()
    ab.commit()
    ab.close()

def clear():
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)
    t5.delete(0,END)

#def resize_image(e):
     #image =Image.open(r"C:\Users\shreyas phansalkar\Dropbox\PC\Desktop\python excel\database\federal.jpg")
     #resized=image.resize((e.width,e.height),Image.ANTIALIAS)
     #image2=ImageTk.photoImage(resized)
     #canvas.create_image(200,200,image=image2,anchor='n')

def delete():
    accno=int(t2.get())
    db=pymysql.connect(host="localhost",user="root",password="",db='bank')
    cursor=db.cursor()
    stmt=(" delete from acc where acc_no="+str(accno)+"")
    cursor.execute(stmt)
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)
    cursor.close()
    db.commit()
    messagebox.showinfo("delete box","RECORD DELETED SUCCESSFULLY!")


def update():
    enm=str(t1.get().lower())
    accno=int(t2.get().lower())
    sal=int(t3.get().lower())
    db=pymysql.connect(host="localhost",user="root",password="",db='bank')
    cursor=db.cursor()
    stmt=("update acc set name='"+enm+"',acc_no="+str(accno)+",bal="+str(sal)+" where acc_no="+str(accno)+"")
    cursor.execute(stmt)
    cursor.close()
    db.commit()
    messagebox.showinfo("update","record updated successfully")
    




root=Tk()
root.title("YES BANK LTD")
root.resizable(0,0)
bg=ImageTk.PhotoImage(Image.open(r"C:\Users\shreyas phansalkar\Dropbox\PC\Desktop\python excel\database\yesbank.jpg"))
canvas=Canvas(root,width=200,height=200)
canvas.pack(fill="both",expand=True)
canvas.create_image(0,0,image=bg,anchor='nw')
root.geometry("900x1000")
l6=Label(root,text="DATABASE FOR YES BANK")
l6.place(x=380,y=0)
l1=Label(root,text="ENTER ACCOUNT NAME",bg="white",fg="black")
l1.place(x=300,y=40)
t1=Entry(root,width=20)
t1.place(x=450,y=40)
l2=Label(root,text="ENTER ACCOUNT NUMBER",bg="white",fg="black")
l2.place(x=300,y=80)
t2=Entry(root,width=20)
t2.place(x=450,y=80)
l3=Label(root,text="ENTER BALANCE",bg="white",fg="black")
l3.place(x=300,y=120)
t3=Entry(root,width=20)
t3.place(x=450,y=120)
b1=Button(root,text="INSERT",width=10,command=adddata)
b1.place(x=450,y=160)
b2=Button(root,text="SEARCH",width=10,command=search)
b2.place(x=300,y=200)
t5=Entry(root,width=20)
t5.place(x=450,y=200)
b3=Button(root,text="CLEAR",width=10,command=clear)
b3.place(x=450,y=240)
b4=Button(root,text="DELETE",width=10,command=delete)
b4.place(x=300,y=160)
b5=Button(root,text="UPDATE",width=10,command=update)
b5.place(x=600,y=160)
l7=Label(root,text="MADE WITH ❤ BY SHREYAS",font=("Modern",20))
l7.pack()
root.mainloop()

