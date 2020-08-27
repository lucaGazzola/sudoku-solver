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

def is_possible(sudoku,i,j,n):
    return n not in sudoku[i] and n not in sudoku[:,j] and n not in square(sudoku,i,j)

def fill(sudoku):
    for k in range(0,len(sudoku)):
        for j in range (0,len(sudoku[k])):
            if sudoku[k][j] == 0:
                for i in range(1,10):
                    if is_possible(sudoku,k,j,i):
                        sudoku[k][j] = i
                        fill(sudoku)
                        sudoku[k][j] = 0
                return
    print(sudoku)

if __name__ == '__main__':
    sudoku = np.genfromtxt('sudoku_hard.csv', delimiter=',')
    print(sudoku)
    fill(sudoku)