from Tkinter import *
import tkMessageBox

#p=61
#q=277
#n=16897
#d=7793
#e=17


#public_key(16897,17)
#private_key(16897,7793)

LUT_encryption = dict()
LUT_decryption = dict()

def openFileSE():
    f = open("ReadmeE.txt", "r")
    for line in f:
        name = line[0:-1]
        etext.insert(END, name)
    f.close()

def openFileOE():
    f = open("ReadmeE.txt", 'w')
    names = etext.get(1.0, END)
    for i in names:
        f.write(i+"\n")
    f.close()

def openFileSD():
    f = open("ReadmeD.txt", "r")
    for line in f:
        name = line[0:-1]
        dtext.insert(END, name)
    f.close()

def openFileOD():
    f = open("ReadmeD.txt", 'w')
    names = dtext.get(1.0, END)
    for i in names:
        f.write(i+"\n")
    f.close()

def encrypt_message():
    e=int(entrye1.get())
    n=int(entryn.get())
    message=etext.get(1.0, END)
    encrypted_msg = ""
    for i in message:
        if i in LUT_encryption:
            encrypted_msg += LUT_encryption[i]
        else:
            numerize = int(ord(i))
            encrypt = pow(numerize, e, n)
            LUT_encryption[i] = unichr(encrypt)
            encrypted_msg += unichr(encrypt)
    clear_entrye()
    etext.insert(END, encrypted_msg)

def decrypt_message():
    n=int(16897)
    d=int(7793)
    message=dtext.get(1.0, END)
    decrypted_msg = ""
    for i in message:
        if i in LUT_decryption:
            decrypted_msg += LUT_decryption[i]
        else:
            numerize = int(ord(i))
            decrypt = pow(numerize, d, n)
            LUT_decryption[i] = unichr(decrypt)
            decrypted_msg += unichr(decrypt)
    clear_entryd()
    dtext.insert(END, decrypted_msg)

def clear_entryd():
    dtext.delete(1.0, END)

def clear_entrye():
    etext.delete(1.0, END)


root=Tk()
root.title("Encryptor 9000")

labele = Label(root, text="Encryption", bg="magenta", anchor=W, width=35)
labele.grid(row=0, column=0, sticky=EW, columnspan=6)

labeld = Label(root, text="Decryption", bg="blue", anchor=W, width=35)
labeld.grid(row=0, column=6, sticky=EW, columnspan=6)

labeln = Label(root, text="n=")
labeln.grid(row=1, column=0)

entryn = Entry(root, width=3)
entryn.grid(row=1, column=1, columnspan=1)

labele1 = Label(root, text="e=")
labele1.grid(row=1, column=2)

entrye1 = Entry(root, width=3)
entrye1.grid(row=1, column=3, columnspan=1)

ebutton = Button(root, text="Encrypt", command=encrypt_message)
ebutton.grid(row=1, column=4, sticky=EW,)

labelp = Label(root, text="Public Key: (16897,17)")
labelp.grid(row=1, column=6)

dbutton = Button(root, text="Decrypt", command=decrypt_message)
dbutton.grid(row=1, column=10, sticky=EW,)

scrollbar = Scrollbar(root, orient=VERTICAL)
etext=Text(root, width=4, height=15, yscrollcommand=scrollbar.set)
scrollbar.config(command=etext.yview)
scrollbar.grid(row=2, column=5, rowspan=10, sticky=NS)
etext.grid(row=2, column=0, sticky=EW, columnspan=5)

message1=etext

scrollbar = Scrollbar(root, orient=VERTICAL)
dtext=Text(root, width=4, height=15, yscrollcommand=scrollbar.set)
scrollbar.config(command=dtext.yview)
scrollbar.grid(row=2, column=11, rowspan=10, sticky=NS)
dtext.grid(row=2, column=6, sticky=EW, columnspan=5)


e=entrye1.get()
n=entryn.get()

menubar = Menu(root)
filemenu1 = Menu(menubar, tearoff=0)
filemenu1.add_command(label="Open", command=openFileSE)
filemenu1.add_separator()
filemenu1.add_command(label="Save", command=openFileOE)
menubar.add_cascade(label="Encription", menu=filemenu1)

filemenu2 = Menu(menubar, tearoff=0)
filemenu2.add_command(label="Open", command=openFileSD)
filemenu2.add_separator()
filemenu2.add_command(label="Save", command=openFileOD)
menubar.add_cascade(label="Decription", menu=filemenu2)
root.config(menu=menubar)
mainloop()