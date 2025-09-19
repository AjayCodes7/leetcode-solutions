class Spreadsheet {
    int[][] sheet;
    public Spreadsheet(int rows) {
        sheet = new int[rows][26];
    }

    private int[] cellValue(String cell){
        int row = Integer.parseInt(cell.substring(1)) - 1;
        int col = cell.charAt(0) - 65;
        return new int[] {row, col};
    }

    private int sheetValue(String cell){
        if(cell.matches("\\d+")) return Integer.parseInt(cell);
        int[] box = cellValue(cell);
        return sheet[box[0]][box[1]];
    }   
    
    public void setCell(String cell, int value) {
        int[] box = cellValue(cell);
        sheet[box[0]][box[1]] = value;
    }
    
    public void resetCell(String cell) {
        int[] box = cellValue(cell);
        sheet[box[0]][box[1]] = 0;
    }
    
    public int getValue(String formula) {
        String[] exp = (formula.substring(1)).split("\\+");
        int a = sheetValue(exp[0]);
        int b = sheetValue(exp[1]);
        return a+b;
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet obj = new Spreadsheet(rows);
 * obj.setCell(cell,value);
 * obj.resetCell(cell);
 * int param_3 = obj.getValue(formula);
 */