import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
synbols = "[]{}()*;/._-"

all = lower + upper + numbers + synbols
length = 16
password = "".join(random.sample(all,length))

print(password)


