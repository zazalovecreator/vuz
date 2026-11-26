matrix = [[9, 0, 0, 3, 1, 0, 1],
          [0, 11, 2, 1, 0, 0, 2],
          [0, 1, 10, 2, 0, 0 ,0],
          [2, 1, 2, 9, 1, 0, 0],
          [1, 0, 0, 1, 12, 0, 1],
          [0, 0, 0, 0, 0, 8, 0],
          [2, 2, 0, 0, 3, 0, 8]]

def a(matrix):
    lst=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0: lst.append(matrix[i][j])
    return lst

def b(matrix):
    lst=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0: lst.append(j+1)
    return lst

def c(matrix):
    lst=[]
    count=1
    lst.append(count)
    for i in matrix:
        for j in range(len(matrix[0])):
            if i[j]!=0: count+=1
        lst.append(count)
    return lst


def to_matrix(a, b, c):
    lst = []
    for i in range(len(c) - 1):
        line = [0] * (len(c) - 1)
        for z in range(c[i] - 1, c[i + 1] - 1):
            line[b[z] - 1] = a[z]
        lst.append(line)
    return lst

def matrix_view(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(str(matrix[i][j]).ljust(2), end = ' ')
        print()

print(a(matrix))
print(b(matrix))
print(c(matrix))

print(matrix_view(to_matrix(a(matrix), b(matrix), c(matrix))))

print([0] * (len(c(matrix)) - 1))