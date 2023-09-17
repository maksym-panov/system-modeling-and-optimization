import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# 1.2.1 - Числові вектори
a = np.array([1, 2, 3, 4, 5])
print("Вектор:\n", a, "\n")

print("Конкатенація:\n", np.append([1, 2, 3, 4, 5], np.append(6, [7, 8])), "\n")

print("Генерація послідовностей:\n", np.arange(0, 1 + 0.1, 0.1), "\n")

print("Копіювання вектора:\n", np.tile(np.array([1, 2]), 3), "\n")

x = np.array([0, math.pi / 2, math.pi])
print("Виконання функцій над векторами:\n", np.sin(x), "\n")

# 1.2.3 - Матриці
print("Матриця (за стовпцями):\n", np.reshape((1, 2, 3, 4, 5, 6), (2, 3), order = "F"), "\n")
print("Одинична матриця:\n", np.ones((2, 2)), "\n")
print("Матриця (за стовпцями):\n", np.reshape((1, 2, 1, 2, 1, 2), (3, 2), order = "F"), "\n")
print("Матриця (за рядками):\n", np.reshape((1, 2, 3, 4, 5, 6), (2, 3)), "\n")

column_names = ["length", "width"]
row_names = ["petal", "sepal"]

matrix = np.reshape((23, 31, 58, 16), (2, 2), order = "F")
df = pd.DataFrame(matrix, columns = column_names, index = row_names);
print("Матриця з іменованими стовпцями та рядками:\n", df, "\n")

A = np.reshape([i for i in range(1, 7)], (2, 3), order = "F")
print("Матриця А:\n", A, "\n")

B = A.transpose()
print("Матриця В - транспонована А:\n", B, "\n")

print("А * B\n", A.dot(B), "\n")
print("B * A\n", B.dot(A), "\n")

A = np.reshape([i for i in range(1, 5)], (2, 2), order = "F")
b = np.array([5, 8])
print("Матриця коефіцієнтів перед змінними\n", A, "\n")
print("Матриця вільних членів\n", b, "\n")

print("Розвʼязок рівняння\n", np.linalg.solve(A, b), "\n")
print("Визначник матриці А\n", np.linalg.det(A), "\n")
print("Матриця, обернена до А\n", np.linalg.inv(A), "\n")

# 1.2.4 - Графіки
x = np.linspace(start = -math.pi, stop = math.pi, num = 30)
y = np.sin(x)

plt.plot(x, y, "ko")
plt.show()

plt.plot(x, y, "b")
plt.title("Sine of x")
plt.show()

x = np.arange(start = -10, stop = 10, step = 0.1)
y1 = x**2 + 2*x - 5
y2 = -x**2 + 60

plt.plot(x, y1, "r")
plt.plot(x, y2, "g", linestyle = "dashed")
plt.legend(["y1", "y2"])
plt.ylim(bottom = -10, top = 100)
plt.title("Графіки функцій")
plt.show()