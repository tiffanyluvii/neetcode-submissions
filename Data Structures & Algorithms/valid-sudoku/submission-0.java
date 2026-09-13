class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<Character> [] boxes = new HashSet [10];
        HashSet<Character> [] rows = new HashSet [9];
        HashSet<Character> [] cols = new HashSet [9];

        int box = 0;

        for (int i = 0; i < 9; i++){
            boxes[i] = new HashSet<Character>();
            rows[i] = new HashSet<Character>();
            cols[i] = new HashSet<Character>();
        }


        for (int i = 0; i < 9; i++){
            for (int j = 0; j < 9; j++){
                // check boxes
                box = (i / 3) * 3 + (j / 3);
                System.out.println("i: " + i);
                System.out.println("j: " + j);
                System.out.println(board[i][j]);

                if (board[i][j] == '.') {
                    continue;
                }
                System.out.println("Box: " + box);
                if (boxes[box].contains(board[i][j])){
                    return false;
                }

                // check rows
                if (rows[i].contains(board[i][j])){
                    return false;
                }
                // check cols
                if (cols[j].contains(board[i][j])){
                    return false;
                }

                if (board[i][j] == '.'){
                    continue;
                }

                boxes[box].add(board[i][j]);
                rows[i].add(board[i][j]);
                cols[j].add(board[i][j]);
            }
        } 
        return true;
    }
}
