import sqlite3 as sq
from tkinter import *
from tkinter import messagebox as msg
import os 
from tkinter.filedialog import askopenfilename
import boto3
import botocore

conn=sq.connect('picture1.db')
conn.execute('create table if not exists picture(Id Auto increment INTEGER,picture BLOB,type Text,filename text,notice text)')
conn.commit
'''def onclick(frame,root,lb,k):
        fra=Frame(root,width=1300,height=1000)
        fra.place(x=0,y=0)
        #num=v.get()[4]
        #num1=int(num)
        #print(num1)
        print(lb)
        conn=sq.connect('picture1.db')
        cos=conn.execute('Select notice from PICTURE where ID=%s'%k)
        fra.config(bg='#FEEBF7')
        lb3=Label(fra,text='Publish a notice.....',bg='#FEEBF7',font=('times',39,'italic'))
        lb3.place(x=230,y=30)
        
        for c in cos:
            da= c[0]
        t1=Text(fra,font=('times',17,'italic'),width=70,height=20)
        t1.place(x=300,y=100)
        t1.insert(END,da)
        b1=Button(fra,text='Upload',width=10,bd=10,command=lambda:data(conn,t1,name),font=('times',17,'italic'))
        b1.place(x=300,y=650)
        b3=Button(fra,text='Upload with image',bd=10,command=lambda:data_img(conn,t1,name),font=('times',17,'italic'))
        b3.place(x=550,y=650)
        b2=Button(fra,text='Back',width=10,bd=10,command=lambda:notice(frame,root),font=('times',17,'italic'))
        b2.place(x=850,y=650)
        fra.mainloop()'''

def notice(frame,root):
    frame.destroy()
    frame3=Frame(root,width=1300,bg='#FEEBF7',height=1000)
    frame3.place(x=0,y=0)
    lb=Label(frame3,text='Welcome to notice board.....',fg='brown',bg='#FEEBF7',font=('times',59,'italic'))
    lb.place(x=230,y=30)
    lb1=Label(frame3,text='  S No. ',font=('times',21,'italic'),bg='brown',fg='#FEEBF7')
    lb1.place(x=70,y=170)
    lb2=Label(frame3,text='      Published Notice...     ',font=('times',21,'italic'),bg='brown',fg='white')
    lb2.place(x=320,y=170)
    lb3=Label(frame3,text='  Image  ',font=('times',21,'italic'),bg='brown',fg='white')
    lb3.place(x=850,y=170)
    b3=Button(frame3,text=' Back ',bd=10,command=lambda:nextmain(frame,root),font=('times',17,'italic'))
    b3.place(x=850,y=650)
    conn=sq.connect('picture1.db')
    cur=conn.execute('Select ID,notice,picture from PICTURE')
    #cos=conn.execute('Select FILE_NAME from PICTURE')
    j=0
    lb7=[0,0,0,0,0,0,0]
    for k,i in enumerate(cur):
        #l.append(i[0])
        dat=i[1]
        no=i[0]
        pic=i[2]
        #print(i[2])
        print(i)
        
        lb=Label(frame3,text='%d'%k,fg='black',bg='#FEEBF7',font=('times',19,'italic'))
        lb.place(x=80,y=250+(j*70))
        #fp=open('%d'%i+'.txt')
        #data=fp.read(25)
        lb=Label(frame3,text='%s'%dat[0:27]+'.......',fg='black',bg='#FEEBF7',font=('times',19,'italic'))
        lb.place(x=325,y=250+(j*70))
        if i[2] :
            img=PhotoImage(file='mark.png')
            lb=Label(frame3,image=img,bg='#FEEBF7')
            lb.image=img
            lb.place(x=890,y=250+(j*70))
        else:
            lb=Label(frame3,text='    ',bg='#FEEBF7')
            lb.place(x=890,y=250+(j*70))
        
        #v=StringVar()
        #v.set('read'+str(j+1))
        #print(v.get())
        #lb7[k]=Button(frame3,textvariable=v,command=lambda:onclick(frame,root,lb7[k],k),font=('times',13,'italic','underline'),bg='#FEEBF7',fg='black')
        #lb7[k].place(x=650,y=250+(j*70))
        #lb7[k].bind('<Button-1>',onclick)
        j=j+1
        
                                                            
def insert_picture(conn,t1):
    txt=t1.get('1.0',END)
    picture_file=askopenfilename()
    with open(picture_file, 'rb') as input_file:
        ablob = input_file.read()
        base=os.path.basename(picture_file)
        afile, ext = os.path.splitext(base)
        sql = '''INSERT INTO PICTURE
        (PICTURE, TYPE, FILE_NAME,notice)
        VALUES(?, ?, ?, ?);'''
        conn.execute(sql,[sq.Binary(ablob), ext, afile, txt]) 
        conn.commit()
    msg.showinfo('sucessfully send...')
        
def send_data(connt,t1):
    txt=t1.get('1.0',END)
    conn=sq.connect('picture1.db')
    conn.execute('Insert into PICTURE(notice) values(?)',[txt])
    conn.commit()
    msg.showinfo('Title','Sucessfully Send')

def disp(frame,root):
    frame.destroy()
    frame1=Frame(root,height=1000,width=1300)
    frame1.place(x=0,y=0)
    frame1.config(bg='#FEEBF7')
    conn=sq.connect('picture1.db')
    lb3=Label(frame1,text='Publish a notice.....',bg='#FEEBF7',font=('times',39,'italic'))
    lb3.place(x=230,y=30)
    t1=Text(frame1,font=('times',17,'italic'),width=70,height=20)
    t1.place(x=300,y=100)
    b1=Button(frame1,text='upload',width=10,bd=10,command=lambda:send_data(conn,t1),font=('times',17,'italic'))
    b1.place(x=100,y=650)
    b2=Button(frame1,text='upload with image',bd=10,command=lambda:insert_picture(conn,t1),font=('times',17,'italic'))
    b2.place(x=430,y=650)
    b3=Button(frame1,text=' Back ',bd=10,command=lambda:nextmain(frame,root),font=('times',17,'italic'))
    b3.place(x=850,y=650)
    frame1.mainloop()

def Quit(frame,root):
    frame.destroy()
    root.destroy()

def cot(var):
        ts=var[0]
        print(var[0])
        print(type(var))
        conn=sq.connect('picture1.db')
        conn.execute('create table if not exists timer(time TEXT)')
        conn.execute('Insert into timer(time) values(?)',ts)
        msg.showinfo('info','Timer set for %s '%var)
        conn.commit()

def nextmain(frame,root):
    frame.destroy()
    frame2=Frame(root,width=1300,height=1000)
    frame2.place(x=0,y=0)
    frame2.config(bg='#FEEBF7')
    lb1=Label(frame2,text='Welcome to notice board.....',bg='#FEEBF7',fg='brown',font=('times',59,'italic'))
    lb1.place(x=230,y=25)
    img=PhotoImage(file='wat.png')
    lb=Label(frame2,image=img,bg='#FEEBF7')
    lb.image=img
    lb.place(x=727,y=200)
    var=StringVar(frame2)
    var.set('Select Timer')
    op=OptionMenu(frame2,var,'1 min','2 min','3 min','4 min','5 min')
    op.config(width=21,height=2,bg='#FEEBF7',font=('times',23,'bold','italic'))
    op.place(x=120,y=150)
    bo=Button(frame2,text='ok',command=lambda:cot(var.get()),font=('times',15,'bold'),fg='brown')
    bo.place(x=550,y=193)
    b1=Button(frame2,text='Select Notice',font=('times',23,'bold','italic'),command=lambda:notice(frame,root),fg='brown',width=20,bd=10)
    b1.place(x=110,y=284)
    b2=Button(frame2,text='New Notice',font=('times',23,'bold','italic'),command=lambda:disp(frame,root),fg='brown',width=20,bd=10)
    b2.place(x=110,y=430)
    b5=Button(frame2,text='Emergency Notice',command=lambda:emergency(frame,root),font=('times',23,'bold','italic'),fg='brown',width=20,bd=10)
    b5.place(x=110,y=570)
    b3=Button(frame2,text='Quit',width=10,bd=10,command=lambda:Quit(frame,root),font=('times',17,'italic'))
    b3.place(x=850,y=650)
    b4=Button(frame2,text='Back',width=10,bd=10,command=lambda:main(root),font=('times',17,'italic'))
    b4.place(x=670,y=650)
    frame2.mainloop()

def emer_data(conn,tim,t1):
    conn.execute('insert into emerg(time,notice) values(?,?);',[tim,t1])
    conn.commit()
    msg.showinfo('Title','sucessfully send...')

def emer_data_img(conn,t1,tim):    
    picture_file=askopenfilename()
    with open(picture_file, 'rb') as input_file:
        ablob = input_file.read()
        base=os.path.basename(picture_file)
        afile, ext = os.path.splitext(base)
        sql = '''INSERT INTO emerg
        (PICTURE, TYPE, FILE_NAME, notice,time)
        VALUES(?, ?, ?, ?, ?);'''
        conn.execute(sql,[sq.Binary(ablob), ext, afile, t1, tim]) 
        conn.commit()
    msg.showinfo('TITLE','sucessfully send...')

def emergency(frame,root):
    frame.destroy()
    frame4=Frame(root,height=1000,width=1300)
    frame4.place(x=0,y=0)
    frame4.config(bg='#FEEBF7')
    lb3=Label(frame4,text='Publish a notice.....',bg='#FEEBF7',font=('times',39,'italic'))
    lb3.place(x=230,y=30)
    t1=Text(frame4,font=('times',17,'italic'),width=70,height=20)
    t1.place(x=300,y=100)
    conn=sq.connect('picture1.db')
    conn.execute('create table if not exists emerg(time TEXT,notice Text,PICTURE BLOB,TYPE INTVAR,FILE_NAME TEXT)')
    b1=Button(frame4,text='upload',width=10,bd=10,command=lambda:emer_data(conn,var.get(),t1.get("1.0",END)),font=('times',17,'italic'))
    b1.place(x=100,y=650)
    var=StringVar()
    var.set('1 min')
    op=OptionMenu(frame4,var,'2 min','3 min','4 min','5 min','15 min','30 min','1 hour','2 hour','3 hour','1 day')
    op.place(x=1070,y=100)
    b2=Button(frame4,text='upload with image',bd=10,command=lambda:emer_data_img(conn,t1.get("1.0",END),var.get()),font=('times',17,'italic'))
    b2.place(x=430,y=650)
    b3=Button(frame4,text=' Back ',bd=10,command=lambda:nextmain(frame,root),font=('times',17,'italic'))
    b3.place(x=850,y=650)
    frame4.mainloop()    
    
def main(root):
    frame=Frame(root,height=1000,width=1300)
    frame.place(x=0,y=0)
    frame.config(bg='#FEEBF7')
    img=PhotoImage(file='tab.png')
    lb=Label(frame,image=img,bg='#FEEBF7')
    lb.place(x=870,y=330)
    lb1=Label(frame,text='Welcome to notice board.....',bg='#FEEBF7',fg='brown',font=('times',59,'italic'))
    lb1.place(x=230,y=30)
    lb2=Label(frame,text='''Welcome, This is e-Notice board belongs
                            to 'XYZ University'. This will Provide you the
                            feature of publishing the e-notice for any one belongs
                            to this campus only.Your message is directly published on
                            second panel of this notice board which can be viewed by others
                            concerned one's.
                            THANK YOU FOR USING THIS.....''',font=('Times',22,'italic'),borderwidth=20,fg='brown',bg='#FEEBF7')
    lb2.place(x=10,y=200)
    b1=Button(frame,text='Quit',width=10,bd=10,command=lambda:Quit(frame,root),font=('times',17,'italic'))
    b1.place(x=690,y=650)
    b2=Button(frame,text='Next >>',width=10,bd=10,command=lambda:nextmain(frame,root),font=('times',17,'italic'))
    b2.place(x=290,y=650)
    frame.mainloop()
    
    
root=Tk()
root.geometry('1300x1000')
root.title('Electronic notice board')
#root.withdraw()
main(root)

msg.showwarning("Don't close","Don't close still Updating...")
aws_access_key_ID='AKIAJTCHQKXGRKNNQQOA'    
aws_secret_access_key='a9DEQshwAlHVRwMoZnZHsttCnlZY8i5w+b/r4ZFl'   
bucketName = 'kajal-ankita'#'ashish2510'# #"Your S3 BucketName"
FileName = 'F:\\eboard\\picture1.db'#'E:\\F\\Python Codes\\My Codes\\Final_IOT.py'      #"Original Name and type of the file you want to upload into s3"
outPutName = 'picture1.db'   #"Output file name(The name you want to give to the file after we upload to s3)"

s3 = boto3.client('s3',aws_access_key_id=aws_access_key_ID,
                      aws_secret_access_key=aws_secret_access_key)
s3.upload_file(FileName,bucketName,outPutName)

print(FileName,'File Uploaded successfullly!!!!!')
msg.showinfo('DONE','Sucessfully Updated')

