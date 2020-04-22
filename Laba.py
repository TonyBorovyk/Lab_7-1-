import sys


def create_matrix_sumizh():
    file = open('File.txt')
    info = file.readline()
    info_size = info.split(" ")
    if ((int(info_size[0]) == 0) and (int(info_size[1]) == 0)) or (int(info_size[0]) == 0):
        sys.exit("Помилка! Оскільки кількість вершин дорівнює нулю!")
    else:
        matrix_sumizh = [[0] * int(info_size[0]) for x in range(int(info_size[0]))]
        for i in range(int(info_size[1])):
            info_versh = file.readline()
            info_versh_arr = info_versh.split(" ")
            matrix_sumizh[int(info_versh_arr[0]) - 1][int(info_versh_arr[1]) - 1] = 1
            matrix_sumizh[int(info_versh_arr[1]) - 1][int(info_versh_arr[0]) - 1] = 1
        file.close()
        return matrix_sumizh


def create_matrix_array():
    file = open('File.txt')
    info = file.readline()
    info_size = info.split(" ")
    if ((int(info_size[0]) == 0) and (int(info_size[1]) == 0)) or (int(info_size[0]) == 0):
        sys.exit("Помилка! Оскільки кількість вершин дорівнює нулю!")
    else:
        matrix_sumizh = []
        for i in range(int(info_size[1])):
            arr = []
            info_versh = file.readline()
            info_versh_arr = info_versh.split(" ")
            arr.append(int(info_versh_arr[0]))
            arr.append(int(info_versh_arr[1]))
            matrix_sumizh.append(arr)
        file.close()

        return matrix_sumizh


def step(matrix):
    array = []
    for y in range(len(matrix) - 2):
        arr = []
        for i in range(len(matrix)):
            count = 0
            for j in range(len(matrix)):
                if matrix[i][j] == 1:
                    count += 1
            arr.append(count)
        t = 0
        for x in range(len(matrix)):
            if arr[x] == 1 and t == 0:
                ind = x
                array.append(x + 1)
                arr[x] = 0
                t += 1
                for l in range(len(matrix)):
                    matrix[l][ind] = 0
                    matrix[ind][l] = 0
    return array


def output_Matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print("%4d" % matrix[i][j], end=' ')
        print()


def output(array, matrix):
    size = len(array)
    for x in range(size):
        t = 0
        for i in range(len(matrix)):
            if array[x] == matrix[i][0] and t == 0:
                t += 1
                array[x] = matrix[i][1]
                matrix[i][1] = 0
                matrix[i][0] = 0
            elif array[x] == matrix[i][1] and t == 0:
                t += 1
                array[x] = matrix[i][0]
                matrix[i][1] = 0
                matrix[i][0] = 0
        size -= 1

    print("За даним деревом код Прюфера має вигляд: ", array)


def Part_2():
    array_1 = []
    array_main = []
    points = str(input("Ввеідть код Прюфера: "))
    p = points.split(" ")
    for i in range(len(p)):
        array_1.append(int(p[i]))
    for i in range(len(p) + 2):
        array_main.append(i + 1)

    matrix_sumizh = [[0] * len(array_main) for x in range(len(array_main))]
    for k in range(len(array_1)):
        arr = []
        for i in array_main:
            if i not in array_1:
                arr.append(i)
        v = min(arr)
        matrix_sumizh[v - 1][array_1[0] - 1] = 1
        matrix_sumizh[array_1[0] - 1][v - 1] = 1
        array_main.remove(v)
        del array_1[0]
    matrix_sumizh[array_main[0] - 1][array_main[1] - 1] = 1
    matrix_sumizh[array_main[1] - 1][array_main[0] - 1] = 1

    return matrix_sumizh


matr = create_matrix_sumizh()
matr1 = create_matrix_array()
question = int(input("Введіть (1) щоб розв'язати задачу побудови Прюфера або (2) щоб побудувати дерево\
                              (Матрицю суміжності) з коду Прюфера: "))
if question == 1:
    array = step(matr)
    output(array, matr1)
elif question == 2:
    matrix = Part_2()
    output_Matrix(matrix)
else:
    print("Помилка!")
