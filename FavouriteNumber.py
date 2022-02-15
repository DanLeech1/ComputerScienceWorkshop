
fav_no = input("Enter your favourite number")

with open("fav_num.txt", "w") as f:
    f.write(fav_no)

f.close

with open("fav_num.txt", "r") as f:
    nice = f.read()

input("Do you want to know your favorite number?")
print(nice)