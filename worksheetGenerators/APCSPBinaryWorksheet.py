import random
mylist = ["1111",15,"10101010",170,223,"11011111"]
print(
"""
Take a screenshot and complete in Notability OR copy/paste
the output into a text editor like Google Docs, Microsoft
Word, or the iOS Notes app. Set the font to COURIER NEW
and complete the worksheet.
"""
)
print(""" ______  _
(____  \(_)
 ____)  )_ ____  _____  ____ _   _
|  __  (| |  _ \(____ |/ ___) | | |
| |__)  ) | | | / ___ | |   | |_| |
|______/|_|_| |_\_____|_|    \__  |
                            (____/
Binary Worksheet""")

for i in range(1):
    print("                             Name: _______________")

print("\nPart A: Convert the 4-bit binary number to decimal")
print("  Hint: 8s 4s 2s 1s")
print("  For example, 1111\u208d\u2082\u208e = 15\u208d\u2081\u2080\u208e")
for i in range(4):
    temp = str(bin(random.randint(i,7)+random.randint(i,7)))
    temp = temp[2:].zfill(4)
    while temp in mylist:
      temp = str(bin(random.randint(i,7)+random.randint(i,7)))
      temp = temp[2:].zfill(4)
    mylist.append(temp)
    print(
        "%6s.) %21s"
        % (
            str(i + 1),
            str(temp) + "\u208d\u2082\u208e = ______\u208d\u2081\u2080\u208e",
        )
    )
print("\nPart B: Convert the 8-bit binary number to decimal")
print("  Hint: 128s 64s 32s 16s 8s 4s 2s 1s")
print("  For example, 10101010\u208d\u2082\u208e = 170\u208d\u2081\u2080\u208e")
for i in range(4):
    temp = str(bin(random.randint(i,i*31+31)+random.randint(i,i*31+31)))
    temp = temp[2:].zfill(8)
    while temp in mylist:
      temp = str(bin(random.randint(i,i*31+31)+random.randint(i,i*31+31)))
      temp = temp[2:].zfill(8)
    mylist.append(temp)
    print(
        "%6s.) %26s"
        % (
            str(i + 5),
            str(temp) + "\u208d\u2082\u208e = ______\u208d\u2081\u2080\u208e",
        )
    )
print("\nPart C: Convert the decimal number to binary")
print("  For example, 223\u208d\u2081\u2080\u208e = 11011111\u208d\u2082\u208e")
for i in range(6):
    temp = random.randint(i, i * 20 + 10) + random.randint(i, i * 20 + 10) + i * 6
    while temp in mylist:
      temp = random.randint(i, i * 20 + 10) + random.randint(i, i * 20 + 10) + i * 6
    mylist.append(temp)
    print(
        "\n%6s.) %34s"
        % (
            str(i + 9),
            str(temp) + "\u208d\u2081\u2080\u208e = ____________________\u208d\u2082\u208e",
        )
    )
print("\nRaise your hand when finished.")
