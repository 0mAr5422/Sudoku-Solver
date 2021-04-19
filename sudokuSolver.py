import collections ;
import time ;
import sys
def printSudoku(matrix) :
    answer = "  "
    for i in range(0 , 27) :
        answer += "_"
    answer += "\n"
    for i in range(len(matrix)):
        answer += "| "
        for j in range(len(matrix[i])) :
            answer += matrix[i][j] + "  ";
            if (j+1) % 3 == 0 and j != 0 :
                answer = answer[:-1]
                answer += "| "
        answer += "\n"
        if (i+1) % 3 == 0 and i != 0 :
            answer += "  "
            for x in range(0 , 27) :
                answer += "_"
            answer += "\n"

    print(answer)


def box(index) :
    if index[0] >=0 and index[0] <= 2 :
        if index[1] >= 0 and index[1] <= 2 :
            ## first box ;
            return 1 ;
        elif index[1] > 2 and index[1] <= 5:
            return 2 ;
        else :
            return 3
    elif index[0] > 2 and index[0] <= 5:
        if index[1] >= 0 and index[1] <= 2 :
            ## first box ;
            return 4 ;
        elif index[1] > 2 and index[1] <= 5:
            return 5 ;
        else :
            return 6
    else :
        if index[1] >= 0 and index[1] <= 2 :
            ## first box ;
            return 7 ;
        elif index[1] > 2 and index[1] <= 5:
            return 8 ;
        else :
            return 9


def isValidIndex(matrix , index , tar) :
    ind = d[tar]
    for x in ind:
        if x[0] == index[0] :
            return False;
        elif x[1] == index[1] :
            return False;
        elif box(x) == box(index) :
            return False;
    return True

def solveSudoku(matrix , x) :
    printSudoku(matrix)
    time.sleep(0.1)
    if x >= len(emptys):
        return True
    index = emptys[x]

    for i in range(1 , 10) :

        if isValidIndex(matrix , index , i) :
            matrix[index[0]][index[1]] = str(i)
            d[i].append(index)
            if solveSudoku(matrix , x+1) :
                return True;
            if x <0 :
                x = 0;
            matrix[index[0]][index[1]] = ".";
            d[i].pop();

    return False


def fillEmptys(matrix) :
    for i in range(0 , len(matrix)) :
        for j in range(0 , len(matrix[i])) :
            if matrix[i][j] == "." :
                emptys.append([i,j])
            else :
                d[int(matrix[i][j])].append([i,j])

matrix = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
emptys = []
d = collections.defaultdict(list) ;

fillEmptys(matrix)

solveSudoku(matrix,0)
