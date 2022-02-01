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
