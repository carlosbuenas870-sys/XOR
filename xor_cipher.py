import random
key = ([str(random.randint(0, 1)) for i in range(50)])
text = input("Texto: ")
encrypted = ''.join([chr(ord(text[i]) ^ int(key[i % len(key)])) for i in range(len(text))])
print("Llave:", key, "\nEncriptado:", encrypted, "\nDesencriptado:", ''.join([chr(ord(encrypted[i]) ^ int(key[i % len(key)])) for i in range(len(encrypted))]))