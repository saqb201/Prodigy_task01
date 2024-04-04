from tkinter import * 
from tkinter import filedialog 

root = Tk()
root.geometry("200x160")

def encrypt_image():
    file1 = filedialog.askopenfile(mode='r',filetypes=[('png file ','*.png')])
    if file1 is not None :
        print(file1)
        file_name = file1.name
        print(file_name)
        key = entry1.get(1.0,END)
        print(file_name,key)
        fi = open(file_name,'rb')
        image = fi.read()
        fi.close()
        image = bytearray(image)
        for index ,values in enumerate(image):
            image [index] = values^int (key)
        fil1 = open(file_name,'wb')
        fil1.write(image)
        fil1.close()    

b1=Button(root,text="enrypt",command=encrypt_image)
b1.place(x=70, y=10)


entry1 = Text(root,height=1,width=10)
entry1.place(x=50 , y=50)

root.mainloop()