# TODO

n = eval(input())

for _ in range(n):
    sentence = set(input().lower())
    sentence.discard(" ")
    if len(sentence) >= 26:
        print("True")
    else:
        print("False")