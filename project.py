#IMPORTS
from tkinter import *
from tkcalendar import*
import tkinter.messagebox as msg

import mysql.connector as form_list
from PIL import ImageTk, Image
import smtplib 
import random 

 

#MAIN_WINDOW_OPEN  
main_window=Tk()

#GLOBAL_DEFINED
global ID 
global firstname            
global lastname
global dateofbirth
global email
global phonenumber
global address
global aboutself 
global qualification
global verification
global login_ask_entry1
global login_ask_entry2
global login_otp_entry 
global OTP

#GET_REGISTERED_NAMES_AND_DETAILS_FROM_FORM_TABLE
mycon=form_list.connect(host='localhost',user='root',passwd='soumyajit',database='project') 
mycursor=mycon.cursor()
form_all_value="SELECT * FROM form"
mycursor.execute(form_all_value)
form_value_get=mycursor.fetchall()

mycon=form_list.connect(host='localhost',user='root',passwd='soumyajit',database='project') 
mycursor=mycon.cursor()
employ_all_get="SELECT * FROM employ"
mycursor.execute(employ_all_get)
employ_value_get=mycursor.fetchall()
    
#NEW_USER_DEFINED
def new():
    
    #REGISTRATION_CONFIGURATION
    registration_window=Toplevel()
    registration_window.geometry('709x765')
    registration_window.minsize(709,756)
    registration_window.maxsize(709,765)
    registration_window.title('REGISTRATION')
    
    
    #REGISTRATION_SCROLLBAR
    registration_scrollbar=Scrollbar(registration_window)
    registration_scrollbar.pack(fill='y',side='right')
    
    
    #REGISTRATION_FRAME
    registration_frame=Frame(registration_window,bg='sky blue')
    registration_frame.pack(fill='y') 
    
    #REGISTRATION_BANNER
    registration_banner1=Image.open('apply.png')
    registration_banner1_resized=registration_banner1.resize((400,100),Image.ANTIALIAS)
    registration_banner1_new=ImageTk.PhotoImage(registration_banner1_resized)
    
    #REGISTRATION_LABEL
    registration_label=Label(registration_frame,image=registration_banner1_new,bd=4,relief='ridge')
    registration_label.pack(pady=20)
    
    #REGISTRATION_IMAGE
    registration_image=Image.open('main_image1.png')
    registration_image_resized=registration_image.resize((690,300),Image.ANTIALIAS)
    registration_image_new=ImageTk.PhotoImage(registration_image_resized)
    
    #REGISTRATION_TEXT
    registration_text=Text(registration_frame,yscrollcommand=registration_scrollbar.set,height=30,width=85,bd=4,relief='ridge')
    registration_text.pack(pady=15)
    
    registration_scrollbar.configure(command=registration_text.yview)
    
    #REGISTRATION_AGGREMENT_TEXT_FILE
    with open('terms.txt','rb') as f:
         aggrement=f.read()
    
    #REGISTRATION_ADD_TEXT_AND_IMAGE
    registration_text.image_create(END, image=registration_image_new)
    registration_text.insert(END, aggrement)
    
    #REGISTRATION_ICON 
    registration_icon=PhotoImage(file='registration.png')
    registration_window.iconphoto(FALSE,registration_icon)
    
    
    def register():
        
        registration_statusbar_value.set('Working on it....')
        registration_statusbar.update()
        import time 
        time.sleep(1)
        registration_statusbar_value.set('Ready')
        
        
        def submit():
            
            ID=0    
            firstname=entry_firstname.get() 
            lastname=entry_lastname.get() 
            dateofbirth=dob.get()
            email=entry_email.get()
            phonenumber=entry_phone.get()
            address=entry_address.get() 
            aboutself=entry_aboutself.get()
            qualification=radvar.get()
            verification=check_button.get()
            
            #SUBMIT_STATUS_CONDITION
            form_statusbar_value.set('Busy...')
            form_statusbar.update()
            import time
            time.sleep(0.5)
            
            
            #SUBMIT_CONDITION
            if (firstname=='' or lastname=='' or dateofbirth=='' or '@' not in email   or phonenumber==91 or address=='' or verification==0):
                form_statusbar_value.set('Submission Fail  !! ')
                form_statusbar.update()
                time.sleep(1)
                form_statusbar_value.set('Ready')
            else:
                form_statusbar_value.set('Submitted Sucessfully')
                form_statusbar.update()
                time.sleep(1)
                form_statusbar_value.set('Ready')
        
            
            if (firstname==''):
                msg.showerror('Insert Status','First Name Required!!')
            elif(lastname==''):
                msg.showerror('Insert Status','Last Name Required!!')
            elif (dateofbirth==''):
                msg.showerror('Insert Status','Dob Required!!')
            elif ('@' not in email):
                msg.showerror('Insert Status','Enail Required!!')
            elif (phonenumber==91):
                msg.showerror('Insert Status','Phone Number Required!!')
            elif (address==''):
                msg.showerror('Insert Status','Address Required!!')
            elif (verification==0):
                msg.showerror('Insert Status','Verify!!')
            else:
                mycon=form_list.connect(host='localhost',user='root',passwd='soumyajit',database='project')
                mycursor=mycon.cursor()
                val=(firstname,lastname,dateofbirth,email,phonenumber,address,aboutself,qualification,verification)
                sql="INSERT INTO form  VALUES({},'{}','{}','{}','{}','{}','{}','{}','{}',{})".format(ID,firstname,lastname,dateofbirth,email,phonenumber,address,aboutself,qualification,verification)
                mycursor.execute(sql)
                mycon.commit()
            
            
                #DESELECT ENTRIES
                ef1.delete(0,'end')
                ef2.delete(0,'end')
                ef3.delete(0,'end')
                ef4.delete(2,'end')
                ef5.delete(0,'end') 
                ef6.delete(0,'end')
                dob.delete(0,'end')
                radvar.__del__()
                chkbf1.deselect() 
                sender_mail='miniproject.storm@gmail.com'
                sender_password='miniproject'
                reciver_mail=email
                message='Subject: Registration Status \n\nWelcome To TechBreeze'+'  '+ firstname + ' ' + lastname +'. '+ 'You Have Sucessfully Registered Into TechBreeze.'+''
                registration_status=smtplib.SMTP('smtp.gmail.com',587)
                registration_status.starttls()
                registration_status.login(sender_mail,sender_password)
                registration_status.sendmail(sender_mail,reciver_mail,message)
                registration_status.quit()
                msg.showinfo('Status','Submitted Sucessfully!!')
                form.destroy()
                registration_window.destroy()
                
                
                    
            
        #FORM_CONFIGURATION    
        form=Toplevel()
        form.geometry('600x750')
        form.title('FORM')
        form.minsize(600,750)
        form.maxsize(600,750)
        form.configure(bg='light yellow')
        
        #FORM_LABEL
        form_label1=Label(form,text= 'Registration Form',font='helvatica 32 bold',fg='red',bg='light yellow')
        form_label1.place(anchor='nw',x=15,y=5)
        form_label2=Label(form,text='Please fill in your details for registration',font='helvatica 16',bg='light yellow')
        form_label2.place(anchor='nw',x=15,y=58)
        
        lf1=Label(form,text='  First Name*:  ',font=6,relief='groove',bg='yellow')
        lf1.place(x=20,y=105)
        lf2=Label(form,text='  Last Name*:  ',font=6,relief='groove',bg='yellow')
        lf2.place(x=20,y=150)
        lf3=Label(form,text='  DOB*:  ',font=6,relief='groove',bg='yellow')
        lf3.place(x=20,y=195)
        lf4=Label(form,text='  Gmail*:  ',font=6,relief='groove',bg='yellow') 
        lf4.place(x=20,y=240)
        lf5=Label(form,text='  Phone Number*:  ',font=6,relief='groove',bg='yellow')
        lf5.place(x=20,y=285)
        lf6=Label(form,text='  Address*:  ',font=6,relief='groove',bg='yellow')
        lf6.place(x=20,y=330)
        lf7=Label(form,text='  About Self:  ',font=6,relief='groove',bg='yellow')
        lf7.place(x=20,y=375)
        lf8=Label(form,text='  Qualification*:  ',font=6,relief='groove',bg='yellow')
        lf8.place(x=20,y=420)
        lf9=Label(form,text='  Verification*:  ',font=6,relief='groove',bg='yellow')
        lf9.place(x=20,y=610)
        
        #FORM_VARIABLE_VALUE
        entry_firstname=StringVar()
        entry_lastname=StringVar()
        dob=StringVar()
        entry_email=StringVar()
        entry_phone=IntVar(value=91)
        entry_address=StringVar()
        entry_aboutself=StringVar()
        check_button=IntVar()
        radvar=StringVar(0)
        radvar.set(0)
        
        #FORM_ENTRY
        ef1=Entry(form,relief='groove',font=6,textvariable=entry_firstname,bg='white')
        ef1.place(x=280,y=105)
        ef2=Entry(form,relief='groove',font=6,textvariable=entry_lastname,bg='white')
        ef2.place(x=280,y=150)
       # dob=DateEntry(form,relief='groove',font=6,width=18,year=2020,month=5,day=12,selectmode='day',textvariable=dob,date_pattern='dd/mm/yyyy',bg='white')
        dob=Entry(form,relief='groove',font=6,textvariable=dob,bg='white')
        dob.place(x=280,y=195)
        ef3=Entry(form,relief='groove',font=6,textvariable=entry_email,bg='white')
        ef3.place(x=280,y=240)
        ef4=Entry(form,relief='groove',font=6,textvariable=entry_phone,bg='white')
        ef4.place(x=280,y=285)
        ef5=Entry(form,relief='groove',font=6,textvariable=entry_address,bg='white')
        ef5.place(x=280,y=330)
        ef6=Entry(form,relief='groove',font=6,textvariable=entry_aboutself,bg='white') 
        ef6.place(x=280,y=375) 
    
        #FORM_RADIOBUTTON
        rad=Radiobutton(form,text='  Diploma in Software Engineering  ',variable=radvar,value='Diploma in Software Engineering',bg='white').place(x=280,y=420)
        rad=Radiobutton(form,text='  Diploma in IT  ',variable=radvar,value='Diploma in IT',bg='white').place(x=280,y=440)
        rad=Radiobutton(form,text='  B.E/B.Tech in Software Engineering  ',variable=radvar,value='B.E/B.Tech in Software Engineering',bg='white').place(x=280,y=460)
        rad=Radiobutton(form,text='  B.E/B.Tech in IT  ',variable=radvar,value='B.E/B.Tech in IT',bg='white').place(x=280,y=480)
        rad=Radiobutton(form,text='  BCA  ',variable=radvar,value='BCA',bg='white').place(x=280,y=500)
        rad=Radiobutton(form,text='  M.E/M.Tech in Software Engineering  ',variable=radvar,value='M.E/M.Tech in Software Engineering',bg='white').place(x=280,y=520)
        rad=Radiobutton(form,text='  M.E/M.Tech in IT  ',variable=radvar,value='M.E/M.Tech in IT',bg='white').place(x=280,y=540)
        rad=Radiobutton(form,text='  MCA  ',variable=radvar,value='MCA',bg='white').place(x=280,y=560)
        rad=Radiobutton(form,text='  Advance Diploma in Software Engineering  ',variable=radvar,value='Advance Diploma in Software Engineering',bg='white').place(x=280,y=580)
    
        #FORM_CHECKBUTTON
        chkbf1=Checkbutton(form,relief='groove',text='  I Am Not A Robot  ',font=6,variable=check_button,bg='white')
        chkbf1.place(x=280,y=610)
    
        #FORM_SUBMIT_BUTTON
        bf1=Button(form,text='  SUBMIT  ',command=submit,font=14,bg='yellow',fg='black') 
        bf1.place(x=155,y=675)
    
        #FORM_BUTTON_HOVER_ENTER_LEAVE
        def bf1_hover_enter(event):
            bf1['bg']='mediumblue'
            bf1['fg']='red'
        def bf1_hover_leave(event):
            bf1['bg']='yellow'
            bf1['fg']='black'
    
        #FORM_BUTTON_HOVER
        bf1.bind('<Enter>',bf1_hover_enter)
        bf1.bind('<Leave>',bf1_hover_leave)
    
        #FORM_STATUS_BAR
        form_statusbar_value=StringVar()
        form_statusbar_value.set('Ready') 
    
        form_statusbar=Label(form,textvariable=form_statusbar_value,anchor='w',bd=1,relief='sunken',fg='black',bg='white')  
        form_statusbar.pack(side='bottom',ipady=2,fill='x')
    
        
        #FORM_ICON
        photo_form=PhotoImage(file='form_icon.png')
        form.iconphoto(FALSE,photo_form)
        
        
        form.mainloop()
     
        
    #REGISTRATION_BUTTON
    registration_button=Button(registration_frame,text='  Click Here To Register  ',command=register,bg='black',fg='red',font='helvatica 16 bold',relief='ridge',bd=3,highlightcolor='red')
    registration_button.pack(pady=15)
    
    #REGISTRATION_BUTTON_HOVER_ENTER_LEAVE
    def registration_button_enter(event):
        registration_button['bg']='yellow'
        registration_button['fg']='red'
        registration_statusbar_value.set('Busy...')
    def registration_button_leave(event):
        registration_button['bg']='black'
        registration_button['fg']='white'
        registration_statusbar_value.set('Ready')
     
    #REGISTRATION_BUTTON_HOVER
    registration_button.bind('<Enter>',registration_button_enter)
    registration_button.bind('<Leave>',registration_button_leave)  
    
    #REGISTRATION_STATUSBAR
    registration_statusbar_value=StringVar()
    registration_statusbar_value.set('Ready')
    
    registration_statusbar=Label(registration_window,textvariable=registration_statusbar_value,bg='white',fg='black',bd=1,relief='sunken',anchor='w')
    registration_statusbar.pack(ipady=2,fill='x',side='bottom')
    
    registration_window.mainloop()

 
#LOGIN_DEFINED
def loginask():
    
    def generateotp():
        
        if login_ask_entry1.get() == '': 
            msg.showerror('Insert Status','Gmail Required !!')
        elif '@' not in login_ask_entry1.get():
            msg.showerror('Insert Status','Please Enter A Valid Gmail Id')
        else:
            #LOGIN_OTP_ASK_PACK
            login_otp_label.pack(pady=3)
            login_otp_entry.pack(pady=3)
            login_ask_button.pack(pady=3)
         
            #OTP_FOR_LOGIN
            otp_login='miniproject.storm@gmail.com'
            otp_password='miniproject' 
            otp_message='Subject: OTP \n\nYour one time password for logging into Tech Breeze is'+ ' ' +''+ str(OTP) +''
            otp_server=smtplib.SMTP('smtp.gmail.com',587)
            otp_server.starttls() 
            otp_server.login(otp_login,otp_password) 
            otp_server.sendmail(otp_login,login_ask_entry1.get(),otp_message) 
            otp_server.quit() 
            msg.showinfo('OTP Status','OTP Has Been Sent To Your Registered Mail') 

    def login():
         
        otp_got=int(login_otp_entry.get())
        #LOGIN_OTP_CONDITION
        if (OTP) == (otp_got):
           #LOGIN_EMAIL_SUCESSFUL
            
            from time import time,ctime
            t=time() 
            c=ctime(t)
            gmail_login='techbreeze.apply.job@gmail.com'
            gmail_password='techbreeze12'
            gmail_message='Subject: Login Status \n\nYou Have Sucessfully Logged Into Tech Breeze at'+ ' ' + '' +  c  + ''
            reciver_mail=(login_ask_entry1.get())
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls() 
            server.login(gmail_login, gmail_password)
            server.sendmail(gmail_login,reciver_mail,gmail_message) 
            server.quit()
            
            #WORKSPACE_WINDOW_CONFUGARATION
            workspace_window=Toplevel()
            workspace_window.title('WORK SPACE')
            workspace_window.geometry('30x670')
            workspace_window.minsize(930,670)
            workspace_window.maxsize(950,700)
            workspace_window.configure(bg='black')
            login_ask_window.destroy()
            
            
            #CLOCK
            def clock():
                import time
                hour=time.strftime('%I')
                minute=time.strftime('%M')
                seconds=time.strftime('%S')
                day=time.strftime('%A')
                am_pm=time.strftime('%p')
                date=time.strftime('%d') 
                month=time.strftime('%m')
                year=time.strftime('%y')
                
            
                workspace_clock_label.after(1000,clock)
                workspace_clock_label.config(text=hour + ':' + minute + ':' + seconds + '' + '' + am_pm  + '')
                workspace_day_label.config(text=day)
                workspace_date_label.config(text=date + ',' + month + ',' + year + '')
            
            #WORKSPACE_FRAME
            workspace_frame=Frame(workspace_window,bg='black')
            workspace_frame.pack(fill='x')
            
            #WORKING_LABEL
            working_label=Label(workspace_frame,bg='sky blue')
            working_label.pack(side='left',anchor='nw',fill=BOTH,padx=2,pady=2)
            
            #LEAVE_LABEL
            leave_label=Label(workspace_frame,bg='red')
            leave_label.pack(side='right',anchor='ne',fill=BOTH,padx=2,pady=2)
            
            #TIME_LABEL
            time_label=Label(workspace_window,bg='light green')
            time_label.pack(fill='x',pady=2,padx=5)
            
            #WORKSPACE_SCROLLBAR
            workspace_scrollbar=Scrollbar(working_label)
            workspace_scrollbar.pack(fill='y',side='right')
            
            #WORKSPACE_LABEL_TEXT_BUTTON_ENTRY
            workspace_label1=Label(working_label,text='WORKING AREA',font=18,bg='sky blue',fg='red')
            workspace_label1.pack(pady=20,padx=10)
        
            workspace_label2=Label(working_label,text='Enter Your Name:',bg='sky blue')
            workspace_label2.pack(pady=5,padx=10)
        
            workspace_entry1=Entry(working_label)
            workspace_entry1.pack(pady=5,padx=10)
            
            workspace_text=Text(working_label,yscrollcommand=workspace_scrollbar.set,relief='ridge')
            workspace_text.pack(pady=5,padx=10)
            workspace_scrollbar.configure(command=workspace_text.yview)
            
            attendence=IntVar()
            
            workspace_checkbutton=Checkbutton(working_label,text='Attendence',variable=attendence,bg='sky blue')  
            workspace_checkbutton.pack(pady=5,padx=10)  
            
            from time import time,ctime
            time=time()
            employ_attendence_time=ctime(time)
            
            #TO_SUBMIT_TO_BOSS
            ID=0
            def submittoboss():
                global employ_name
                employ_name=workspace_entry1.get()
                global employ_work
                employ_work=workspace_text.get('1.0',END)
                global employ_attendence_got
                employ_attendence_got=attendence.get()
                if (workspace_entry1.get()=='') :
                    msg.showerror('Insert Status','Please Enter Your Name')
                elif (employ_attendence_got==0):
                    msg.showerror('Insert Status','Attendence Compulsary')
                else:
                    mycon=form_list.connect(host='localhost',user='root',passwd='soumyajit',database='project')
                    mycursor=mycon.cursor()
                    employ_val=(employ_name,employ_work)
                    employ_submit="INSERT INTO employ VALUES({},'{}','{}',{},'{}')".format(ID,employ_name,employ_work,employ_attendence_got,employ_attendence_time)
                    mycursor.execute(employ_submit)
                    mycon.commit()
                    msg.showinfo('Insert Status','Submitted Sufessfully')
                    workspace_entry1.delete(0,END)
                    workspace_text.delete('1.0',END)
                    workspace_checkbutton.deselect() 
                   
            #WORKSPACE_WORK_BUTTON
            workspace_button=Button(working_label,text='  SUBMIT  ',bg='yellow',fg='blue',command=submittoboss) 
            workspace_button.pack(pady=8,padx=10) 
            
            #WORKSPACE_LEAVE_LABEL
            workspace_label3=Label(leave_label,text='LEAVE APPLICATION',bg='red',fg='yellow',font=8)
            workspace_label3.pack(pady=20,padx=10)
            
            #WORKSPACE_LEAVE_NAME_LABEL
            workspace_label4=Label(leave_label,text='Enter Your Name:',bg='red',fg='black')
            workspace_label4.pack(padx=10,pady=8)
            
            #WORKSPACE_LEAVE_ENTRY
            workspace_entry2=Entry(leave_label)
            workspace_entry2.pack(padx=10,pady=8)
            
            radvar=StringVar()
            radvar.set(0)
            
            rad=Radiobutton(leave_label,text=' Hospital ',variable=radvar,value='Hospital',bg='yellow',fg='red').pack(pady=2)
            rad=Radiobutton(leave_label,text=' Personal ',variable=radvar,value='Personal',bg='yellow',fg='red').pack(pady=2)
            rad=Radiobutton(leave_label,text=' Vacation ',variable=radvar,value='Vacation',bg='yellow',fg='red').pack(pady=2)
            
            def sendleaveapplication():
                employ_name=workspace_entry2.get() 
                reason=radvar.get()
                if (employ_name==''):
                    msg.showerror('Insert Status','Please Enter Your Name')
                else:
                    mycon=form_list.connect(host='localhost',user='root',passwd='soumyajit',database='project')
                    mycursor=mycon.cursor()
                    leave_reason="INSERT INTO leave_reason VALUES('{}','{}')".format(employ_name,reason)  
                    mycursor.execute(leave_reason)
                    mycon.commit()
                    msg.showinfo('Message Status','Submitted Sucessfully') 
                    workspace_entry2.delete(0,END)
                    radvar.__del__() 
            
            #WORKSPACE_LEAVE_BUTTON
            workspace_leave_button=Button(leave_label,text='  SUBMIT  ',bg='yellow',fg='blue',command=sendleaveapplication)
            workspace_leave_button.pack(padx=10,pady=8)
            
            #WORKSPACE_CLOCK
            workspace_clock_label=Label(time_label,text='',font=14,bg='black',fg='red',relief='sunken',bd=3)
            workspace_clock_label.pack(padx=12,pady=12,side='right')
            
            #WORKSPACE_DATE
            workspace_date_label=Label(time_label,text='',font=8,bg='light green',fg='red')
            workspace_date_label.pack(padx=10,pady=12,side='right')
        
            #WORKSPACE_DAY
            workspace_day_label=Label(time_label,text='',font=8,bg='light green',fg='red')
            workspace_day_label.pack(padx=10,pady=12,side='right')
            
            clock()
            
            workspace_icon=PhotoImage(file='workspace.png')
            workspace_window.iconphoto(FALSE,workspace_icon)
             
            
            workspace_window.mainloop()
        else:
            msg.showerror('Insert Status','Login Failed')
            login_ask_window.destroy() 
                
            
    #LOGIN_ASK_WINDOW_CONFUGARATION
    login_ask_window=Toplevel()
    login_ask_window.title('LOGIN')
    login_ask_window.geometry('300x250')
    login_ask_window.minsize(300,250)
    login_ask_window.maxsize(300,250)
    login_ask_window.configure(bg='yellow')
    
    #LOGIN_ASK_LABEL
    login_ask_label1=Label(login_ask_window,text='  Enter Gmail:  ',bg='yellow',fg='blue',font=4)
    login_ask_label1.pack(pady=3)
    
    mail_text_variable=StringVar()
    
    #LOGIN_ASK_ENTRY
    login_ask_entry1=Entry(login_ask_window,font=4,relief='ridge',bd=2,textvariable=mail_text_variable)
    login_ask_entry1.pack(pady=3)
    
    #LOGIN_ASK_ENTRY_GET
    login_entry_get=mail_text_variable.get() 
    
    #LOGIN_OTP_LABEL
    login_otp_label=Label(login_ask_window,text='  Enter OTP  ',bg='yellow',fg='red',font=4)
    
    #LOGIN_OTP_ENTRY
    login_otp_entry=Entry(login_ask_window,font=4,relief='ridge',bd=2)
    
    #LOGIN_OTP_BUTTON
    login_otp_button=Button(login_ask_window,text=' Generate OTP ',command=generateotp,bg='black',fg='blue',relief='groove',bd=2,font=3)
    login_otp_button.pack(pady=5)
    
    #LOGIN_ASK_BUTTON
    login_ask_button=Button(login_ask_window,text='  Login  ',command=login,bg='red',fg='yellow',font=4,relief='groove',bd=4)
    
    #GENERATE_OTP
    OTP=random.randint(1000, 9999)
    
    login_ask_icon=PhotoImage(file='login.png') 
    login_ask_window.iconphoto(FALSE,login_ask_icon)
    
    #LOGIN_ASK_WINDOW_CLOSE
    login_ask_window.mainloop()

     
#ADMIN_DEFINED
def admin():
    def password():
        if password_value.get()==password_entry.get():
            
            
            #ADMIN_WINDOW_CONFUGARATION
            admin_window=Toplevel()
            #ADMIN_WINDOW_FULL_SCREEN
            admin_window.attributes('-fullscreen',TRUE)
            admin_window.title('ADMIN PANNEL')
            password_window.destroy()
            
            #ADMIN_MAIN_FRAME
            admin_main_frame=Frame(admin_window,bg='black')
            admin_main_frame.pack(fill='x')
            
            #ADMIN_DASHBOARD_LABEL
            admin_dashboard_label=Label(admin_main_frame,bg='yellow',width=100,height=300,bd=4)
            admin_dashboard_label.pack(side='left',anchor='nw')
            
            #GET_FROM_EMPLOY_LABEL
            admin_employ_label=Label(admin_main_frame,bg='green',height=300,bd=4)
            admin_employ_label.pack(side='right',anchor='ne')
            
            #ADMIN_COMMAND_LABEL
            admin_command_label=Label(admin_window,bg='red')
            admin_command_label.pack(fill='x')
            
            #ADMIN_TIME_LABEL
            admin_time_label=Label(admin_window,bg='sky blue')
            admin_time_label.pack(fill='x')
            
            #ADMIN_LABEL
            admin_label=Label(admin_dashboard_label,bg='red',text=' MANAGER DASHBOARD ',relief='ridge',font='helvatica 18 bold')
            admin_label.pack(pady=10)
            
            #ADMIN_DASGBOARD_SCROLLBAR
            admin_dashboard_scrollbar=Scrollbar(admin_dashboard_label)
            admin_dashboard_scrollbar.pack(fill='y',side='right')
            
            #ADMIN_TEXT
            admin_text=Text(admin_dashboard_label,height=41,width=90,yscrollcommand=admin_dashboard_scrollbar.set,relief='ridge')
            admin_text.pack(fill='x',pady=10,padx=10)
            admin_dashboard_scrollbar.config(command=admin_text.yview)
            
            #ADMIN_GET_INFO_LABEL_BUTTON
            def get():
                admin_text.insert(END,form_value_get)
            
            admin_button1=Button(admin_dashboard_label,command=get,text='  GET  ',relief='ridge',bd=2)
            admin_button1.pack(anchor='s',side='left',padx=35,pady=10)
            
            #ADMIN_HIDE_BUTTON_UNPACK 
            def hide():
        
                admin_delete_label.pack_forget()
                admin_delete_entry.pack_forget()
                admin_delete_button.pack_forget()
            
            admin_hide_button=Button(admin_dashboard_label,command=hide,text='  Hide  ',relief='ridge',bd=2)
            admin_hide_button.pack(anchor='s',side='right',pady=10,padx=35)
            
            #ADMIN_DELETE_LABEL_ENTRY_BUTTON_PACK
            def delete():
            
                admin_delete_label.pack(side='left',padx=1)
                admin_delete_entry.pack(side='left',padx=1)
                admin_delete_button.pack(side='left',padx=3)
            
            admin_button3=Button(admin_dashboard_label,command=delete,text='  DELETE  ',relief='ridge',bd=2)
            admin_button3.pack(anchor='s',side='left',padx=35,pady=10)
            
            #ADMIN_DELETE_LABEL_ENTRY_BUTTON
            def deleteentry():
                deleted_value=admin_delete_entry.get()
                if deleted_value=='':
                    msg.showerror('Insert Status','ID Required !!')
                else:
                    
                    mycon=form_list.connect(host='localhost',user='root',passwd='soumyajit',database='project') 
                    mycursor=mycon.cursor()
                    delete_record=("DELETE FROM form WHERE ID =" + deleted_value + '')
                    mycursor.execute(delete_record)
                    mycon.commit()
                    msg.showinfo('Delete Stauts','Deleted Sucessfully')
                    admin_delete_entry.delete(0,END)
                    
            #ADMIN_DELETE
            admin_delete_label=Label(admin_command_label,text='  Enter ID:  ')
            admin_delete_entry=Entry(admin_command_label)
            admin_delete_button=Button(admin_command_label,command=deleteentry,text='Delete Record')
        
            #ADMIN_GET_FROM_EMPLOY_WORK
            admin_employ_label2=Label(admin_employ_label,text='  Employ Records  ',bg='red',fg='black',font='Helvatica 18 bold',relief='ridge')
            admin_employ_label2.pack(pady=10)
            
            admin_employ_scrollbar=Scrollbar(admin_employ_label)
            admin_employ_scrollbar.pack(side='right',fill='y')
            
            admin_employ_text=Text(admin_employ_label,yscrollcommand=admin_employ_scrollbar.set,relief='ridge',height=41,width=90)
            admin_employ_text.pack(pady=10,padx=10)
            admin_employ_scrollbar.config(command=admin_employ_text.yview)
            
            #GET_EMPLOY_WORK
            def getemploywork():
                
                admin_employ_text.insert(END,employ_value_get)
                
            admin_employ_button=Button(admin_employ_label,text='  GET  ',command=getemploywork,relief='ridge',bd=2)
            admin_employ_button.pack(pady=10,padx=35,side='left',anchor='s')
            
            #ADMIN_EMPLOY_HIDE_BUTTON
            def hide():
                admin_employ_delete_label.pack_forget()
                admin_employ_delete_entry.pack_forget()
                admin_employ_delete_button.pack_forget()
            admin_employ_hide_button=Button(admin_employ_label,text='  HIDE  ',command=hide,relief='ridge',bd=2)
            admin_employ_hide_button.pack(side='right',pady=10,padx=35,anchor='s')
            
            #DELETE_EMPLOY_WORK
            def deleteemploywork():
                admin_employ_delete_label.pack(padx=1,side='left')
                admin_employ_delete_entry.pack(padx=1,side='left')
                admin_employ_delete_button.pack(padx=3,side='left')
            
            admin_employ_button_2=Button(admin_employ_label,text='  DELETE  ',command=deleteemploywork,relief='ridge',bd=2)
            admin_employ_button_2.pack(pady=10,padx=35,side='left',anchor='s')
            
            def deleteemployentry():
                deleted_value=admin_employ_delete_entry.get()
                if deleted_value=='':
                    msg.showerror('Insert Status','Enter Employ Name')
                else:
                    mycon=form_list.connect(host='localhost',user='root',passwd='soumyajit',database='project') 
                    mycursor=mycon.cursor()
                    delete_work=('DELETE FROM employ WHERE ID='+ deleted_value +'') 
                    mycursor.execute(delete_work)
                    mycon.commit()
                    msg.showinfo('Delete Status','Deleted Sucessfully') 
                    admin_employ_delete_entry.delete(0,END)
            
            admin_employ_delete_label=Label(admin_command_label,text='  Enter ID:  ')
            admin_employ_delete_entry=Entry(admin_command_label)
            admin_employ_delete_button=Button(admin_command_label,command=deleteemployentry,text='Delete Work')            
            
            #ADMIN_QUIT_BUTTON
            def quit():
                admin_window.destroy()
                
            admin_quit_button=Button(admin_command_label,command=quit,text="  QUIT  ",bg='blue',fg='yellow',relief='ridge',font='Helvatica 10 bold')
            admin_quit_button.pack(pady=4,side='right')
            
            #CLOCK
            def adminclock():
                import time
                hour=time.strftime('%I')
                minute=time.strftime('%M')
                seconds=time.strftime('%S')
                day=time.strftime('%A')
                am_pm=time.strftime('%p')
                date=time.strftime('%d')
                month=time.strftime('%m')
                year=time.strftime('%y')
                
                admin_clock_label.config(text=hour + ':' + minute + ':' + seconds + '' + '' + am_pm  + '')
                admin_clock_label.after(1000,adminclock)
                
                admin_day_label.config(text=day)
                admin_date_label.config(text=date + ',' + month + ',' + year + '') 
            
            admin_day_label=Label(admin_time_label,text='',font=6,bg='sky blue',fg='red')
            admin_day_label.pack(side='left',anchor='n',padx=10,pady=1)
        
            admin_date_label=Label(admin_time_label,text='',font=6,bg='sky blue',fg='red')
            admin_date_label.pack(side='left',anchor='n',padx=10,pady=1)
            
            admin_clock_label=Label(admin_time_label,text='',font=8,bg='black',fg='green',relief='sunken',bd=4)
            admin_clock_label.pack(side='left',anchor='n',padx=12,pady=1)
            
            adminclock()
            
            admin_icon=PhotoImage(file='admin.png') 
            admin_window.iconphoto(FALSE,admin_icon)
            
            admin_window.mainloop()
            
        else:
            #EMAIL_SENDING
            from time import time, ctime
            t=time()
            c=ctime(t)
            sender_mail='miniproject.storm@gmail.com'
            sender_password='miniproject'
            connection=smtplib.SMTP('smtp.gmail.com',587)
            connection.ehlo()
            connection.starttls() 
            connection.login(sender_mail, sender_password) 
            email_message='Subject: Security Alert !! \n\nSomeone just tried to login into your Admin Pannel on'+ '  ' + '' +  c  + ''
            connection.sendmail(sender_mail,'soumyajitmaj@gmail.com',email_message )  
            connection.quit()
            msg.showerror('Warning','Wrong Password')
            password_window.destroy()
            main_window.destroy()
        
    #PASSWORD_WINDOW_CONFUGARATION    
    password_window=Toplevel()
    password_window.title('PASSOWRD')
    password_value=StringVar(value='techbreeze')
    password_label=Label(password_window,text='Enter Password')
    password_label.pack()
    password_entry=Entry(password_window,show="*",font=12)
    password_entry.pack()
    password_button=Button(password_window,text='Submit',command=password)
    password_button.pack()
    
    password_icon=PhotoImage(file='password.png')
    password_window.iconphoto(FALSE,password_icon) 
    
    password_window.mainloop() 

#MAIN_WINDOW_CONFIGURATION
main_window.geometry('1400x620')
main_window.title('TECH BREEZE')
main_window.minsize(1400,620)
main_window.maxsize(1400,620)

#MAIN_LABEL_IMAGE
main_background_image=Image.open('main_background.png')
main_background_image_resized=main_background_image.resize((1400,700),Image.ANTIALIAS)
main_background_image_new=ImageTk.PhotoImage(main_background_image_resized)

main_label=Label(main_window,image=main_background_image_new)
main_label.pack(fill=BOTH)


#MAIN_COMPANY_IMAGE
main_company_image=Image.open('main6.png')
main_company_image_resized=main_company_image.resize((1400,550),Image.ANTIALIAS)
main_company_image_new=ImageTk.PhotoImage(main_company_image_resized)
 
image_label=Label(main_label,image=main_company_image_new)
image_label.pack() 

#MAIN_BUTTON
main_button1=Button(main_label,text='  NEW USER  ',bg='black',fg='blue',font=14,relief='groove',bd=3,command=new)
main_button1.pack(pady=8,side='left',padx=100)

main_button2=Button(main_label,text='  LOGIN  ',bg='black',fg='green',relief='groove',bd=3,command=loginask,font=14)
main_button2.pack(pady=8,side='left',padx=100)

main_button3=Button(main_label,text='  ADMIN  ',bg='black',fg='red',font=14,relief='groove',bd=3,command=admin)
main_button3.pack(pady=8,side='left',padx=100)
 
#MAIN_ICON 
main_icon=PhotoImage(file='main_icon.png')
main_window.iconphoto(FALSE,main_icon)


main_window.mainloop() 