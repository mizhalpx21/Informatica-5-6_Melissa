def sum_of_row(matrix, row_number: int): #Difining the name sum_of_row
    row = matrix[row_number] #Asking for a row 
    row_sum = 0  #Starting our row_sum with 0
    for item in row:
        #row_sum = row_sum + item
        row_sum += item

    return row_sum

def sum_of_column(matrix, column_number: int):
    column_sum = 0
    for row in matrix: #For every row in the matrix...
        column_sum = column_sum + row[column_number] #we are going to add to the column sum
    return column_number

matrix = [[1,2,3,4,],[5,6,7,8],[9,10,11,12],[13,14,15,16]] #Each list is a row
#my_sum = sum_of_row(matrix,1)
my_sum = sum_of_column(matrix,2)
print(my_sum)

def change_element(matrix, column_number, row_number, new_value):
    row = matrix[row_number]
    row[column_number] = new_value     

matrix = [[1,2,3,4,],[5,6,7,8],[9,10,11,12],[13,14,15,16]] 
#my_sum = sum_of_row(matrix,1)
#my_sum = sum_of_column(matrix,2)

print(matrix)
change_element(matrix,2,3,1000)
print(matrix)
        