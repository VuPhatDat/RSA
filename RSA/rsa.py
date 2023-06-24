import random
from Components import Components
import hashlib

list_Character_chr = ["a","b","c","d","e","f","g","h","i","j","k","m","l","n","o","p","q","r","s","t","u","v","w","x","y","z"]
list_Character_num = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25"]
list_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
p = 193
q = 197
n = p * q
phi_n = (p-1) * (q-1)
b = random.randint(1,phi_n)
while Components.gcd(b, phi_n) != 1:
    b = random.randint(1, phi_n)
a = Components.Inverst(b, phi_n)
def num(num):
    y = Components.bpvn(num, a, n)
    if y > 26:
        y = y % 26
    y = str(y)
    z = ''
    for i in range(0, 26):
        if y == list_Character_num[i]:
            z = list_Character_num[i]
    return z
def character(num):
    y = Components.bpvn(num, a, n)
    if y > 26:
        y = y % 26
    y = str(y)
    z = ''
    for i in range(0, 26):
        if y == list_Character_num[i]:
            z = list_Character_chr[i].upper()
    return z
def character2(num):
    y = Components.bpvn(num, b, n)
    if y > 26:
        y = y % 26
    y = str(y)
    z = ''
    for i in range(0, 26):
        if y == list_Character_num[i]:
            z = list_Character_num[i]
    return z
def RSA_sign(text_sign):
    text_sign = text_sign.upper()
    text = hashlib.new("md5")
    text.update(text_sign.encode())
    text = text.hexdigest()
    text_result = []
    i = 0
    while i < len(text):
        for j in range(0, 26):
            if text[i] == list_Character_num[j]:
                text_result.insert(i, character(list_num[j]))
            if text[i] == list_Character_chr[j]:
                text_result.insert(i, character(list_num[j]))
        i = i + 1
    ele = ""
    for i in text_result:
        ele += i
    return ele
def RSASignAllNumber(text_sign):
    text_sign = text_sign.upper()
    text = hashlib.new("md5")
    text.update(text_sign.encode())
    text = text.hexdigest()
    text_result = []
    i = 0
    while i < len(text):
        for j in range(0, 26):
            if text[i] == list_Character_num[j]:
                text_result.insert(i, num(list_num[j]))
            if text[i] == list_Character_chr[j]:
                text_result.insert(i, num(list_num[j]))
        i = i + 1
    return text_result
def RSA_check(text_sign):
    text_sign = text_sign.lower()
    text_result = []
    i = 0
    while i < len(text_sign):
        for j in range(0,26):
            if text_sign[i] == list_Character_chr[j]:
                text_result.insert(i, character2(list_num[j]))
        i += 1
    return text_result

def ss(text_a, text_b):
    text_check_a = RSASignAllNumber(text_a)
    text_check_b = RSA_check(text_b)
    list_check_a = []
    list_check_b = []
    k = text_check_a[0]
    h = text_check_b[0]
    i = 1
    flag = 0
    while i < len(text_check_a):
        if text_check_a[i] == k:
            list_check_a.append(i)
            flag += 1
        i += 1
    i2 = 1
    while i2 < len(text_check_b):
        if text_check_b[i2] == h:
            list_check_b.append(i2)
        i2 += 1
    count = 1
    i3 = 0
    while i3 < flag:
        if list_check_a[i3] != list_check_b[i3]:
            count = 0
            break
        i3 += 1
    if count == 1:
        return 'khop'
    else:
        return 'khong khop'