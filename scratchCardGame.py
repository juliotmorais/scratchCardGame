import random

row1=["■","■","■"]
row2=["■","■","■"]
row3=["■","■","■"]
map=[row1, row2, row3]

print("")
print(f"{row1}\n{row2}\n{row3}")

win_column=  random.randint(1,3)-1
win_row= random.randint(1,3)-1
map[win_row][win_column] = "O"

print("Enter the position you want to scratch off!")
print("Enter as a 2 digit number, column first, row second.")
print("Example: 23 is column 2, row 3 (bottom center)")
position= input("Enter position here: ")

chosen_column = int(position[0])
chosen_row= int(position[1])
print("")

print(f"You chose {chosen_column},{chosen_row}")


map[chosen_row-1][chosen_column-1] = "X"

print(f"Winning position is {win_column+1},{win_row+1}")

if((win_row == chosen_row-1) and (win_column == chosen_column-1)):
    map[chosen_row-1][chosen_column-1] = "☆"
    print("")
    print("WINNER WINNER")
else:
    print("")
    print("Sorry! Try again!")

print("")
print(f"{row1}\n{row2}\n{row3}")
print("")
