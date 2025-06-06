# Caesar-Cipher Decipher Tool

## Authors

- Gal Rubinstein
- Ben Liberman

---

## Overview

This project implements a phrase deciphering utility that attempts to decrypt an encoded sentence using Caesar Cipher and a known English word lexicon.
The system evaluates all possible Caesar Cipher shifts and checks if the resulting words are in the provided lexicon.

Key components include:

- Caesar Cipher decryption using a custom alphabet list.
- Phrase validation against a precompiled lexicon of 10,000 common English words.
- Outputs the original phrase and the shift value if deciphering is successful.

---

## Setup Instructions

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/JusticeIL/caesar-cipher-decipher-tool.git
   cd caesar-cipher-decipher-tool
   ```

2. **Configure Input**  
   Open the file `config-decipher.json` with any text editor,  
   and insert your secret string under the key `"secret_phrase"`.


3. **(Optional) Custom Configuration**  
   - Replace or modify `lexicon.pkl` with a custom word list.  
   - Replace or edit `abc.txt` to change the decoding alphabet.

4. **Run the Program**  
   - Open `decipher.py` in your Python IDE (e.g., PyCharm) and run the code in the IDE.  
   - or in the terminal window from instrcution #1, run:
   ```bash
   python3 decipher.py
   ```
   
> 🔥 **Important:**  
> Any Python version must be pre-installed on your machine.

---

## Program Features

- **Caesar Cipher Decryption:**  
  The program shifts characters backward through a predefined alphabet to decode potential phrases.

- **Lexicon Validation:**  
  Only phrases where all decoded words exist in the lexicon are considered valid.

- **Robust Error Handling:**  
  Detects missing files or empty input strings and returns appropriate status codes.

- **Status Codes:**  
  - `0`: Successful decryption.
  - `1`: No valid decryption found.
  - `2`: Input phrase is empty.

---

## License

This repository is intended for educational purposes.
