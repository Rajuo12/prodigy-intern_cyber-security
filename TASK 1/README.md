# Caesar Cipher GUI (Tkinter)

A simple Python GUI application that encrypts and decrypts messages using the classic Caesar cipher. The interface is built with Tkinter and lets you enter a message and an integer shift value, then encrypt or decrypt with a click.

## Features
- Encrypt and decrypt text using a Caesar cipher
- Preserves letter case (uppercase/lowercase)
- Non-alphabetic characters (digits, punctuation, spaces) are left unchanged
- Shift value wraps around the alphabet (any integer supported via modulo 26)

## Requirements
- Python 3.6+
- Tkinter (usually included with standard Python installs)
  - On Debian/Ubuntu: `sudo apt-get install python3-tk`
  - On some minimal Python builds or Linux containers, you may need to install your platform package that provides Tkinter

## Usage
1. Save the provided script as `caesar_cipher_gui.py` (or another filename of your choice).
2. Run the script:
   ```
   python3 caesar_cipher_gui.py
   ```
3. In the GUI:
   - Enter the message in "Enter Message".
   - Enter an integer shift value in "Enter Shift Value" (positive for right shift).
   - Click "Encrypt" to see the encrypted message or "Decrypt" to reverse it.
   - The result displays below the buttons.

Example:
- Message: `Hello, World!`
- Shift: `3`
- Encrypted: `Khoor, Zruog!`

## How it works (brief)
The Caesar cipher shifts each alphabetic character by a fixed number of positions. The implementation:
- Normalizes the shift using `shift % 26`
- Applies a positive shift for encryption, negative for decryption
- Uses ASCII ranges to preserve case (A-Z and a-z)
- Leaves non-alpha characters unchanged

## Limitations & Notes
- The current GUI expects a valid integer in the shift field. If the field is empty or non-numeric, the script will raise a `ValueError`. You may want to add input validation to handle that gracefully.
- This is a classical substitution cipher and is not secure for modern cryptographic needs — it's intended for learning and demonstration.

## Possible Improvements
- Add validation and user-friendly error messages for invalid shift input
- Allow rotating through alphabet only for letters from other alphabets or add Unicode support
- Add copy-to-clipboard button for results
- Add file import/export options

## License
This project is provided under the MIT License. Adapt and reuse freely.

## Author
Created by Rajuo12
