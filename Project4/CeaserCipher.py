alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
               ,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encryption(plain_text, shift_number):
    ciper_text = ""
    for char in plain_text:
        if char in alphabets :           
            position = alphabets.index(char)
            new_position = (position + shift_number) % 26
            ciper_text +=alphabets[new_position]
        else:
            ciper_text += char
    print(f"Here your encrypt text : {ciper_text}")

def decryption(ciper_text, shift_number):
    plain_text = ""
    for char in ciper_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position - shift_number) % 26
            plain_text +=alphabets[new_position]
        else:
            plain_text += char
    print(f"Here your decrypt text : {plain_text}")

want_to_end = False
while not want_to_end :
    what_you_want_to_do = input("Type encrypt for encrypt, Type decrypt for decrypt : ")
    message = input("Type your message :").lower()
    shift = int(input("Type shift number :"))

    if what_you_want_to_do == "encrypt" :
        encryption(plain_text = message, shift_number = shift)
    elif what_you_want_to_do == "decrypt" :
        decryption(ciper_text = message, shift_number = shift)
         
    yes_or_no = input("Type 'yes' if you want to go again other wise type 'no' :")
    if yes_or_no == "no" :
        want_to_end = True
        print("Bye")
