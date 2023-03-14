import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
synbols="[]{}()*;/._-"

all=lower+upper+numbers+synbols
length=16
passworld="".join(random.sample(all,length))
print(passworld)