def matmul(m1, m2):
    type_err = 0  # to keep track of invalid inputs
    
    # checking if m1 is iterable
    for objects in m1:
        if not isinstance(objects, (list, tuple)):
            type_err += 1
            raise TypeError("Multiplication is not compatible with given objects")
    
    # checking if m2 is iterable
    for objects in m2:
        if not isinstance(objects, (list, tuple)):
            type_err += 1
            raise TypeError("Multiplication is not compatible with given objects")
    
    if type_err == 0:
        # checking if all the elements are numeric in m1 matrix
        for lists in m1:
            for element in lists:
                if not isinstance(element, (float, int, complex)):
                    type_err += 1
                    raise TypeError("Invalid input")

        # checking if all the elements are numeric in m2 matrix
        for lists in m2:
            for element in lists:
                if not isinstance(element, (float, int, complex)):
                    type_err += 1
                    raise TypeError("Invalid input")

    # if there are no type errors, we can go ahead with multiplication
    if type_err == 0:
        if len(m1[0]) != len(m2):
            raise ValueError("Multiplication is done only if the indices match")

        else:
            s = []

            # creating list inside list for storing rows of resultant matrix
            for i in range(len(m1)):
                s.append([])

                # accessing row elements of m1
                for j in range(len(m2[0])):
                    sum = 0  # initialsing sum to zero

                    # accessing column elements of m2
                    for k in range(len(m2)):
                        sum += m1[i][k] * m2[k][j]
                    s[i].append(sum)
    return s
