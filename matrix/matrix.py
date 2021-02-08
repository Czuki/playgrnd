class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

        self.rows_str = [row.split(' ') for row in matrix_string.splitlines()] #list comprehension for changing matrix string to matrix list
        self.rows_int = [[int(el) for el in row] for row in self.rows_str] # list comprehension for changing 'str' types to 'int' types in matrix list
        self.num_columns = len(self.rows_str[0]) #storing number of columns for later use

        self.col_int = [] #empty list for columns list
        for i in range(self.num_columns):
            self.col_int_tmp = [row[i] for row in self.rows_int]
            self.col_int.append(self.col_int_tmp.copy())
            self.col_int_tmp.clear()

    def row(self, index):
        return self.rows_int[index-1]

    def column(self, index):
        return self.col_int[index-1]

# a = Matrix("1 2 3 4\n5 6 7 8\n9 8 7 6")
# print(a.row(1))
# print(a.column(2))