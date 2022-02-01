import time

print('HelloWorld')
print("Something else")

x = input("How are you? (good/bad):")
if x == "good":
    print("Nice to hear that.")
elif x == "bad":
    print("lololol stay sad")

for i in range(10):
    print("Nice")
    time.sleep(0.1)

y = input("What is your name?: ")
if y not in ["dan", "jeremy", "ethan", "sachin sachin"]:
    print("What the heck are you doing here?")
else:
    print("Hello", y)

print("Nice")

print("Im hacking into the mainframe")
time.sleep(2)
print("Preparing")
time.sleep(1)
print("...")
time.sleep(1)
for x in range(5000):
        print("0101010000111100110101000110101101010101001010101010101010101001010101")
        print("0101101011010101101100110010101100011010101101010101010101010101010101")
print("\n")

message = "Successfully hacked into the mainframe."
for i in range(0, len(message) - 1):
    print(message[i], end="")
    time.sleep(0.5))
print("\n")
