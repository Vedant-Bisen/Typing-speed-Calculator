'''This is a project file'''
'''Project idea - Typing speed test'''

import random,time

def remover(a):
    j = list(a)
    j.remove("\n")
    c = ""
    for b in j:
        c += b
    return c

def wpm_counter(string,i,start,end):
    t_time = round(end-start,2)
    s_string = i.split()
    wpm = round(len(s_string)/t_time*60,2)
    print("\nYour words per min are: ",wpm)

def accurancy(string,i):
    original = string.split()
    input = i.split()
    accurancy = 0
    inaccuracy = 0
    for k in range(0,len(input)):
        if (input[k]==original[k]):
            accurancy += 1
        else:
            inaccuracy +=1
    print("Your accuracy is: ",round(accurancy/(accurancy+inaccuracy)*100,2))


    

i = []
path1 = "C:/Users/Admin/Documents/Programing/Python/Typing-speed-Calculator/Words.txt"
f = open( path1 ,"r")

while(len(i) < 3000):
    a = str(f.readline())
    word = remover(a)
    i.append(word)

string = ""

for k in range(0,100):
    l = random.randint(0,3000)
    string += i[l]
    string += " "

print(string,"\n")
start = time.time()
i = str(input("Enter the above phrase: "))
end = time.time()

wpm_counter(string,i,start,end)
accurancy(string,i)
