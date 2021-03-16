# Sean Shea

s = []
k = []
ascii_key = []
key_string = "this is my key"
for letter in key_string:
    ascii_key.append(ord(letter))

#print(ascii_key)

key_length = len(ascii_key)
for i in range(256):
    s.append(i)
    k.append(ascii_key[i % key_length])

#print(s)
#print(k)

j = 0

for i in range(256):
    j = (j + s[i] + k[i]) % 256
    temp = s[i]
    s[i] = s[j]
    s[j] = temp

#print(s)

i = j = 0

message = input("Input text to be encrypted: ")

byte_array = bytearray(message, 'utf8')
byte_list = []
for byte in byte_array:
    binary = bin(byte)
    byte_list.append(binary)

#print(byte_list)
encrypted_message = []
saved_keyStream = []
for byte in byte_list:
    i = (i + 1) % 256
    j = (j + s[i]) % 256
    temp = s[i]
    s[i] = s[j]
    s[j] = temp
    t = (s[i] + s[j]) % 256
    keyStreamByte = s[t]
    binaryKey = bin(keyStreamByte)
    saved_keyStream.append(binaryKey)
    #print(keyStreamByte)
    #print(binaryKey)
    encrypted_message.append(int(byte, 2) ^ int(binaryKey, 2))

encrypted_message_string = ""
for byte in encrypted_message:
    encrypted_message_string += bin(byte)

print('Your encrypted message is ' + encrypted_message_string)

decrypted_message = []

count = 0
for byte in encrypted_message:
    decrypted_message.append(byte ^ int(saved_keyStream[count],2))
    count += 1

decrypted_string = ''
for letter in decrypted_message:
    decrypted_string += chr(letter)

print('Your decrypted message is: ' + decrypted_string)