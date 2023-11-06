
# 第四题： 数独解决方案验证    

def validate_sudoku(board):
    elements = set(range(1, 10))

    for b in board:
        if set(b) != elements: 
            return False
    for b in zip(*board):  
        if set(b) != elements: 
            return False

    for i in range(3, 10, 3):
        for j in range(3, 10, 3):
            elements_set = set()
            for w in range(j-3, j):
                for q in range(i-3, i):
                    elements_set.add(board[q][w])
            if elements != elements_set:
                return False
            
    return True
