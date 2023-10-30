import math 
str1=input("Enter the Word: ") 
final=[] 
final1=[] 
dict1={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 
'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,  
'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26} 
key_list = list(dict1.keys()) 
val_list = list(dict1.values()) 
k=int(input("Enter the Key: ")) 
def encryption(dict1): 
E=0 
st=[] 
for i in range(0,len(str1)): 
for keys,values in dict1.items(): 
if str1[i] in keys: 
E=(values+k)%26 
st.append(E) 
position = val_list.index(st[i]) 
final.append(key_list[position]) 
print(st) 
print("Encrypted Text: ",final) 
def decryption(dict1,final): 
E=0 
st=[] 
for i in range(0,len(final)): 
for keys,values in dict1.items(): 
if final[i] in keys: 
E=(values-k)%26 
st.append(E) 
position = val_list.index(st[i]) 
final1.append(key_list[position]) 
print(st) 
print("Decrypted Text: ",final1) 
encryption(dict1) 
decryption(dict1,final) 