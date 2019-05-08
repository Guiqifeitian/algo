import copy
class Solution(object):
    dc = set(["1","2","3","4","5","6","7","8","9"])
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        pro,flag,flag2 = self.getProba(board)
        if not flag2:
             return False
        if flag:
             return True
        m,n = self.getFirst(pro)
        for i in range(len(pro[m][n])):
            board[m][n] = pro[m][n][i]
            nex = self.solveSudoku(board) 
            if nex == False:
                # 如果讲当前空格处可能的值全部尝试过还是不能找到正确的解，那么就要告诉上一层空格填错了，回溯
                if i == len(pro[m][n]) - 1:
                    board[m][n] = "."
                    return False
                continue
            else:
                # 找到一个正确的解，不用再找了
                break;

    def getFirst(self,pro):
        for i in xrange(9):
            for j in xrange(9):
                if not pro[i][j] is None:
                     return i,j    
 
    def getExist(self,board,m,n):
        # 找出空格处不可能的值
        res = []
        for i in xrange(9):
            if board[m][i] != ".":
                res.append(board[m][i])
            if board[i][n] != ".":
                res.append(board[i][n])
        for i in xrange((m/3) * 3,(m/3) * 3 + 3):
            for j in xrange((n/3) * 3,(n/3) * 3 + 3):
                if board[i][j]  != ".":
                    res.append(board[i][j])
        return set(res)
    
    def getProba(self,board):
        prob = copy.deepcopy(board)
        flag = True
        flag2 = True
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == ".":
                    prob[i][j] = list(self.dc - self.getExist(board,i,j))
                    # 如果某个空格处可能的值为空，说明这条路径走失败了
                    if len(prob[i][j]) == 0:
                        flag2 = False
                    flag = False
                else:
                    # 没有空格，说明全部都填完了，获得了解
                    prob[i][j] = None
        return prob,flag,flag2

s = Solution()
#board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
board = [[".",".",".",".",".","7",".",".","9"],[".","4",".",".","8","1","2",".","."],[".",".",".","9",".",".",".","1","."],[".",".","5","3",".",".",".","7","2"],["2","9","3",".",".",".",".","5","."],[".",".",".",".",".","5","3",".","."],["8",".",".",".","2","3",".",".","."],["7",".",".",".","5",".",".","4","."],["5","3","1",".","7",".",".",".","."]]
s.solveSudoku(board)

print board
