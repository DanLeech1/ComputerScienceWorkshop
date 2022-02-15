import time

with open("DNAtext.txt", "r") as file: text = file.readlines()

while True:
    for line in text:
        print(line, end = "")
        time.sleep(0.05)