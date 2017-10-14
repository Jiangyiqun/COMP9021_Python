from sys import exit

class SudokuError(Exception):
    def __init__(self, message):
        self.message = message


class Sudoku():
    def __init__(self, filename):
        self.matrix = []
        self.filename = filename
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


    def bare_tex_output(self):
        latex_prefix = [
                r'\documentclass[10pt]{article}',
                r'\usepackage[left=0pt,right=0pt]{geometry}',
                r'\usepackage{tikz}',
                r'\usetikzlibrary{positioning}',
                r'\usepackage{cancel}',
                r'\pagestyle{empty}',
                r'',
                r'\newcommand{\N}[5]{\tikz{\node[label=above left:{\tiny #1},',
                r'                               label=above right:{\tiny #2},',
                r'                               label=below left:{\tiny #3},',
                r'                               label=below right:{\tiny #4}]{#5};}}',
                '',
                r'\begin{document}',
                '',
                r'\tikzset{every node/.style={minimum size=.5cm}}',
                '',
                r'\begin{center}',
                r'\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\hline\hline',
                ]
        # generate latex file name
        latex_bare_filename = ""
        for s in self.filename:
            if s != ".":
                latex_bare_filename += s
            else:
                break
        latex_bare_filename += "_bare.tex"
        # create and handle latex file
        with open(latex_bare_filename, "w+") as output_file:
            # convert matrix to matrix_string, where every none zero value is string, and zero value is empty string
            matrix_string = []
            for row in self.matrix:
                row_string = []
                for e in row:
                    if e == 0:
                        row_string.append('')
                    else:
                        row_string.append(str(e))
                matrix_string.append(row_string)
            # write latex file
            for line in latex_prefix:
                output_file.write(line + "\n")
            for i in range(9):
                output_file.write(r"% Line " + str(i+1) + "\n")
                output_file.write(r"\N{}{}{}{}{" + matrix_string[i][0]
                                  + r"} & \N{}{}{}{}{" + matrix_string[i][1]
                                  + r"} & \N{}{}{}{}{" + matrix_string[i][2]
                                  + r"} &" + "\n"
                                  + r"\N{}{}{}{}{" + matrix_string[i][3]
                                  + r"} & \N{}{}{}{}{" + matrix_string[i][4]
                                  + r"} & \N{}{}{}{}{" + matrix_string[i][5]
                                  + r"} &" + "\n"
                                  + r"\N{}{}{}{}{" + matrix_string[i][6]
                                  + r"} & \N{}{}{}{}{" + matrix_string[i][7]
                                  + r"} & \N{}{}{}{}{" + matrix_string[i][8]
                                  + r"}"
                                  )
                if i+1 in (1, 2, 4 ,5 ,7 ,8):
                    output_file.write(r" \\ \hline" + "\n" + "\n")
                if i+1 in (3, 6):
                    output_file.write(r" \\ \hline\hline" + "\n" + "\n")
                if i+1 == 9:
                    output_file.write(r" \\ \hline\hline" + "\n"
                                        + r"\end{tabular}"  + "\n"
                                        + r"\end{center}" + "\n"
                                        + "\n"
                                        + r"\end{document}" + "\n"
                                        )

    def forced_tex_output(self):
        pass


    def marked_tex_output(self):
        pass

    def worked_tex_output(self):
        pass

if __name__ == '__main__':
    def print_matrix(matrix):
        for line in matrix:
            print(line, end='\n')


    sudoku = Sudoku('sudoku_4.txt')
    sudoku.bare_tex_output()
    # print_matrix(sudoku.matrix)