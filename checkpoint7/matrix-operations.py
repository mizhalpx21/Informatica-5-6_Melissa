def sum_of_row(matrix, row_number: int):
    row = matrix[row_number]
    row_sum = 0
    for item in row:
        #row_sum = row_sum + item
        row_sum += item

    return row_sum

def sum_of_column(matrix, column_number: int):
    column_sum = 0
    for row in matrix:
        column_sum = column_sum + row[column_number]
    return column_number

matrix = [[1,2,3,4,],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#my_sum = sum_of_row(matrix,1)
my_sum = sum_of_column(matrix,2)
print(my_sum)