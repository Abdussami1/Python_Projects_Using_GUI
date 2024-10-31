from tkinter import *
root = Tk()
root.title("Abdus Password Checker")
root.geometry("800x400")

def clear():
    e.delete(0,END)

def check():
    global p
    global uppercase
    global lowercase
    global digit
    global specialcharacter
    global result
    global clear_button
    global check_button
    global exit_button
    global result_frame 
    uppercase=lowercase=digit=specialcharacter=0
    p=e.get()
    result_frame.grid_forget()
    button_frame.grid_forget()
    result_frame=LabelFrame(root,padx=97,pady=10,bd=5)
    result_frame.grid(row=5,column=0,columnspan=3,padx=10,pady=10)
    if len(p)>=8:
        for i in p:
            if i.isupper():
                uppercase+=1
            elif i.islower():
                lowercase+=1
            elif i.isdigit():
                digit+=1
            elif i.isalnum()!= True and i!=' ':
                specialcharacter+=1
        if uppercase>=1:
            if lowercase>=1:
                if digit>=1:
                    if specialcharacter>=1:
                        result=Label(result_frame,text="Password is Valid and satisfy all the above conditions.",fg="blue",font="bold")
                        result.grid(row=0,column=0,columnspan=3)
                    else:
                        result=Label(result_frame,text="Password doesn't have any Special Character.",fg="red",font="bold")
                        result.grid(row=0,column=0,columnspan=3)
                elif digit<1 and specialcharacter>=1:
                    result=Label(result_frame,text="Password doesn't have any digit.",fg="red",font="bold")
                    result.grid(row=0,column=0,columnspan=3)
                elif digit<1 and specialcharacter<1:
                    result=Label(result_frame,text="Password doesn't have any digit and special character.",fg="red",font="bold")
                    result.grid(row=0,column=0,columnspan=3)
            elif lowercase<1 and digit>=1 and specialcharacter>=1:
                result=Label(result_frame,text="Password doesn't have any lowercase Alphabet.",fg="red",font="bold")
                result.grid(row=0,column=0,columnspan=3)
            elif lowercase<1 and digit<1 and specialcharacter<1:
                result=Label(result_frame,text="Password doesn't have any lowercase Alphabet, digit and special character.",fg="red",font="bold")
                result.grid(row=0,column=0,columnspan=3)
            elif lowercase<1 and digit<1 and specialcharacter>=1:
                result=Label(result_frame,text="Password doesn't have any lowercase Alphabet and digit.",fg="red",font="bold")
                result.grid(row=0,column=0,columnspan=3)
            elif lowercase<1 and digit>=1 and specialcharacter<1:
                result=Label(result_frame,text="Password doesn't have any lowercase Alphabet and special character.",fg="red",font="bold")
                result.grid(row=0,column=0,columnspan=3)
        elif uppercase<1 and lowercase>=1 and digit<1 and specialcharacter<1:
            result=Label(result_frame,text="Password doesn't have any uppercase alphabet, digit and special chracter.",fg="red",font="bold")
            result.grid(row=0,column=0,columnspan=3)
        elif uppercase<1 and lowercase>=1 and digit>=1 and specialcharacter>=1:
            result=Label(result_frame,text="Password doesn't have any uppercase alphabet.",fg="red",font="bold")
            result.grid(row=0,column=0,columnspan=3)
        elif uppercase<1 and lowercase>=1 and digit>=1 and specialcharacter<1:
            result=Label(result_frame,text="Password doesn't have any uppercase alphabet and special chracter.",fg="red",font="bold")
            result.grid(row=0,column=0,columnspan=3)
        elif uppercase<1 and lowercase>=1 and digit<1 and specialcharacter>=1:
            result=Label(result_frame,text="Password doesn't have any uppercase alphabet and digit.",fg="red",font="bold")
            result.grid(row=0,column=0,columnspan=3)
        elif uppercase<1 and lowercase<1 and digit>=1 and specialcharacter>=1:
            result=Label(result_frame,text="Password doesn't have any uppercase amd lowercase alphabet.",fg="red",font="bold")
            result.grid(row=0,column=0,columnspan=3)
        elif uppercase<1 and lowercase<1 and digit<1 and specialcharacter<1:
            result=Label(result_frame,text="Password doesn't have any uppercase and lowercase alphabet, digit and special character.",fg="red",font="bold")
            result.grid(row=0,column=0,columnspan=3)
        elif uppercase<1 and lowercase<1 and digit<1 and specialcharacter>=1:
            result=Label(result_frame,text="Password doesn't have any uppercase and lowercase alphabet and digit.",fg="red",font="bold")
            result.grid(row=0,column=0,columnspan=3)
        elif uppercase<1 and lowercase<1 and digit>=1 and specialcharacter<1:
            result=Label(result_frame,text="Password doesn't have any uppercase and lowercase alphabet and special character.",fg="red",font="bold")
            result.grid(row=0,column=0,columnspan=3)
    else:
        result=Label(result_frame,text="Password Should be minimum of 8 characters.",fg="red",font="bold")
        result.grid(row=0,column=0,columnspan=3)
    button_frame.grid(row=6,column=0,columnspan=3,padx=10,pady=10)
    clear_button.grid(row=0,column=0,padx=5,pady=5)
    check_button.grid(row=0,column=1,padx=5,pady=5)
    exit_button.grid(row=0,column=2,padx=5,pady=5)


head=Label(root,text="Abdus Password Checker",fg="red",font="calibri 20 bold")
information_frame=LabelFrame(root,padx=97,pady=10,bd=5)
information_1=Label(information_frame,text="Password must contain the following:-",font="bold" )
information_2=Label(information_frame,text="* Atleast 8 characters",fg="red",font="bold")
information_3=Label(information_frame,text="* Atleast one Uppercase and Atleast one lowercase Alphabet",fg="red",font="bold")
information_4=Label(information_frame,text="* Atleast one Digit",fg="red",font="bold")
information_5=Label(information_frame,text="* Atleast one Special Character",fg="red",font="bold")
label=Label(root,text="Enter Password",fg="purple",bd=5,relief=SUNKEN,font="bold")
e=Entry(root,width=55,fg="blue",bd=5,font="bold")

result_frame=LabelFrame(root,padx=97,pady=10,bd=5)
r=Label(result_frame,text="")


button_frame=LabelFrame(root,padx=190,pady=1,bd=5)
clear_button=Button(button_frame,text="CLEAR",command=clear,bd=5,font="bold")
check_button=Button(button_frame,text="CHECK",command=check,bd=5,font="bold")
exit_button=Button(button_frame,text="EXIT",command=root.quit,bd=5,font="bold")



head.grid(row=0,column=1)
information_frame.grid(row=1,column=0,columnspan=3,padx=5,pady=5)
information_1.pack(anchor=W)
information_2.pack(anchor=W)
information_3.pack(anchor=W)
information_4.pack(anchor=W)
information_5.pack(anchor=W)

label.grid(row=4,column=0,padx=5,sticky=W+E)
e.grid(row=4,column=1,columnspan=2)

result_frame.grid(row=5,column=0,columnspan=3,padx=10,pady=10)
r.grid(row=0,column=0,padx=5,pady=5)
button_frame.grid(row=6,column=0,columnspan=3,padx=10,pady=10)
clear_button.grid(row=0,column=0,padx=5,pady=5)
check_button.grid(row=0,column=1,padx=5,pady=5)
exit_button.grid(row=0,column=2,padx=5,pady=5)



root.mainloop()