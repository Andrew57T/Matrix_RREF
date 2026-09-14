q = """Welcome to your matrix calculator!!
Here you can calculate a 2x2 matrix. Want to continue?
1-Yes
2-No:"""
option = 1
while option != 2:
    option = int(input(q))
    if option == 1:
        row1 = list(input("row 1:"))
        row2 = list(input("row 2:"))
        mat = row1, row2
        mat = list(mat)
        print(mat)
        for n in mat:
            for e in n:
                x = n.index(e)
                n[x] = int(e)
        print(mat)
        if len(mat[0]) >= 3 or len(mat[1]) >=3:
            print("invalid length of rows, they should be 2.")
            continue

        while mat[0][0] != 1:
            if mat[0][0] != 1 or 0:
                x = mat[0][0]
                mat[0][0] = mat[0][0]/x
                mat[0][1] = mat[0][1]/x
                print("we devided the first row by: ", x)
                print(mat)
            elif mat[0][0] == 0:
                a00 = mat[0][0]
                a01 = mat[0][1]
                a10 = mat[1][0]
                a11 = mat[1][1]
                mat[0][0] = a10
                mat[0][1] = a11
                mat[1][0] = a00
                mat[1][1] = a01
                print("we switched row 1 and row 2.")
                print(mat)
        if mat[0][0] == 1 and mat[1][0] != 0:
            x = mat[1][0]
            mat[1][0] -= mat[0][0]*x
            mat[1][1] -= mat[0][1]*x
            print("we cancled the number under the leading 1")
            print(mat)
        if mat[1][1] != 1 and mat[1][1] != 0:
            x = mat[1][1]
            mat[1][1] = mat[1][1]/x
            print("we devided row 2 by:",x)
            print(mat)
        if mat[1][1] == 1:
            mat[0][1] -= mat[0][1]*mat[1][1]
            print("we canceled the number above the leading 1 in the second row.")
        print("The final RREF of the matrix is:",mat)
    elif option == 2:
        print("Exiting...")
