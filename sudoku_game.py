<Modalities>
</Modalities>
<Modalities>
</Modalities>
from llm_assist import fill_row

sudoku = [
    [0, 1, 0, 0, 3, 0, 4, 0, 0],
    [0, 0, 0, 7, 4, 5, 0, 0, 0],
    [0, 0, 4, 0, 9, 6, 0, 3, 0],
    [7, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 8, 1, 0, 0, 7, 0, 9, 4],
    [0, 0, 0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 7, 0, 0, 2, 0],
    [6, 7, 3, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 5, 0, 1, 0, 4, 7],
]

def display_board(board):
    for row in board:
        print(" ".join(str(cell) if cell != 0 else "." for cell in row))

def main():
    print("初始数独：")
    display_board(sudoku)
    print("\n输入 `fill row x` 填写第 x 行（从1开始）")
    command = input("输入命令: ")
    if command.startswith("fill row"):
        row_num = int(command.split()[-1]) - 1
        new_row = fill_row(row_num)
        sudoku[row_num] = new_row
        print("\n填写后的数独：")
        display_board(sudoku)

if __name__ == "__main__":
    main()
