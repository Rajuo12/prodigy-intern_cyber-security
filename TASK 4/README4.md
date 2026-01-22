# Simple Key Logger (pynput)

A minimal Python script that listens to keyboard events (using `pynput`) and writes keystrokes to a text file (`simple_key_log.txt`). It records printable characters literally, writes a space for the spacebar and a newline for Enter, and writes other non-character keys (e.g., `Key.shift`, `Key.tab`) inside square brackets. Press `Esc` to stop the listener.

> IMPORTANT: This script captures keystrokes. Use it only on machines you own or when you have explicit permission. Unauthorized use may be illegal and unethical. See the "Security & Privacy" section below.

## Features
- Records typed characters to a log file.
- Represents special keys in a readable bracketed format (e.g., `[Key.shift]`).
- Space and Enter are recorded as `" "` and newline respectively.
- Stop the logger by pressing the `Esc` key.
- Very small and easy to extend.

## Requirements
- Python 3.6+
- pynput library

Install the dependency with pip:
```bash
pip install pynput
```

## Usage
1. Save the script (for example as `keylogger.py`) in the same folder where you want the log file to be created.
2. Run the script:
```bash
python keylogger.py
```
3. The script appends keystrokes to `simple_key_log.txt` in the same directory.
4. Press `Esc` to stop logging and exit the program.

## Script behavior summary
- Printable characters (letters, digits, punctuation) are written as-is.
- `Key.space` => writes a single space (` `).
- `Key.enter` => writes a newline (`\n`).
- Other special keys (e.g., `Key.shift`, `Key.ctrl_l`, `Key.tab`) are written as `[Key.name]`.
- The file is opened in append mode, so previous logs are preserved.

## Example log output
```
Hello world
[Key.enter]
This is a test[Key.space][Key.tab]more text[Key.enter]
```

## Customization
- Change the output file name by editing the `log_file` variable.
- Change the key that stops the script by modifying the `stop_logging` function.
- Add timestamps, window/application context, or filtering logic by extending the `log_key` function.

## Platform notes
- `pynput` supports Windows, macOS and Linux, but on macOS you may need to grant Accessibility permissions to the terminal or Python interpreter in System Preferences > Security & Privacy > Privacy.
- Behavior may vary slightly between platforms for certain special keys.

## Security & Privacy
This tool logs all keystrokes and can capture sensitive data. Do not run it on other people's computers or on shared/public systems without informed consent. Secure or delete log files containing sensitive information. Use responsibly and follow local laws and organizational policies.

## Troubleshooting
- Permission errors on macOS: give Accessibility permission to your Python interpreter.
- No keystrokes captured: ensure the script is running and the terminal/app has required permissions and focus.
- File not found / write errors: check file path permissions and available disk space.

## License
This README and the accompanying example script are provided under the MIT License. Use at your own risk.

## Minimal example script
(For reference — the script this README describes)
```python
from pynput.keyboard import Key, Listener

log_file = "simple_key_log.txt"

def log_key(key):
    with open(log_file, "a") as file:
        try:
            file.write(f"{key.char}")
        except AttributeError:
            if key == Key.space:
                file.write(" ")
            elif key == Key.enter:
                file.write("\n")
            else:
                file.write(f"[{str(key)}]")

def stop_logging(key):
    if key == Key.esc:
        return False

with Listener(on_press=log_key, on_release=stop_logging) as listener:
    listener.join()
```