<div align="center">

# Caesar-Cipher Decipher Tool

[![Python](https://img.shields.io/badge/Python-any_version-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/ "Download Python")
[![Lexicon](https://img.shields.io/badge/Lexicon-10%2C000_words-5c8e25?style=for-the-badge)](#program-features "Program Features")
[![License](https://img.shields.io/badge/License-Educational-lightgrey?style=for-the-badge)](#license "License")

</div>

## Authors

- Gal Rubinstein
- Ben Liberman

---

This project implements a phrase deciphering utility that attempts to decrypt an encoded sentence using Caesar Cipher and a known English word lexicon. The system evaluates all possible Caesar Cipher shifts and checks if the resulting words are in the provided lexicon.

Key components include:

* Caesar Cipher decryption using a custom alphabet list
* Phrase validation against a precompiled lexicon of 10,000 common English words
* Outputs the original phrase and the shift value if deciphering is successful

* [SETUP INSTRUCTIONS](#setup-instructions)
    * [Custom configuration](#custom-configuration)
* [PROGRAM FEATURES](#program-features)
    * [Status codes](#status-codes)
* [LICENSE](#license)

# SETUP INSTRUCTIONS

1. **Clone the repository:**

    ```bash
    git clone https://github.com/JusticeIL/caesar-cipher-decipher-tool.git
    cd caesar-cipher-decipher-tool
    ```

2. **Configure the input.** Open [config-decipher.json](config-decipher.json) with any text editor, and insert your secret string under the key `"secret_phrase"`.
3. **(Optional)** Apply a [custom configuration](#custom-configuration).
4. **Run the program**, either way:

    Where|How
    :---|:---
    Python IDE (e.g., PyCharm)|Open [decipher.py](decipher.py) and run the code in the IDE
    Terminal|In the terminal window from step 1, run `python3 decipher.py`

**Important**: Any Python version must be pre-installed on your machine.

## CUSTOM CONFIGURATION

File|Description
:---|:---
[lexicon.pkl](data/lexicon.pkl)|Replace or modify it with a custom word list
[abc.txt](data/abc.txt)|Replace or edit it to change the decoding alphabet

# PROGRAM FEATURES

Feature|Description
:---|:---
Caesar Cipher Decryption|The program shifts characters backward through a predefined alphabet to decode potential phrases
Lexicon Validation|Only phrases where all decoded words exist in the lexicon are considered valid
Robust Error Handling|Detects missing files or empty input strings and returns appropriate status codes

## STATUS CODES

Code|Meaning
:---|:---
`0`|Successful decryption
`1`|No valid decryption found
`2`|Input phrase is empty

# LICENSE

This repository is intended for educational purposes.
