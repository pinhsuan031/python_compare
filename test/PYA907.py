# TODO
f_name = input()
lines = 0
words = []
characters = ""

with open(file=f_name, mode="r", encoding="utf-8") as f:

    for line in f:
        lines += 1
        words += line.split(" ")
        characters += line

characters = characters.replace(" ", "")
characters = characters.replace("\n", "")

print(f"{lines} line(s)")
print(f"{len(words)} word(s)")
print(f"{len(characters)} character(s)")

