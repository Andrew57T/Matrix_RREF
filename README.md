# Matrix RREF Calculator

A simple Python command-line program that computes the Reduced Row Echelon Form (RREF) of a matrix using Gauss-Jordan elimination.

## What this program does

This program lets you:

- enter a square matrix interactively
- convert it to reduced row-echelon form
- follow each row operation as the matrix is reduced
- display the resulting matrix in simplified form
- measure how long the calculation took

It is useful for solving systems of linear equations, checking linear dependence, and understanding matrix structure.

## Features

- Accepts a matrix size entered by the user
- Reads each row as space-separated values
- Supports numeric input including decimal values
- Uses a floating-point tolerance to avoid tiny numerical noise near zero or one
- Prints the modified matrix after every row swap, pivot-row normalization, and pivot-column clearing step
- Prints the final reduced matrix and runtime

## Requirements

- Python 3

## Running the program

From the project directory, run:

```bash
python main.py
```

## How to use it

When you start the script, you will be prompted with:

```text
Welcome to your matrix calculator!!
Here you can calculate any size square matrix. Want to continue?
1-Yes
2-No:
```

Choose:

- `1` to continue
- `2` to exit the program

Then enter the size of your matrix. For example, if you want a 2x2 matrix, enter:

```text
2
```

Next, enter each row of the matrix as space-separated numbers. For example:

```text
1 2
3 4
```

The program will print:

- the matrix you entered
- the modified matrix after each row swap and normalization step
- the matrix in RREF
- the execution time in seconds

## Example

Example session:

```text
Welcome to your matrix calculator!!
Here you can calculate any size square matrix. Want to continue?
1-Yes
2-No: 1
How big is your square matrix? 2
Row 1: 1 2
Row 2: 3 4

Swap row 1 with row 2:
[3.0, 4.0]
[1.0, 2.0]

Normalize row 1 using pivot column 1:
[1.0, 1.3333333333333333]
[1.0, 2.0]

Normalize pivot column 1 by clearing row 2:
[1.0, 1.3333333333333333]
[0.0, 0.6666666666666667]

...

Final RREF:
[1.0, 0.0]
[0.0, 1.0]
Execution time: 0.000123 seconds
```

For the matrix

```text
[1 2]
[3 4]
```

its reduced row-echelon form is the identity matrix:

```text
[1 0]
[0 1]
```

## Notes

- The matrix must be square, meaning the number of rows equals the number of columns.
- This implementation uses a tolerance (`EPSILON = 1e-10`) so values extremely close to 0 or 1 are normalized cleanly.
- The algorithm is based on Gauss-Jordan elimination, which systematically creates pivots and eliminates all other entries in each column.

## Project files

- `main.py` — contains the matrix logic and command-line interface
- `README.md` — this documentation
