#!/usr/bin/python

import random
import sys

with open("allowed_chars.txt") as allowed:
    al_chars = allowed.read().rstrip('\n').split("\\x")
    
print "Allowed Chars : \r\n" + str(al_chars[1::]) + "\r\n"
al_chars_int = []
for allowed_int in al_chars[1::]:
    x = int(str(allowed_int),16)
    al_chars_int.append(x)

print "Allowed Chars int: \r\n" + str(al_chars_int) + "\r\n"

target = sys.argv[1]

ind = target[6:8]+target[4:6]+target[2:4]+target[0:2]

target = 68719476735 - int(ind,16) + 1
target =  hex(target)[3::]

print target.upper()



target1 = int(target[6:8],16)
target2 = int(target[4:6],16)
target3 = int(target[2:4],16)
target4 = int(target[0:2],16)


def generate(target):
    total = 0
    while total != target:
            x1 = random.choice(al_chars_int)
            x2 = random.choice(al_chars_int)
            x3 = random.choice(al_chars_int)
            
            total = x1 + x2 + x3
            
            if total == target:
                print "[+] found : "+str(hex(target))+" =  " + str(hex(x1))[2::].upper() + " - " + str(hex(x2))[2::].upper() + " - " + str(hex(x3))[2::].upper()
                return str(hex(x1))[2::].upper()+" - "+str(hex(x2))[2::].upper()+" - " + str(hex(x3))[2::].upper()



x1 = generate(target1).split(" - ")
x2 = generate(target2).split(" - ")
x3 = generate(target3).split(" - ")
x4 = generate(target4).split(" - ")

def formathex(x1):
    y = []
    for x in x1:
        if len(x)==1:
            y.append("0"+x)
        else:
            y.append(x)
    return y

x1 = formathex(x1)
x2 = formathex(x2)
x3 = formathex(x3)
x4 = formathex(x4)

beg = "\r\nAND EAX,554E4D4A\r\n\
AND EAX,2A313235\r\n\
PUSH ESP\r\n\
POP EAX\r\n\
SUB EAX,55554D66\r\n\
SUB EAX,55554B66\r\n\
SUB EAX,5555506A\r\n\
PUSH EAX\r\n\
POP ESP\r\n"
print beg


def tostring(x1,x2,x3,x4):
    x = x4[0]+x3[0]+x2[0]+x1[0]
    y = x4[1]+x3[1]+x2[1]+x1[1]
    z = x4[2]+x3[2]+x2[2]+x1[2]
    
    block = "\r\nBlock : \r\nAND EAX,554E4D4A\r\nAND EAX,2A313235\r\nSUB EAX,"+x+"\r\nSUB EAX,"+y+"\r\n"+"SUB EAX,"+z+"\r\nPUSH EAX"
    return block

print tostring(x1,x2,x3,x4)

















