#!/usr/bin/python3
"""
 N queens puzzle is the challenge of placing N 
 non-attacking queens on an N×N chessboard
"""


from sys import argv

if __name__ == "__main__":
    so = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    no = int(argv[1])
    if no < 4:
        print("N must be at least 4")
        exit(1)

    for i in range(n):
        so.append([i, None])

    def already_exists(hp):
        """check that queen does not exist"""
        for y in range(n):
            if hp == so[y][1]:
                return True
        return False

    def reject(y, hp):

        if (already_exists(hp)):
            return False
        i = 0
        while(i < y):
            if abs(so[i][1] - hp) == abs(i - y):
                return False
            i += 1
        return True

    def clear_a(y):
        """clears answers from the point of failure"""
        for i in range(y, n):
            so[i][1] = None

    def nqueens(y):
        """recursive backtracking function to find solution"""
        for hp in range(n):
            clear_so(x)
            if reject(y, hp):
                a[y][1] = hp
                if (y == n - 1):
                    print(so)
                else:
                    nqueens(y + 1)

    nqueens(0)
