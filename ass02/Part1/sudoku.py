from sys import exit

class SudokuError(Exception):
    def __init__(self, message):
        self.message = message


class Sudoku():
    def __init__(self, filename):
        self.matrix = []
        #   check the validity of input, and generate matrix
        with open(filename) as input_file:
            for line in input_file:
                if not line.isspace():
                    # check each value is an integer and between 0 and 9
                    matrix_row = []
                    for e in line.strip().replace(" ", ""):
                        try:
                            if int(e)>=0 and int(e)<=9:
                                matrix_row.append(int(e))
                            else:
                                # print('some integer out of range')
                                raise SudokuError('Incorrect input')
                                sys.exit()
                        except ValueError:
                            # print('some are not integer')
                            raise SudokuError('Incorrect input')
                            sys.exit()
                    # check the length of each row is 9
                    if len(matrix_row) != 9:
                        # print('check the length of each row is 9')
                        raise SudokuError('Incorrect input')
                        sys.exit()
                    self.matrix.append(matrix_row)
        # check the length of column is 9
        if len(self.matrix) != 9:
            # print('check the length of column is 9')
            raise SudokuError('Incorrect input')
            sys.exit()


    def preassess(self):
        # check numbers in each row is unique
        for row in self.matrix:
            existed_number = {0}
            for e in row:
                if e != 0:
                    if e in existed_number:
                        print('There is clearly no solution.')
                        return
                    else:
                        existed_number.add(e)

        # check numbers in each column is unique
        for j in range(9):
            existed_number = {0}
            for i in range(9):
                e = self.matrix[i][j]
                if e != 0:
                    if e in existed_number:
                        print('There is clearly no solution.')
                        return
                    else:
                        existed_number.add(e)
        # generate cells
        matrix_cell = []
        for nb_of_cell_i in range(3):
            for nb_of_cell_j in range(3):
                cell = []
                for i in range(nb_of_cell_i*3, 3 + nb_of_cell_i*3):
                    for j in range(nb_of_cell_j*3, 3 + nb_of_cell_j*3):
                        cell.append(self.matrix[i][j])
                matrix_cell.append(cell)
        # check numbers in each cell is unique
        for cell in matrix_cell:
            existed_number = {0}
            for e in cell:
                if e != 0:
                    if e in existed_number:
                        print('There is clearly no solution.')
                        return
                    else:
                        existed_number.add(e)
        print('There might be a solution.')






if __name__ == '__main__':
    def print_matrix(matrix):
        for line in matrix:
            print(line, end='\n')


    sudoku = Sudoku('sudoku_1.txt')
    sudoku.preassess()
    # print_matrix(sudoku.matrix)