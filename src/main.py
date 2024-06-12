import onetimepad
import tkinter
from tkinter import ttk
from tkinter import messagebox as mb

import sv_ttk

root = tkinter.Tk(screenName="EzEncrypt")
root.title("EzEncrypt")
root.geometry("700x300")
root.grid_anchor(anchor="center")
root.eval('tk::PlaceWindow . center')

# functions


def encryptMessage():
    if (stEntry.get() == ""):
        mb.showerror(title="Error", message="Please enter a secret key")
        pass
    elif (ptEntry.get() == ""):
        mb.showerror(
            title="Error", message="Please enter a plaintext to encrypt")
        pass
    pt = ptEntry.get()
    # encrypt the message
    et = onetimepad.encrypt(pt, stEntry.get())
    etEntry.config(state='normal')
    etEntry.delete(first=0)
    etEntry.insert(0, et)
    etEntry.config(state='readonly')


def decryptMessage():
    if (stEntry.get() == ""):
        mb.showerror(
            title="Error", message="Please enter a secret key")
        pass
    elif (ctEntry.get() == ""):
        mb.showerror(
            title="Error", message="Please enter a plaintext to encrypt")
        pass
    ct = ctEntry.get()
    # encrypt the message
    dt = onetimepad.decrypt(ct, stEntry.get())
    dtEntry.config(state='normal')
    dtEntry.delete(first=0, last=len(dtEntry.get()))
    dtEntry.insert(0, dt)
    dtEntry.config(state='readonly')


# labels
stLabel = ttk.Label(root, text="Secret Key")
stLabel.grid(row=8, column=1, pady=5, padx=5)

ptLabel = ttk.Label(root, text="Plain Text")
ptLabel.grid(row=10, column=1, padx=5)

etLabel = ttk.Label(root, text="Encrypted Text")
etLabel.grid(row=11, column=1, padx=5)

ctLabel = ttk.Label(root, text="Cipher Text")
ctLabel.grid(row=10, column=10, padx=5)

dtLabel = ttk.Label(root, text="Decrypted Text")
dtLabel.grid(row=11, column=10, padx=5)

# create entries and position them on the grid
stEntry = ttk.Entry(root)
stEntry.grid(row=8, column=3, pady=5, padx=5)

ptEntry = ttk.Entry(root)
ptEntry.grid(row=10, column=3, padx=5)

etEntry = ttk.Entry(root, state='readonly')
etEntry.grid(row=11, column=3, padx=5)

ctEntry = ttk.Entry(root)
ctEntry.grid(row=10, column=11, padx=5)

dtEntry = ttk.Entry(root, state='readonly')
dtEntry.grid(row=11, column=11, padx=5)

# create encryption and decryption buttons to produce the output
encryptButton = ttk.Button(root, text="Encrypt", command=encryptMessage)
encryptButton.grid(row=13, column=3, sticky="EW", padx=5)

decryptButton = ttk.Button(root, text="Decrypt", command=decryptMessage)
decryptButton.grid(row=13, column=11, sticky="EW", padx=5)

# exit button
exitButton = ttk.Button(root, text="Exit", command=root.destroy)
exitButton.grid(row=20, column=1, sticky="EW")

# run the gui
sv_ttk.set_theme("dark")

root.mainloop()

# ? Build for current device:  pyinstaller --noconfirm --onefile --windowed --collect-data sv_ttk src/main.py
# ? Executable available at:   dist/main/main.exe
