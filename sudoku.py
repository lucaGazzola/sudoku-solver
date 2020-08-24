import numpy as np

def square(sudoku,k,j):
    if k < 3 and j < 3:
        return sudoku[0:3, 0:3]
    if k < 3 and j >= 3 and j < 6:
        return sudoku[0:3, 3:6]
    if k < 3 and j >= 6 and j < 9:
        return sudoku[0:3, 6:9]
    if k >= 3 and k < 6 and j < 3:
        return sudoku[3:6, 0:3]
    if k >= 3 and k < 6 and j >= 3 and j < 6:
        return sudoku[3:6, 3:6]
    if k >= 3 and k < 6 and j >= 6 and j < 9:
        return sudoku[3:6, 6:9]
    if k >= 6 and k < 9 and j < 3:
        return sudoku[6:9, 0:3]
    if k >= 6 and k < 9 and j >= 3 and j < 6:
        return sudoku[6:9, 3:6]
    if k >= 6 and k < 9 and j >= 6 and j < 9:
        return sudoku[6:9, 6:9]


def fill(sudoku):
    tmp = np.array(sudoku)
    possibilities = {}
    flag = False
    for k in range(0,len(sudoku)):
        for j in range (0,len(sudoku[k])):
            if sudoku[k][j] == 'e':
                for i in range(1,10):
                    if str(i) not in sudoku[k] and str(i) not in sudoku[:,j] and str(i) not in square(sudoku,k,j):
                        flag = True
                        if (k,j) not in possibilities:
                            possibilities[(k,j)] = [str(i)]
                        else:
                            possibilities[(k,j)].append(str(i))
    
    for k in range(0,len(sudoku)):
        for j in range (0,len(sudoku[k])):
            if (k,j) in possibilities:
                if len(possibilities[(k,j)]) == 1:
                    sudoku[k][j] = possibilities[(k,j)][0]
    
    if flag:
        return fill(sudoku)
    else:
        print('sudoku filled.')
        return sudoku

def load(filename):
    print('loading sudoku...')
    sudoku = []
    sudokuFile = open(filename, 'r')
    lines = sudokuFile.readlines() 
    for line in lines:
        line = line.strip("\n") 
        sudoku.append(line.split(','))
    print('sudoku loaded.')
    return np.array(sudoku)

def print_formatted(sudoku):
    for row in sudoku:
        for cell in row:
            print("{}|".format(cell if cell != 'e' else ' '),end='')
        print('')

if __name__ == '__main__':
    sudoku = load('sudoku_easy2.txt')
    print_formatted(sudoku)
    solved_sudoku = fill(sudoku)
    print_formatted(solved_sudoku)