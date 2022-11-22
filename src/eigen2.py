import numpy as np
import math

def copy(Matrix):
    mat = [[0 for j in range(Matrix.shape[0])] for i in range(Matrix.shape[0])]

    for i in range(Matrix.shape[0]):
        for j in range(Matrix.shape[1]):
            mat[i][j] = Matrix[i, j]

    return mat



def normalize(vector):
    length = 0
    for i in range(vector.size):
        length += (vector[i] ** 2)
    
    length = math.sqrt(length)

    resVector = np.array([])
    
    for i in range(vector.size):
        resVector = np.append(resVector, (vector[i] / length))

    return resVector



def qrDecomp(Matrix):
    a = np.array(np.transpose(Matrix))
    u = np.array([])
    e = np.array([])

    # Gram-Schmidt Procedure
    u = np.append(u, a[0])              # u1
    e = np.append(e, normalize(a[0]))   # e1

    # For un and en, n > 1
    u = np.array([u])
    e = np.array([e])

    for i in range(1, a.shape[0]):
        temp = a[i]
        for j in range(i):
            temp = np.subtract(temp, np.dot(a[i], e[j]) * e[j])
        u = np.vstack([u, temp])
        e = np.vstack([e, normalize(u[i])])

    # Q and R matrices
    Q = np.zeros(shape=(Matrix.shape[0], Matrix.shape[0]))
    R = np.zeros(shape=(Matrix.shape[0], Matrix.shape[0]))

    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            Q[j, i] = e[i, j]

    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            if(i <= j):
                R[i, j] = np.dot(a[j], e[i])

    return (Q, R)



def eigenValue(Matrix): # Note : Call eigenValue(Matrix)[0] to return only the eigenvalues
    eigenVal = np.array([])

    # Create Identity Matrix
    QQ = np.eye(Matrix.shape[0])

    # Matrix will converge as iteration approaches infinity (large number in practice)
    for i in range(10):
        Q, R = qrDecomp(Matrix)
        Matrix = np.matmul(R, Q)
        QQ = np.matmul(QQ, Q)

    for i in range(len(Matrix)):
        eigenVal = np.append(eigenVal, Matrix[i, i])

    return (eigenVal, QQ)



def eigenVector(Matrix):
    return eigenValue(Matrix)[1]






# TESTS
# Samples
# a = np.array([[1, 1, 0], 
#      [1, 0, 1], 
#      [0, 1, 1]])

# b = np.array([[3, 0],
#     [8, -1]])


# c= np.array([[10, 0, 2],
#    [0, 10, 4],
#    [2, 4, 2]])

# d = np.array([[24294.3, 23763.3, -22564, -27522, 2028.72],         
#     [23763.3, 37215.3, -26584, -31211, -3183.3],         
#     [-22564, -26584, 32686.9, 25780.3, -9319.5],       
#     [-27522, -31211, 25780.3, 45872.7, -12919],       
#     [2028.72, -3183.3, -9319.5, -12919, 23393.1]])

# e = np.array([[2, 1, 0],
#     [1, 2, 0],
#     [0, 0, 3],])

# f = np.array([[1, 1, 1, 1, 1],
#     [16, 8, 4, 2, 1],
#     [81, 27, 9, 3, 1],
#     [256, 64, 16, 4, 1],
#     [625, 125, 25, 5, 1]])



# Eigen Values
# print("Test Eigen Values :")
# print("Eigen Value Matriks a: ", eigenValue(a)[0])
# print("Eigen Value Matriks b: ", eigenValue(b)[0])
# print("Eigen Value Matriks c: ", eigenValue(c)[0])
# print("Eigen Value Matriks d: ", eigenValue(d)[0])
# print("Eigen Value Matriks e: ", eigenValue(e)[0])
# print("Eigen Value Matriks f: ", eigenValue(f)[0], '\n')



# Eigen Vectors
# print("Test Eigen Values :")
# print("Eigen Vector Matriks b:\n", (eigenVector(b)), '\n')
# print("Eigen Vector Matriks d:\n", (eigenVector(d)), '\n')

# print(eigenVector(np.random.rand(256, 256)))