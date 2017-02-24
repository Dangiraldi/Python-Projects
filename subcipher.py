import random
alph='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#write function which generates a key, or random sequence of letters in alphabet
def key_gen():
    return random.sample(alph,len(alph))

#encryption function
def encrypt(plaintext,key):
    ciphertext=''
    for letter in plaintext:
        if letter in alph:
            i=alph.index(letter)
            ciphertext+=key[i]
        else:
            ciphertext+=letter
    return ciphertext

def decrypt(ciphertext,key):
    plaintext=''
    for letter in ciphertext:
        if letter in key:
            i=key.index(letter)
            plaintext+=alph[i]
        else:
            plaintext+=letter
    return plaintext

def main():
    k=key_gen()

    uin=input("What would you like to encrypt? ")
    uin=uin.upper()
    uin_encrypted=encrypt(uin,k)
    print(uin_encrypted)

    decryption=decrypt(uin_encrypted,k)
    print(decryption)

main()
