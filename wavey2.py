import time



with open('wavey.txt') as f:
    line_list = f.readlines()
while(True):
    x = 1
    for i in range(18):
            print(line_list[x])
            time.sleep(0.1)
            x += 1
        