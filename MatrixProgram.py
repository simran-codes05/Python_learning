#Matrix position accessing index
row1 = ['O','O','O']
row2 = ['O','O','O']
row3 = ['O','O','O']

print(f"\n {row1} \n {row2} \n {row3}")
matrix = [row1 , row2 , row3]
position = input("Enter the position you want to hide your money :")

row_num = int(position[0])
col_num = int(position[1])

selected_row = matrix[row_num - 1]
selected_row[col_num - 1] = "X"

print(f"\n {row1} \n {row2} \n {row3}")