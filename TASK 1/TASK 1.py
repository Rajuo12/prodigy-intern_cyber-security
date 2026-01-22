import tkinter as tk
from tkinter import messagebox

# Caesar Cipher Algorithm
def caesar_cipher(message, shift, mode='encrypt'):
    result = ""
    shift = shift % 26  # Ensure shift is within 0-25
    if mode == 'decrypt':
        shift = -shift
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Function for Encryption
def encrypt_message():
    message = entry_message.get()
    shift = int(entry_shift.get())
    encrypted = caesar_cipher(message, shift, mode='encrypt')
    output_label.config(text="Encrypted Message: " + encrypted)

# Function for Decryption
def decrypt_message():
    message = entry_message.get()
    shift = int(entry_shift.get())
    decrypted = caesar_cipher(message, shift, mode='decrypt')
    output_label.config(text="Decrypted Message: " + decrypted)

# Setting up the GUI
root = tk.Tk()
root.title("Caesar Cipher Application")

# Message Input
tk.Label(root, text="Enter Message:").grid(row=0, column=0, padx=10, pady=10)
entry_message = tk.Entry(root, width=50)
entry_message.grid(row=0, column=1, padx=10, pady=10)

# Shift Value Input
tk.Label(root, text="Enter Shift Value:").grid(row=1, column=0, padx=10, pady=10)
entry_shift = tk.Entry(root, width=50)
entry_shift.grid(row=1, column=1, padx=10, pady=10)

# Buttons for Encrypt and Decrypt
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message)
encrypt_button.grid(row=2, column=0, padx=10, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_message)
decrypt_button.grid(row=2, column=1, padx=10, pady=10)

# Output Label
output_label = tk.Label(root, text="Result: ")
output_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI loop
root.mainloop()
