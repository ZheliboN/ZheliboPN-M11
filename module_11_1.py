import matplotlib.pyplot as plt
import numpy as np


# Создаём рисунок с координатной плоскостью
fig = plt.subplots()
# Создаём область, в которой будет отображаться график функции
x = np.linspace(-3, 3, 100)
# Даём заголовок для графика синусоиды
plt.title('График синусоиды')
# Даём метку оси x для графика синусоиды
plt.xlabel('Значения по оси X')
# Даём метку оси y для графика синусоиды
plt.ylabel('Y = sin(X)')
# Задаем отображение координатной сетки
plt.grid(True, which='both')
# Выделяем ось X
plt.axhline(y=0, color='r')
# Выделяем ось Y
plt.axvline(x=0, color='r')
# Вычерчиваем график функции
plt.plot(x, np.sin(x))
# показываем график
plt.show()
