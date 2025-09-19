class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = [[0]*26 for _ in range(rows)]
        # TC : O(rows)
    
    # Helper Functions
    def cellValue(self, cell):
        return (int(cell[1:]) - 1, ord(cell[0]) - 65)
        # TC: O(1)
    
    def sheetValue(self, cell):
        if cell.isdigit():
            return int(cell)
        row, col = self.cellValue(cell)
        return self.sheet[row][col]
        # TC : O(1)

    def setCell(self, cell: str, value: int) -> None:
        row, col = self.cellValue(cell)
        self.sheet[row][col] = value
        # TC : O(1)

    def resetCell(self, cell: str) -> None:
        row, col = self.cellValue(cell)
        self.sheet[row][col] = 0
        # TC : O(1)

    def getValue(self, formula: str) -> int:
        exp = formula[1:].split('+')
        a = self.sheetValue(exp[0])
        b = self.sheetValue(exp[1])
        return a+b
        # TC : O(1)




# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)