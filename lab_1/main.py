"""
Первая лабораторная: задания 1-6.
1. Работа с изображениями.
Выбрать язык программирования и библиотеку для записи изображений в файл.

Создать матрицу размера H*W, заполнить её элементы нулевыми
значениями, сохранить в виде полутонового (одноканального) 8-битового
изображения высотой H и шириной W, убедиться, что полученное
изображение открывается средствами операционной системы и полностью чёрное.

Создать матрицу размера H*W, заполнить её элементы значениями, равными
255, сохранить в виде полутонового (одноканального) 8-битового
изображения высотой H и шириной W, убедиться, что полученное
изображение открывается средствами операционной системы и полностью
белое.

Создать матрицу размера H*W*3, заполнить её элементы значениями,
равными (255, 0, 0), сохранить в виде цветного (трёхканального) 8-битового
изображения высотой H и шириной W, убедиться, что полученное
изображение открывается средствами операционной системы и полностью
красное.
Создать матрицу размера H*W*3, заполнить её элементы произвольными
значениями по выбранной схеме (например, значение элемента равно сумме
его координат по модулю 256), сохранить в виде 8-битового изображения
высотой H и шириной W, убедиться, что полученное изображение
открывается средствами операционной системы (в предложенном примере
должен получиться плавный градиент от чёрного цвета в верхнем левом углу
изображения).

2. Отрисовка прямых линий
Реализовать все описанные в лекциях алгоритмы отрисовки прямых (до
алгоритма Брезенхема включительно).
Для каждого алгоритма сохранить в файл изображение размера 200х200 с
нарисованной на нём «звездой» (см. лекции).
Подсказка:
начальная координата (100,100)
конечная координата (100 + 95 𝑐𝑜𝑠 (𝛼) , 100 + 95 𝑠𝑖𝑛 (𝛼) ), 𝛼 =
2𝜋𝑖
13
, 𝑖 = 0,1, … , 12.

3. Работа с трёхмерной моделью (вершины)
Считать из приложенного файла obj строки, содержащие информацию о
вершинах модели в объект созданного класса:
v X1 Y1 Z1
v X2 Y2 Z2
<…>
4. Отрисовка вершин трёхмерной модели
Нарисовать вершины модели (игнорируя координату Z) на изображении
размером (1000, 1000).
Для того, чтобы модель была видна на изображении (и не была слишком
большой), поэкспериментируйте с масштабированием и смещением
координат точек, например:
[50 * X + 500, 50 * Y + 500]

5. Работа с трёхмерной моделью (полигоны)
Считать из приложенного файла строки, содержащие информацию о
полигонах модели.
Сведения о полигонах в файле хранятся в формате:
f v1/vt1/vn1 v2/vt2/vn2 v3/vt3/vn3
В рамках лабораторной загрузить в память необходимо только первые
значения в каждой тройке – номера вершин, загруженных ранее.
Обратите внимание, что вершины нумеруются, начиная с единицы.
6. Отрисовка рёбер трёхмерной модели
Отрисовать все рёбра всех полигонов модели с помощью алгоритма
Брезенхема (координаты вершин округляем до ближайшего целого).

"""
import numpy as np
from PIL import Image


def task_1():
    height, width = 500, 500

    matrix_white = np.zeros((height, width), dtype=np.uint8)
    image_black = Image.fromarray(matrix_white)
    image_black.save('black_rect.png')

    matrix_white = np.full(shape=(height, width), fill_value=255, dtype=np.uint8)
    image_black = Image.fromarray(matrix_white)
    image_black.save('white_rect.png')

    matrix_red = np.full(shape=(height, width, 3),
                         fill_value=(255, 0, 0),
                         dtype=np.uint8)
    image_red = Image.fromarray(matrix_red)
    image_red.save('red_rect.png')

    matrix_gradient = np.array([[((i + j) % 256, (i - j) % 256, i % 256)
                                 for i in range(height)]
                                for j in range(width)],
                               dtype=np.uint8)
    image_gradient = Image.fromarray(matrix_gradient)
    image_gradient.save('gradient_rect.png')


def task_2():
    pass


if __name__ == '__main__':
    task_1()
    # task_2()
