row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")

position = input("Where do you want to put the treasure?  ")

# grab the input from the user and identify the horizontal and vertical. convert to an integer
horizontal = int(position[0])
vertical = int(position[1])
# grab the veritcal position
selected = map[vertical - 1]
# grab horizontal, indetify the placement and replace/reassign the values. 
selected[horizontal - 1] = "X"
 
print(f"{row1}\n{row2}\n{row3}\n")