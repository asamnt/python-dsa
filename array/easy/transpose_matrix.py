# O(W x H) time O(W x H) space
def get_transpose(matrix):
    transposed_matrix = []
    for col in range(len(matrix[0])):#how many columns we have
        newRow = []
        for row in range(len(matrix)):
            newRow.append(matrix[row][col])# instead of col,row, we go row,col
        transposed_matrix.append(newRow)
    return transposed_matrix