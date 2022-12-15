lines = ["a","b"]
with open('key.txt','w') as f:
    for i in range (100000,999999):
        text="BTY"+str(i)
        f.write(text)
        f.write('\n')
#add 10 to the time spent after calculating the real time spent