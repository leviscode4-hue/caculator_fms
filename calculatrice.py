import tkinter as tk 


root = tk.Tk()   
root.title(' Calculator')
root.geometry('500x600') 
root.configure(background='light blue')

def calculate(event):
    text = event.widget.cget('text')
    if text == '=':
        try:
            result= str(eval(entry.get()))
            entry.set(result)
        except Exception as e:
            entry.set('Error')
        return

    if text == 'C':
        entry.set('')
        return
    entry.set(entry.get() + text)

entry = tk.StringVar()       
entry.set('')
entry1 = tk.Entry(root, textvar=entry, font='lucida 30 bold', bd=5, insertwidth=4, bg='powder blue', justify='right' )
entry1.pack(fill=tk.X, ipadx=8, pady=10, padx=10)




button_frame = tk.Frame(root)
button_frame.pack()

button_list =[
    '7',  '8',  '9',  '/',
    '4',  '5',  '6',  '*',
    '1',  '2',  '3',  '-',
    '.',  '0',  '=',  '+',
    '00',  '000',  'C','⌫'
]

i = 0 

for btn_text in button_list:
    button = tk.Button(button_frame, text=btn_text, font = 'lucida 20 bold', bg='skyblue')
    button.grid(row=int(i/4), column=i%4, padx=3, pady=3)
    i+= 1
    button.bind('<Button-1>', calculate)
root.mainloop()