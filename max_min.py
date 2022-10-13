# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


print("How many integers would you like to enter?")
number = int(input())
print("please enter", number, "integers.")
for i in range(1, number + 1):
    f_number = input()
for digit in f_number:
    for letter in f_number:
        if int(digit) > int(letter):
            maximal = digit
            print("max:", maximal)
        elif int(letter) > int(digit):
            maximal = letter
            print("max:", maximal)
            if int(digit) < int(letter) < int(maximal):
                minimal = digit
                print("min:", minimal)
            elif int(letter) < int(digit) < int(maximal):
                minimal = letter
                print("min:", minimal)
            elif int(letter) < int(maximal):
                minimal = letter
                print("min:", minimal)
            elif int(digit) < int(maximal):
                minimal = letter
                print("min:", minimal)
            else:
                print("no minimum")
        else:
            print("no maximum")
