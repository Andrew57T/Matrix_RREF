q = """Welcome to your matrix calculator!!
Here you can calculate a 3x3 matrix. Want to continue?
1-Yes
2-No:"""
option = 1
while option != 2:
    option = int(input(q))
    if option == 1:
        row1 = list(input("row 1:"))
        row2 = list(input("row 2:"))
        row3 = list(input("row 3:"))
        mat = row1, row2, row3
        mat = list(mat)
        print(mat)
        for n in mat:               #makes all entries integeres
             for e in n:
                x = n.index(e)
                n[x] = int(e)
        print(mat)
        if len(mat[0]) >= 4 or len(mat[1]) >=4:
            print("invalid length of rows, they should be 3.")
            continue
        if mat[0][0] != 0 or mat[1][0] != 0 or mat[2][0] != 0:
            while mat[0][0] != 1:           #make first leading number a 1 in row 1
                if mat[0][0] != 0:
                    x = mat[0][0]
                    for n in mat[0]:
                        y = mat[0].index(n)
                        mat[0][y] = n/x
                    print("we devided the first row by: ", x)
                    print(mat)
                elif mat[0][0] == 0:
                    r1 = mat[0]             #switch row1 with any other row with leading number non 0
                    for r in mat[1:]:
                        if r[0] != 0:
                            x = mat.index(r)
                            mat[0] = r
                            mat[x] = r1
                            break
                    print("we switched row 1 and row ",x+1)
                    print(mat)
        if mat[0][0] == 1 and mat[1][0] != 0 and mat[2][0] != 0:
            row2 = mat[1].copy()            #cancel all numbers from rows 2 and 3 under the leading 1 in row 1
            x = row2[0]
            row3 = mat[2].copy()
            y = row3[0]
            for k in range(len(mat[1])):
                k_i = mat[1][k]
                mat[1][k] -= mat[0][k]*x
            for l in range(len(mat[2])):
                l_i = mat[2][l]
                mat[2][l] -= mat[0][l]*y
            print("we cancled the number under the leading 1 of row 1")
            print(mat)
        if mat[1][1] != 0 or mat[2][1] != 0:
            while mat[1][1]!= 1:
                if mat[1][1] != 0:
                    x = mat[1][1]           #make first leading number a 1 in row2
                    for n in mat[1]:
                        y = mat[1].index(n)
                        mat[1][y] = n/x
                    print(" we devided the second row bby:", x)
                    print(mat)
                elif mat[1][1] == 0:        #switch row2 with any other row without leading 0
                    r2 = mat[1]
                    for r in mat[2:]:
                        if r[1] != 0:
                            x = mat.index(r)
                            mat[1] = r
                            mat[x] = r2
                            break
                    print("we switched row 2 by row ", x+1)
                    print(mat)
                continue
        if mat[1][1] == 1 and mat[2][1] != 0:
            row3 = mat[2].copy()            #cancel the number from row3 under the leading 1 in row 2
            x = row3[1]
            for k in range(len(mat[2])):
                k_i = mat[2][k]
                mat[2][k] -= mat[1][k]*x
            print("we canceled the number under the leading 1 of row 2")
            print(mat)
        if mat[2][2] != 1 and mat[2][2] != 0:
            x = mat[2][2]               #make the first leading number a 1 in row3
            for n in mat[2]:
                y = mat[2].index(n)
                mat[2][y] = n/x
            print("we devided row 3 by: ", x)
            print(mat)
        if mat[2][2] == 1:              #cancel all numbers from row 1 and 2 above the leading 1 in row 3
            row1 = mat[0].copy()
            x = row1[2]
            row2 = mat[1].copy()
            y = row2[2]
            if mat[0][2] != 0:
                for k in range(len(mat[0])):
                    k_i = mat[0][k]
                    mat[0][k] -= mat[2][k]*x
            if mat[1][2] != 0:
                for l in range(len(mat[1])):
                    l_i = mat[1][l]
                    mat[1][l] -= mat[2][l]*y
            print("we cancled the numbers above the leading 1 of row 3")
            print(mat)
        if mat[1][1] == 1 and mat[0][1] != 0:
            row1 = mat[0].copy()            #cancel the number from row1 above the leading 1 in row 2
            x = row1[1]
            for k in range(len(mat[0])):
                k_i = mat[0][k]
                mat[0][k] -= mat[1][k]*x
            print("we canceled the number above the leading 1 of row 2")
            print(mat)
        print("The final RREF of the matrix is:",mat)
    elif option == 2:
        print("Exiting...")

