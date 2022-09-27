from turtle import position


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(pln_txt, shift_amt):
    cipher_text = ""
    for letter in pln_txt:
        position = alphabet.index(letter)
        new_position = position + shift_amt
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print("The cipher is: " + cipher_text)
    restart()

def decrypt(cph_txt, shift_amt):
    pln_txt = ""
    for letter in cph_txt:
        position = alphabet.index(letter)
        new_position = position - shift_amt
        new_letter = alphabet[new_position]
        pln_txt += new_letter
    print("The cipher is: " + pln_txt)
    restart()

def caesar(cph_dir, srt_txt, sft_amt):
    if cph_dir.lower() == "encode"  or cph_dir.lower() == "e":
        encrypt(srt_txt, sft_amt)
    elif cph_dir.lower() == "decode" or cph_dir.lower() == "d":
        decrypt(srt_txt, sft_amt)
    else:
        print("Please enter a correct value.")

def restart():
    answer = input("Would you like to calculate again? Y or N?\n")
    if answer.lower() == "yes" or answer.lower() == "y":
        dn = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        tt = input("Type your message:\n").lower()
        st = int(input("Type the shift number:\n"))
        caesar(dn, tt, st)
    else:
        print("Goodbye!")

caesar(direction, text, shift)