import time

#Floating point tolerance
EPSILON = 1e-10


def print_matrix(matrix):
    """Print a matrix with readable values rounded to two decimal places."""
    for row in matrix:
        formatted_row = [f"{value:.2f}" for value in row]
        print(f"[{', '.join(formatted_row)}]")


def rref(matrix):
    """Return the reduced row-echelon form of a matrix, showing each operation."""

    #make a copy of the matrix
    result = []
    for row in matrix:
        result.append(row[:])


    row_count = len(result)
    if row_count != 0:
        column_count = len(result[0])
    else:
        column_count = 0
    pivot_row = 0

    for pivot_column in range(column_count):
        if pivot_row >= row_count:
            break

        #finds the max value in the pivot column
        pivot = max(
            range(pivot_row, row_count),
            key=lambda row_index: abs(result[row_index][pivot_column]),)

        #skips the collumn if the largest pivot is a zero (column of zeros)
        if abs(result[pivot][pivot_column]) <= EPSILON:
            continue

        #if the pivot found is not in the pivot row, swap the two rows
        if pivot != pivot_row:
            result[pivot_row], result[pivot] = result[pivot], result[pivot_row]
            print(
                f"\nSwap row {pivot_row + 1} with row {pivot + 1}:"
            )
            print_matrix(result)

        pivot_value = result[pivot_row][pivot_column]
        
        for column_index in range(column_count):
            result[pivot_row][column_index] /= pivot_value
        print(
            f"\nNormalize row {pivot_row + 1} using pivot column "
            f"{pivot_column + 1}:"
        )
        print_matrix(result)

        for row_index in range(row_count):
            if row_index == pivot_row:
                continue
            factor = result[row_index][pivot_column]
            if abs(factor) <= EPSILON:
                continue
            for column_index in range(column_count):
                result[row_index][column_index] -= factor * result[pivot_row][column_index]
            print(
                f"\nNormalize pivot column {pivot_column + 1} by clearing "
                f"row {row_index + 1}:"
            )
            print_matrix(result)

        pivot_row += 1

    for row in result:
        for column_index, value in enumerate(row):
            if abs(value) <= EPSILON:
                row[column_index] = 0.0
            elif abs(value - 1.0) <= EPSILON:
                row[column_index] = 1.0

    return result


def read_matrix(size):
    matrix = []
    while len(matrix) < size:
        row_number = len(matrix) + 1
        values = input(f"Row {row_number}: ").split()
        if len(values) != size:
            print(f"Please enter exactly {size} values.")
            continue
        try:
            matrix.append([float(value) for value in values])
        except ValueError:
            print("Every matrix entry must be a number.")
    return matrix


def main():
    prompt = """Welcome to your matrix calculator!!
Here you can calculate any size square matrix. Want to continue?
1-Yes
2-No: """

    while True:
        try:
            option = int(input(prompt))
        except ValueError:
            print("Please enter 1 or 2.")
            continue

        if option == 2:
            print("Exiting...")
            return
        if option != 1:
            print("Please enter 1 or 2.")
            continue

        try:
            size = int(input("How big is your square matrix? "))
        except ValueError:
            print("Matrix size must be a positive integer.")
            continue
        if size <= 0:
            print("Matrix size must be a positive integer.")
            continue

        matrix = read_matrix(size)
        print("\nStarting matrix:")
        print_matrix(matrix)
        start = time.time()
        reduced_matrix = rref(matrix)
        print("\nFinal RREF:")
        print_matrix(reduced_matrix)
        print("Execution time:", time.time() - start, "seconds")


if __name__ == "__main__":
    main()
