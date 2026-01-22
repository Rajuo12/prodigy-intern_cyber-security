# Password Strength Checker (Tkinter)

A simple desktop utility built with Python and Tkinter that evaluates the strength of a password entered by the user. It provides an overall strength rating (Strong / Moderate / Weak) and detailed feedback on which criteria are missing.

## Features
- Graphical user interface using Tkinter
- Real-time strength assessment when the user clicks "Check Password Strength"
- Strength categories: Strong (green), Moderate (orange), Weak (red)
- Detailed suggestions to improve the password:
  - Minimum length requirement
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
  - At least one special character

## How it works
The checker evaluates the password against five criteria:
1. Length >= 8
2. Contains an uppercase letter
3. Contains a lowercase letter
4. Contains a digit
5. Contains a special character from the set `!@#$%^&*(),.?":{}|<>`

Each satisfied criterion increases the score by 1. The final score determines the rating:
- 5: Strong
- 3–4: Moderate
- 0–2: Weak

## Requirements
- Python 3.x
- Tkinter (usually included with standard Python distributions)
- No external libraries required

## Installation & Usage
1. Save the provided script to a file, e.g. `password_checker.py`.
2. Run it from a terminal or by double-clicking:
   ```
   python password_checker.py
   ```
3. Enter a password in the text field and click "Check Password Strength".

## Safety note
- This tool is for local, offline evaluation only. Do not paste or test sensitive or production passwords you cannot change — treat any password pasted into the app as potentially exposed.
- The program does not store or transmit passwords.

## Customization
- Change the minimum required length by modifying the `length_check` condition.
- Extend or restrict the allowed special character set by editing the regular expression used for `special_char_check`.
- Update colors, fonts, or layout via Tkinter widget options in the script.

## Example
Save and run the script; the window will prompt for a password and show an overall rating and line-by-line suggestions to improve the password strength.

## License
MIT License — feel free to reuse and adapt.
