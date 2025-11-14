import os

# read
# append
# write
# create
# Dave Gray pronounced the acronym as rocs

# read - error if it doesn't exist
f = open("names.txt", "r")


for line in f:
    print(line)

f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print("The file you want to read does not exist")
finally:
    f.close()

# Append - creates the files if it doesn't exist

f = open("names.txt", "a+")
f.write("\nNiel")
f.close()


f = open("names.txt")
print(f.read())
f.close()


# write (overwrites)

f = open("context.txt", "w")
f.write("I deleted all of context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# opens a file for writing, creates the file if it does not exist

f = open("name_list.txt", "w")

f.close()

# creates the specified file, return error if it already exists

if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()


# Delete a file
# avoid an error if it doesn't exist

if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("That file does not exist, mate")

with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)


