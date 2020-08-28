import numpy as np

def is_possible(sudoku,i,j,n):
    return n not in sudoku[i] and n not in sudoku[:,j] and n not in sudoku[(i//3)*3:(i//3)*3+3, (j//3)*3:(j//3)*3+3]

def fill(sudoku):
    global counter
    for k in range(0,len(sudoku)):
        for j in range (0,len(sudoku[k])):
            if sudoku[k][j] == 0:
                for i in range(1,10):
                    if is_possible(sudoku,k,j,i):
                        sudoku[k][j] = i
                        fill(sudoku)
                        counter += 1
                        sudoku[k][j] = 0
                return
    print(sudoku)

if __name__ == '__main__':
    global counter
    sudoku = np.genfromtxt('sudoku_hard.csv', delimiter=',')
    print(sudoku)
    counter = 0
    fill(sudoku)
    print('filling procedure rolled back {} times'.format(counter))