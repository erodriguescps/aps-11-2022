from tkinter import *
from tkinter import filedialog
from hashlib import md5
from cryptography.fernet import Fernet 
import pyperclip as pc

# Head
menu = Tk() # Inicia a interface grafica
menu.title("Encriptação") # Define o titulo que aparece na janela
menu.geometry("925x308+100+100") # Define o tamanho da janela
menu.iconbitmap("images/icon.ico") # Define o icone

# Coloca o plano de fundo
bg = PhotoImage(file = "images/bg.png")
label = Label( menu, image = bg)
label.place(x = 0, y = 0)

# Funções:

def criptografar():
    texto = filedialog.askopenfilename(initialdir="C:/", title="Selecione o arquivo", filetypes=(("Text Files", "*.txt"),))
    texto = open(texto, 'r')
    abertura = texto.read()
    
    key = Fernet.generate_key() 
    fernet = Fernet(key) 
    
    mensagemEnc = fernet.encrypt(abertura.encode()) 
    mensagemDesc = fernet.decrypt(mensagemEnc).decode() 
    hash = abertura.encode("utf8")
    hash = md5(hash).hexdigest()
    
    resposta= f"""
    Texto cryptografado: {mensagemEnc}\n
    Chave: {key}\n
    Hash: {hash}
    """
    label_1 = Label(menu, width=900, anchor=W, bd=5, justify= LEFT, text= resposta)
    label_1.pack(padx=10)

    pc.copy(resposta)

    texto.close()

def descriptografar():
    def validar():  
        fernet = Fernet(chave_input.get()) 
        mensagemDesc = fernet.decrypt(texto_input.get(1.0, END)).decode() 
        
        hash = mensagemDesc.encode("utf8")
        hash = md5(hash).hexdigest()
        hash_igual = hash_input.get() == hash
        
        if hash_igual:
            Label(menu, text="HASH IDENTICO, ARQUIVO ORIGINAL", background="green", foreground='#009', anchor="center").place(x = 600, y=70, width=300, height=20)
        else:
            Label(menu, text="HASH DIFERENTE, ARQUIVO CORROMPIDO", background="red", foreground='#009', anchor="center").place(x = 600, y=70, width=300, height=20)

        Label(menu, text=f"{mensagemDesc}", background="#dde", foreground='#009', anchor="center").place(x = 600, y=90, width=300, height=210)

    Label(menu, text="Chave", background="#dde", foreground='#009', anchor="center").place(x = 10, y=80, width=200, height=20)
    chave_input = Entry(menu)
    chave_input.place(x=10, y=100, width=200, height=20)
    
    Label(menu, text="Hash", background="#dde", foreground='#009', anchor="center").place(x = 10, y=150, width=200, height=20)
    hash_input = Entry(menu)
    hash_input.place(x=10, y=170, width=200, height=20)

    Label(menu, text="Texto", background="#dde", foreground='#009', anchor="center").place(x = 10, y=220, width=200, height=20)
    texto_input = Text(menu)
    texto_input.place(x=10, y=240, width=200, height=60)

    btnDescriptografar =Button(menu, background="green", width=20, height=3, text="Validar", anchor="center", command=lambda: validar()).place(x = 350,y=240)
    
# Botões

btnCriptografar = Button(menu, width= 30, height= 1, text="Criptografar", command=lambda: criptografar())
btnCriptografar.pack(pady=10)

btnDescriptografar =Button(menu, width= 30, height= 1, text="Descriptografar", command=lambda: descriptografar()) 
btnDescriptografar.pack(pady=10)

# Esse sempre vai ficar na ultima linha, é o que impede de fechar a janela
menu.mainloop()
