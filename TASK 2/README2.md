# Image Encryption Tool (Tkinter + Pillow)

A simple desktop GUI that demonstrates a basic image "encryption" and "decryption" process using Python, Tkinter and Pillow. This project is intended for educational purposes to illustrate how pixel manipulation and simple arithmetic transforms can be combined to obfuscate image data. It is not intended for real-world secure encryption.

## Features
- Load PNG / JPG / JPEG images from disk.
- "Encrypt" an image by:
  - Swapping pixels in a 2x2 stride pattern.
  - Applying a simple per-channel additive math operation with a small integer key.
- "Decrypt" an image by reversing the above operations.
- Preview image in a small display panel inside the GUI.

## How it works (high level)
1. swap_pixels(image): Iterates over the image with a 2x2 stride and swaps each pixel at (i, j) with the pixel at (i+1, j+1) when available.
2. apply_math_operation(image, key): Adds `key` modulo 256 to each color channel (keeps alpha as-is for RGBA images). Using a negative key reverses that step.
3. Encryption = swap_pixels -> apply_math_operation(key=+15)
4. Decryption = apply_math_operation(key=-15) -> swap_pixels

Because the swap pattern and the additive key are deterministic and reversed in the correct order, running the decrypt routine should restore the original image (subject to image mode and boundaries).

## Requirements
- Python 3.7+
- Pillow (PIL fork)
- Tkinter (usually included with standard Python installs on Windows/macOS; for Linux you may need to install the system package that provides Tk)

Install dependencies:
```bash
pip install pillow
```

## Installation & Run
1. Clone or copy the project files to a directory.
2. Ensure dependencies are installed (see above).
3. Run the GUI script:
```bash
python image_encryptor.py
```
(Replace `image_encryptor.py` with the filename you saved the provided code under.)

## Using the GUI
1. Click "Load Image" and select a PNG or JPG/JPEG file.
2. Click "Encrypt Image" to apply the obfuscation steps and preview the result.
3. Click "Decrypt Image" to reverse the operations and preview the restored image.

Note: The GUI preview resizes images to a 300×300 display; the internal image operations preserve the original resolution.

## Customization
- Change the key: The script uses a default additive key of 15. To use a different key, edit the calls to `apply_math_operation(..., key=15)` and `apply_math_operation(..., key=-15)` to match your chosen integer. Use the negative of the same key to decrypt.
- Swap algorithm: The pixel-swapping function is intentionally simple. You can change the stride, swap pattern, or apply randomized permutations (store the permutation to decrypt later) to explore different transformations.

## Limitations & Security
- This is NOT cryptographically secure. The operations are trivial to reverse if the algorithm/key are known.
- Lossy image formats or conversions (e.g., repeated JPEG re-encoding) may prevent perfect restoration.
- For true confidentiality or integrity guarantees, use established cryptographic libraries and formats (e.g., AES, libsodium) and authenticated encryption modes.

## Troubleshooting
- If you see issues opening the GUI, ensure Tkinter is available for your Python installation:
  - On Debian/Ubuntu: `sudo apt-get install python3-tk`
- If images look incorrect after operations, confirm the image mode (RGB / RGBA) and that your Pillow version is recent.

## Contributing
Contributions are welcome for:
- Better UI/UX (progress, save encrypted/decrypted image buttons).
- More robust handling of different image modes and bounds.
- Implementing a secure encryption option (with a warning and separate code path).

Please open issues or pull requests with suggested improvements.

## License
This project is provided as-is for educational use. No warranty. You may copy or adapt the code; include attribution if sharing significant portions.

## Author
Created by Rajuo12 (example). Feel free to adapt and experiment for learning purposes.
