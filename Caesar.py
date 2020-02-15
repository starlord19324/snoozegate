# Ця програма створена для кодування тексту за правилом кода Цезаря
# Використання: ввести ключ (порядок зміщення, цифри від 0)
# Ввести текст:
# Потрібно використовувати літери англійського алфавіту
# Copyright Anton Kharchenko, 2020 

L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

key = int(input('Ключ: '))
plaintext = str(input('Текст: '))


# encipher
ciphertext = ""
for c in plaintext.upper():
    if c.isalpha(): ciphertext += I2L[ (L2I[c] + key)%26 ]
    else: ciphertext += c

# decipher
plaintext2 = ""
for c in ciphertext.upper():
    if c.isalpha(): plaintext2 += I2L[ (L2I[c] - key)%26 ]
    else: plaintext2 += c

print (plaintext)
print (ciphertext)
print (plaintext2)
