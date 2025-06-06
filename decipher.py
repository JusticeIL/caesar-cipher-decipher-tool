import json
import pickle
import os
import sys

#This function returns the deciphered char by k in case the char is in abc.txt, and returns the char itself otherwise.
def char_by_k(abc, ch, k):
    new_ch = ch
    if ch in abc:
        index = abc.index(ch) - k
        if index < 0: #Exception from the abc list
            index += len(abc)
        new_ch = abc[index]
    return new_ch

#This function deciphers a phrase (if possible) and updates a dictionary accordingly.
def decipher_phrase(phrase, lexicon_filename, abc_filename):
    print(f'starting deciphering using {lexicon_filename} and {abc_filename}')

    if not os.path.isfile(lexicon_filename) or not os.path.isfile(abc_filename): #file does not exist
        print("file does not exist, exiting program...")
        sys.exit(1)

    result = {"status": 1, "orig_phrase": '', "K": -1}

    if phrase == '': #empty phrase
        result['status'] = 2
        return result

    with open (lexicon_filename , 'rb') as handle:
        lexicon = pickle.load(handle) #unpack the lexicon into a list

    with open(abc_filename, 'r') as abc_file:
        abc = abc_file.read().split() #unpack the abc

    for k in range(26): #all Ks possible [0,25]
        deciphered = ''
        for char in phrase:
            deciphered += char_by_k(abc, char, k)
        to_check_phrase = deciphered.split()

        all_exist = True

        for word in to_check_phrase: #check if all words are in lexicon
            if not word in lexicon:
                all_exist = False #at least one word is not in lexicon
                break
        if all_exist: #all words found correctly in lexicon
            result['orig_phrase'] = deciphered
            result['status'] = 0
            result['K'] = k
            break #found the K, stop searching for a K

    return result

students = {'id1': '209385509', 'id2': '322465600'} #Name1: Gal Rubinstein, Name2: Ben Liberman

if __name__ == '__main__':
    with open('config-decipher.json', 'r') as json_file:
        config = json.load(json_file)

    # note that lexicon.pkl is a serialized list of 10,000 most common English words
    result = decipher_phrase(config['secret_phrase'],
                             config['lexicon_filename'],
                             config['abc_filename'])

    assert result["status"] in {0, 1, 2}

    if result["status"] == 0:
        print(f'deciphered phrase: {result["orig_phrase"]}, K: {result["K"]}')
    elif result["status"] == 1:
        print("cannot decipher the phrase!")
    else:  # result["status"] == 2:
        print("empty phrase")