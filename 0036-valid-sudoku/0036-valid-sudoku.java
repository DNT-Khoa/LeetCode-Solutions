import java.util.*;

class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<String> check = new HashSet<>();
        
        for (int row = 0; row < 9; row++){
            for (int column = 0; column < 9; column++) {
                char value = board[row][column];
                
                if (value == '.') {
                    continue;
                }
                
                if (!check.add(value + " in row " + row)
                    || !check.add(value + " in column " + column)
                    || !check.add(value + " in box index " + row / 3 + '-' + column / 3)
                   ) {
                    return false;
                }
            }
        }
        
        return true;
    }
}