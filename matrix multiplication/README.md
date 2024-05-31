# MATRIX MULTIPLICATION

## Limitations of matrix multiplication

For testing matrix multiplication, we can think of following test cases:

- If the input is *not numeric*, this should raise `TypeError`
- If the no. of columns of first matrix *doesn't match* with no. of rows of second matrix, matrix multiplication is not compatile, this  should raise `ValueError`
- If the given inputs are *non-matrices*, this should raise `TypeError`
- If no. of elements are not matched in each list/tuple, it should raise `IndexError`

## Approach

### Tackling errors

- _Non-Matrices_ : I have used isinsatnce to check if the inputs are of iterable type, it can be list, tuple. I have used for loop to check for inside the list/tuple. Once non-list/tuple is encountered, it raises `TypeError`.

- _Non-Numeric_ : After making sure that entries are matrices, I have used isinstance to check if the inputs given are either intergers or float or complex. I have used for loops to check for each element. Once non-numeric element is encountered, it raises `TypeError`.

- _Axes Mismatch_ : I have checked, if no. of column of first matrix are same as the no. of rows of second matrix. If not, it raises `ValueError`.

### Algorithm

If there are no errors are raised, matrix multiplication is carried out:

   First, I have created an *empty list* to store the resultanat matrix. It multiplies elements of 1st row of 1st matrix with 1st column of 2nd matrix, respectively and added them. Initialised sum back to zero, and same process is continued for all columns. This gives us the first row of resultant matrix. Similarly, its done for other rows of first matrix and resultant matrix is obatined.
    
   I have used *for* loops for this process. First one to create lists inside list for each row in the resultant matrix. One to loop through elements of rows in first matrix and the other one to go through columns in the second matrix.
   
   Checking for non-matrices, non-numeric values in first ensures that we have valid matrix entries. Only then it proceeds with matrix multiplication.