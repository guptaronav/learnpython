
alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(cleartext):
    cyphertext = ""
    for character in cleartext:
        if character in alphabet:
            newposition = (alphabet.find(character) + 13) % 26
            cyphertext += alphabet[newposition]
        else:
            cyphertext += character
    return cyphertext

for i in range(3):
    cleartext = input("Cleartext: ")
    cleartext = cleartext.lower()
    print(encrypt(cleartext))

#Ebani naq Fhunav ner gur orfg!
