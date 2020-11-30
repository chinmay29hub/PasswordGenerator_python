import random


lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()__+"


all = lower + upper + numbers + symbols
length = 16


password = "".join(random.sample(all, length)) #join()=will join all the strings, random.sample()=will pick random values upto 'length' characters from 'all' without repeating it. 



print(password)
