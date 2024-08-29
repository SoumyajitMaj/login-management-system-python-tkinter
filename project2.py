from tkinter import*
root=Tk()


root.title("Mental Health Tracker")
root.geometry("500x500")
root.minsize(500,500)
root.maxsize(500,500)


def get():
        i=0
        file=open("ques.txt","rt")
        content=file.readlines()
        while(i<5):
            
            question_box.insert(END,content[i])
            i=i+1
        
        file.close()

global score        
score=0
global a
a=[]
def submit():
    x = question_type.get()
    file1 = open("ans.txt", "r")
    file2 = open("wrong.txt", "r")    
    file3= open("worst.txt","r")
    content1 = file1.readlines()
    content2 = file2.readlines()
    content3=file3.readlines()
    file1.close()
    file2.close()
    file3.close()

    found_in_best = any(x in line for line in content1)
    found_in_avg = any(x in line for line in content2)
    found_in_worst= any(x in line for line in content3)

    if found_in_best:
        a.append(3)
    elif found_in_avg:
        a.append(-1)
    else:
        a.append(-2)

    ans_box.delete(0, 'end')
    


def display():
    score=0
    print(a)
    for i in a:
        score=score+i
    if (score>=10 and score<=15):
        display_text.insert(END,"Mental Status is Good")
    elif(score>=5 and score<10):
        display_text.insert(END,"Mental Status is Avg")
    elif(score>=0 and score<5):
        display_text.insert(END,"Mental Status is Bad")
    else:
        display_text.insert(END,"Mental Status is Worst")
    
question_label=Label(text="Questions Will Be Displayed Here",fg="red",font=10)
question_label.place(x=100,y=5)

question_box=Text(root)
question_box.place(x=25,y=50,height=150,width=450)

get_question=Button(root,text="Get",command=get)
get_question.place(x=230,y=210)



ans_label=Label(text="Type The Answers Here",font=10,fg="red")
ans_label.place(x=140,y=240)

question_type=StringVar()
ans_box=Entry(root,textvariable=question_type,font=10)
ans_box.place(height=50,width=400,x=50,y=270)

ans_button=Button(root,text="Submit",command=submit)
ans_button.place(x=225,y=330)

display_label=Label(root,text="Click to show your Mental Health Status",fg="red",font=10)
display_label.place(x=110,y=360)

display_button=Button(root,text="Display",command=display)
display_button.place(x=225,y=390)

display_text=Text(root)
display_text.place(x=20,y=430,height=40,width=450)

root.mainloop()
