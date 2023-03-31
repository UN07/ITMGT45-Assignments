#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Module 3: Individual Programming Assignment 1
Thinking Like a Programmer
This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.
    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "
    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 
    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    LShift = ""
    letter = str(letter)
    shift = int(shift)
    
    if 65 < ord(letter) > 90:
        US = "_"
        LShift = LShift + US
    
    elif ord(letter) == 32:
        US = "_"
        LShift = LShift + US
    
    elif 65 <= ord(letter) <= 90:
        let = ((ord(letter) - ord("A")) + shift)% 26
        ls = chr(let + ord("A"))
        LShift = LShift + ls
    
    else:
        pass
    
    return LShift 

shift_letter("A", 3)


# In[2]:


def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    LShift = ""
    message = str(message)
    shift = int(shift)
    
    if message.isupper():
        for i in message:
            if ord(i) == 32:
                ls = chr(ord(i))
                LShift = LShift + ls

            elif 65 <= ord(i) <= 90:
                letter = ((ord(i) - ord("A")) + shift)% 26
                ls = chr(letter + ord("A"))
                LShift = LShift + ls

            else:
                pass
    else:
        LShift = "error"
        
    return LShift

caesar_cipher("I AM JUAN", 5)


# In[3]:


def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.
    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.
    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    LShift = ""
    letter = str(letter)
    letter_shift = str(letter_shift)
    
    if letter.isupper() and letter_shift.isupper():
        if 65 < ord(letter) > 90:
            US = "_"
            LShift = LShift + US

        elif ord(letter) == 32:
            US = "_"
            LShift = LShift + US

        elif 65 <= ord(letter) <= 90 and ord(letter_shift) != 32:
            let = ((ord(letter) - ord("A")) + (ord(letter_shift)-65))% 26
            ls = chr(let + ord("A"))
            LShift = LShift + ls

        else:
            pass
    else:
        LShift = "error"
        
    return LShift


shift_by_letter("B", "Y")


# In[4]:


def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.
    Example:
    vigenere_cipher("A C", "KEY") -> "K A"
    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    
    LShift = ""
    
    message = str(message)
    key = str(key)
    key_let = [ord(i) for i in key]
    message_let = [ord(i) for i in message]

    if len(key) == len(message) and key.isupper() and message.isupper():
        for i in range(len(message)):
            if ord(message[i]) == 32:
                ls = " "
                LShift = LShift + ls
            
            elif ord(key[i]) == 32:
                ls = message[i]
                LShift = LShift + ls

            elif 65 <= ord(message[i]) <= 90:
                let = ((message_let[i] - ord("A")) + (key_let[i] - 65))% 26
                ls = chr(let + ord("A"))
                LShift = LShift + ls
            
            elif 65 < ord(message[i]) > 90 and ord(message[i]) != 32:
                LShift = "error"
                
            elif 65 < ord(key[i]) > 90 and ord(key[i]) != 32:
                LShift = "error"
        
            else:
                pass
    
    else:
        LShift = "error"
    
    return LShift
    
#vigenere_cipher("AAB ", "ACK ")
#vigenere_cipher("aab ", "ACK ")
#vigenere_cipher("AAA", "K Y") #<-- retain letter if a space is found in the key
#vigenere_cipher("ZZZZZ", "BBBBB")
vigenere_cipher("A C", "KEY")

