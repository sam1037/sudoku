#structure

table = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
] # 0 stand for empty

def print_board():
    # show the sudoku table
    
    for i, row in enumerate(table):
        msg = ""
        if i % 3 == 0 and i !=0:
            print("- "*11)
        for i,num in enumerate(row):
            if i % 3 == 0 and i != 0:
                msg = msg + "| " + f"{num} "
            else:
                msg = msg + f"{num} "
        print(msg)

def findEmpty():
    for rownum, row in enumerate(table):
        for colnum, num in enumerate(row):
            if num == 0:
                return (rownum,colnum) 
    return "finished"

def check_valid(number, pos):
    numrow = pos[0]
    numcol = pos[1]
    blockx = numrow // 3
    blocky = numcol // 3
    for row, rowobj in enumerate(table):
        if row == numrow:
            if number in rowobj:
                return False
        for col, num in enumerate(rowobj):
            if col == numcol and num == number:
                return False
            if row in range(blockx*3,blockx*3+3) and col in range(blocky*3,blocky*3+3):
                if num == number:
                    return False
    return True

def solve():
    # condition for ending
    if findEmpty() == "finished":
        return True

    # repeat part
    pos = findEmpty()
    row = pos[0]
    col = pos[1]
    for trynum in range(1,10):
        if check_valid(trynum, pos):
            table[pos[0]][pos[1]] = trynum
            if solve():
                return True
            table[row][col] = 0
    return False


solve()
print_board()