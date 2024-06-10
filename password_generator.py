import random
import pyperclip as clip

caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low = "abcdefghijklmnopqrstuvwxyz"
num = "1234567890"
sym = "!()-.?[]_`~;:@#$%^&*+="
seq = []

while True:
    N = int(input('Enter password length (8-32) : '))
    if(N < 8):
        print("Password length should be atleast 8 characters !\n")
        continue
    elif(N > 32):
        print("Password length should be less than 32 characters !\n")
        continue
    else:
        break

while True:
    if (input("Include upper case letters ? (y/n) : ")).lower() == 'y':
        seq.append(caps)
    if (input("Include lower case letters ? (y/n) : ")).lower() == 'y':
        seq.append(low)
    if (input("Include numbers ? (y/n) : ")).lower() == 'y':
        seq.append(num)
    if (input("Include symbols ? (y/n) : ")).lower() == 'y':
        seq.append(sym)
    if seq == []:
        print('ERROR : No set of character chosen !\n')
        continue
    else:
        break

password = ""
for i in range(N):
    password += ''.join(random.sample(seq[i%len(seq)], 1))

password = list(password)
for i in range(random.randint(0,N)):
    random.shuffle(password)
password = ''.join(password)

print("Generated password : " + password)
if input("Would you like to copy password to clipboard ? (y/n) ").lower() == 'y' :
    clip.copy(password)
