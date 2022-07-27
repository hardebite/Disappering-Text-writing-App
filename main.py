from tkinter import *
root=Tk()
root.title("Dangerous Writing App")
root.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
text= Entry(width=40)
text_label=Label( text="text").grid(column=1, row=1)
text.grid(row=1,column=2)

words=[]

def clear(event):
    root.after_cancel(5000)
    words.append(event.char)
    print(words)
    root.after(5000)
    text.delete(0,END)

#
# def key_pressed(event):
#     w=Label(root,text="Key Pressed:"+event.char)
#     w.place(x=70,y=90)
#     print(event.char)





# def key_pressed2(event):
#     w=Label(root,text="Key Pressed:"+event.char)
#     w.place(x=70,y=90)
#     print(event.char)
#     root.after(3000,clear)

# root.bind("<Key>",key_pressed)
root.bind("<KeyRelease>",clear)
root.mainloop()


