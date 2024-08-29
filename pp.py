import tkinter as tk

root = tk.Tk()

root.title("Mental Health Tracker")
root.geometry("500x500")
root.minsize(500, 500)
root.maxsize(500, 500)

questions = []
current_question_index = 0

def load_questions():
        file= open("ques.txt", "rt") 
        questions.extend(file.readlines())

def get():
    global current_question_index
    

    if current_question_index < len(questions):
        question = questions[current_question_index]
        question_box.delete(1.0, tk.END)
        question_box.insert(tk.END, question)
        current_question_index += 1
    else:
        question_box.delete(1.0, tk.END)
        question_box.insert(tk.END, "No more questions.")
        

global score
score = 0
a = []

def submit():
    x = question_type.get()
    file1 = open("best.txt", "r")
    file2 = open("avg.txt", "r")
    file3 = open("worst.txt", "r")
    content1 = file1.readlines()
    content2 = file2.readlines()
    content3 = file3.readlines()
    file1.close()
    file2.close()
    file3.close()

    found_in_best = any(x in line for line in content1)
    found_in_avg = any(x in line for line in content2)
    found_in_worst = any(x in line for line in content3)

    if found_in_best:
        a.append(3)
    elif found_in_avg:
        a.append(2)
    elif found_in_worst:
        a.append(1)
    else:
        a.append(0)

    ans_box.delete(0, 'end')

def display():
    score = 0
    for i in a:
        score = score + i
    if 10 <= score <= 15:
        display_text.delete(1.0, tk.END)
        display_text.insert(tk.END, "Mental Status is Good")
    elif 5 <= score < 10:
        display_text.delete(1.0, tk.END)
        display_text.insert(tk.END, "Mental Status is Avg")
    elif 0 <= score < 5:
        display_text.delete(1.0, tk.END)
        display_text.insert(tk.END, "Mental Status is Bad")
    else:
        display_text.delete(1.0, tk.END)
        display_text.insert(tk.END, "Mental Status is Worst")

load_questions()

frame=tk.Frame(root,bg="blue")
frame.place(x=10,y=1)

question_label = tk.Label(frame,text="Questions Will Be Displayed Here", fg="red", font=10)
question_label.place(x=100, y=5)

question_box = tk.Text(frame)
question_box.place(x=25, y=50, height=150, width=450)

get_question = tk.Button(frame, text="Get", command=get)
get_question.place(x=230, y=210)

ans_label = tk.Label(frame,text="Type The Answers Here", font=10, fg="red")
ans_label.place(x=140, y=240)

question_type = tk.StringVar()
ans_box = tk.Entry(frame, textvariable=question_type, font=10)
ans_box.place(height=50, width=400, x=50, y=270)

ans_button = tk.Button(frame, text="Submit", command=submit)
ans_button.place(x=225, y=330)

display_label = tk.Label(frame, text="Click to show your Mental Health Status", fg="red", font=10)
display_label.place(x=110, y=360)

display_button = tk.Button(frame, text="Display", command=display)
display_button.place(x=225, y=390)

display_text = tk.Text(frame)
display_text.place(x=20, y=430, height=40, width=450)

root.mainloop()
