# Вариант 21. Решение задач по функциям нескольких переменных

## Дано

По условиям варианта 21 требуется выполнить пять заданий:

1. Вычислить частные производные первого порядка.
2. Проверить равенство смешанных производных второго порядка.
3. Вычислить производную по направлению.
4. Выписать уравнение касательной плоскости и нормали к поверхности.
5. Исследовать функцию на экстремум.

---

## №1. Частные производные первого порядка

Дана функция

$$
z=\frac{\cos y}{\sqrt{\ln\left(x^2+y-9\right)}}.
$$

Обозначим

$$
S=x^2+y-9, \qquad L=\ln S.
$$

Тогда функцию можно записать так:

$$
z=\cos y \cdot L^{-\frac12}.
$$

Область определения функции задается условием

$$
\ln(x^2+y-9)>0,
$$

то есть

$$
x^2+y-9>1,
$$

следовательно,

$$
x^2+y>10.
$$

### Производная по $x$

При нахождении частной производной по $x$ переменная $y$ считается постоянной:

$$
\frac{\partial z}{\partial x}
=\cos y \cdot \frac{\partial}{\partial x}\left(L^{-\frac12}\right).
$$

Используем правило дифференцирования сложной функции:

$$
\frac{\partial}{\partial x}\left(L^{-\frac12}\right)
=-\frac12 L^{-\frac32}\cdot \frac{\partial L}{\partial x}.
$$

Так как

$$
L=\ln(x^2+y-9),
$$

то

$$
\frac{\partial L}{\partial x}
=\frac{2x}{x^2+y-9}.
$$

Получаем:

$$
\frac{\partial z}{\partial x}
=\cos y \cdot \left(-\frac12\right)
\left(\ln(x^2+y-9)\right)^{-\frac32}
\cdot \frac{2x}{x^2+y-9}.
$$

После сокращения:

$$
\boxed{
\frac{\partial z}{\partial x}
=-\frac{x\cos y}{(x^2+y-9)\left(\ln(x^2+y-9)\right)^{\frac32}}
}
$$

### Производная по $y$

Теперь считаем $x$ постоянной величиной:

$$
z=\cos y \cdot L^{-\frac12}.
$$

Применяем правило производной произведения:

$$
\frac{\partial z}{\partial y}
=(\cos y)'_y \cdot L^{-\frac12}
+\cos y \cdot \frac{\partial}{\partial y}\left(L^{-\frac12}\right).
$$

Первая часть:

$$
(\cos y)'_y=-\sin y.
$$

Вторая часть:

$$
\frac{\partial}{\partial y}\left(L^{-\frac12}\right)
=-\frac12L^{-\frac32}\cdot \frac{\partial L}{\partial y}.
$$

Так как

$$
\frac{\partial L}{\partial y}
=\frac{1}{x^2+y-9},
$$

то

$$
\frac{\partial z}{\partial y}
=-\sin y \cdot L^{-\frac12}
-\frac{\cos y}{2(x^2+y-9)L^{\frac32}}.
$$

Итог:

$$
\boxed{
\frac{\partial z}{\partial y}
=-\frac{\sin y}{\sqrt{\ln(x^2+y-9)}}
-\frac{\cos y}{2(x^2+y-9)\left(\ln(x^2+y-9)\right)^{\frac32}}
}
$$

---

## №2. Проверка равенства смешанных производных второго порядка

Дана функция

$$
z=e^{\frac{x}{y}}-\operatorname{arctg}(5y^2+2y).
$$

Нужно проверить равенство

$$
\frac{\partial^2 z}{\partial y\partial x}
=
\frac{\partial^2 z}{\partial x\partial y}.
$$

### Находим первую производную по $x$

При дифференцировании по $x$ переменная $y$ считается постоянной:

$$
\frac{\partial z}{\partial x}
=\frac{\partial}{\partial x}\left(e^{\frac{x}{y}}\right)
-
\frac{\partial}{\partial x}\left(\operatorname{arctg}(5y^2+2y)\right).
$$

Второе слагаемое не зависит от $x$, поэтому его производная равна нулю:

$$
\frac{\partial z}{\partial x}
=e^{\frac{x}{y}}\cdot \frac1y.
$$

То есть

$$
\frac{\partial z}{\partial x}=\frac{1}{y}e^{\frac{x}{y}}.
$$

Теперь находим смешанную производную:

$$
\frac{\partial^2 z}{\partial y\partial x}
=\frac{\partial}{\partial y}\left(\frac{1}{y}e^{\frac{x}{y}}\right).
$$

Применяем правило производной произведения:

$$
\frac{\partial}{\partial y}\left(\frac{1}{y}e^{\frac{x}{y}}\right)
=\left(\frac1y\right)'_y e^{\frac{x}{y}}
+rac1y\left(e^{\frac{x}{y}}\right)'_y.
$$

Имеем:

$$
\left(\frac1y\right)'_y=-\frac1{y^2},
$$

а также

$$
\left(e^{\frac{x}{y}}\right)'_y
=e^{\frac{x}{y}}\cdot \left(\frac{x}{y}\right)'_y
=e^{\frac{x}{y}}\cdot \left(-\frac{x}{y^2}\right).
$$

Тогда

$$
\frac{\partial^2 z}{\partial y\partial x}
=-\frac1{y^2}e^{\frac{x}{y}}
+rac1y e^{\frac{x}{y}}\left(-\frac{x}{y^2}\right).
$$

Получаем:

$$
\boxed{
\frac{\partial^2 z}{\partial y\partial x}
=-\frac{e^{\frac{x}{y}}}{y^2}
-rac{x e^{\frac{x}{y}}}{y^3}
=-\frac{(x+y)e^{\frac{x}{y}}}{y^3}
}
$$

### Находим первую производную по $y$

Теперь дифференцируем исходную функцию по $y$:

$$
z=e^{\frac{x}{y}}-\operatorname{arctg}(5y^2+2y).
$$

Первая часть:

$$
\frac{\partial}{\partial y}\left(e^{\frac{x}{y}}\right)
=e^{\frac{x}{y}}\cdot \left(-\frac{x}{y^2}\right).
$$

Вторая часть:

$$
\frac{\partial}{\partial y}\left(\operatorname{arctg}(5y^2+2y)\right)
=\frac{10y+2}{1+(5y^2+2y)^2}.
$$

Следовательно,

$$
\frac{\partial z}{\partial y}
=-\frac{x}{y^2}e^{\frac{x}{y}}
-rac{10y+2}{1+(5y^2+2y)^2}.
$$

Теперь находим смешанную производную по $x$:

$$
\frac{\partial^2 z}{\partial x\partial y}
=rac{\partial}{\partial x}\left(
-\frac{x}{y^2}e^{\frac{x}{y}}
-rac{10y+2}{1+(5y^2+2y)^2}
\right).
$$

Второе слагаемое не зависит от $x$, значит его производная по $x$ равна нулю.

Остается:

$$
\frac{\partial^2 z}{\partial x\partial y}
=\frac{\partial}{\partial x}\left(-\frac{x}{y^2}e^{\frac{x}{y}}\right).
$$

Так как $y$ считается постоянной:

$$
\frac{\partial^2 z}{\partial x\partial y}
=-\frac1{y^2}e^{\frac{x}{y}}
-rac{x}{y^2}e^{\frac{x}{y}}\cdot \frac1y.
$$

Получаем:

$$
\boxed{
\frac{\partial^2 z}{\partial x\partial y}
=-\frac{e^{\frac{x}{y}}}{y^2}
-rac{x e^{\frac{x}{y}}}{y^3}
=-\frac{(x+y)e^{\frac{x}{y}}}{y^3}
}
$$

### Вывод

Так как

$$
\frac{\partial^2 z}{\partial y\partial x}
=
\frac{\partial^2 z}{\partial x\partial y}
=-\frac{(x+y)e^{\frac{x}{y}}}{y^3},
$$

то смешанные производные второго порядка равны:

$$
\boxed{
\frac{\partial^2 z}{\partial y\partial x}
=
\frac{\partial^2 z}{\partial x\partial y}
}
$$

---

## №3. Производная по направлению

Дана функция

$$
u=xy+\sqrt z+4zx,
$$

точки

$$
A(1;2;1), \qquad B(-1;0;0).
$$

Так как вариант 21 нечетный, производную нужно найти в направлении вектора $\overrightarrow{AB}$.

### Находим вектор направления

$$
\overrightarrow{AB}=B-A.
$$

Подставляем координаты:

$$
\overrightarrow{AB}=(-1-1;\,0-2;\,0-1)=(-2;-2;-1).
$$

Длина этого вектора:

$$
|\overrightarrow{AB}|
=\sqrt{(-2)^2+(-2)^2+(-1)^2}
=\sqrt{4+4+1}=3.
$$

Единичный вектор направления:

$$
\vec e=\frac{\overrightarrow{AB}}{|\overrightarrow{AB}|}
=\left(-\frac23;-\frac23;-\frac13\right).
$$

### Находим градиент функции

Производная по направлению вычисляется как скалярное произведение градиента функции на единичный вектор направления:

$$
\frac{\partial u}{\partial l}=\operatorname{grad}u(A)\cdot \vec e.
$$

Найдем частные производные:

$$
\frac{\partial u}{\partial x}=y+4z,
$$

$$
\frac{\partial u}{\partial y}=x,
$$

$$
\frac{\partial u}{\partial z}=\frac{1}{2\sqrt z}+4x.
$$

В точке $A(1;2;1)$:

$$
\frac{\partial u}{\partial x}(A)=2+4\cdot1=6,
$$

$$
\frac{\partial u}{\partial y}(A)=1,
$$

$$
\frac{\partial u}{\partial z}(A)=\frac{1}{2\sqrt1}+4\cdot1=\frac12+4=\frac92.
$$

Значит,

$$
\operatorname{grad}u(A)=\left(6;1;\frac92\right).
$$

### Вычисляем производную по направлению

$$
\frac{\partial u}{\partial l}
=\left(6;1;\frac92\right)
\cdot
\left(-\frac23;-\frac23;-\frac13\right).
$$

Раскрываем скалярное произведение:

$$
\frac{\partial u}{\partial l}
=6\left(-\frac23\right)
+1\left(-\frac23\right)
+\frac92\left(-\frac13\right).
$$

$$
\frac{\partial u}{\partial l}
=-4-\frac23-\frac32.
$$

Приведем к общему знаменателю:

$$
-4-\frac23-\frac32
=-\frac{24}{6}-\frac46-\frac96
=-\frac{37}{6}.
$$

Ответ:

$$
\boxed{
\frac{\partial u}{\partial l}=-\frac{37}{6}
}
$$

---

## №4. Касательная плоскость и нормаль к поверхности

Дана поверхность

$$
\frac{x^2}{9}+\frac{y^2}{25}-\frac{z^2}{225}=0,
$$

и точка

$$
A(\sqrt3;\sqrt5;2\sqrt{30}).
$$

Обозначим поверхность как неявно заданную функцию:

$$
F(x,y,z)=\frac{x^2}{9}+\frac{y^2}{25}-\frac{z^2}{225}.
$$

Тогда касательная плоскость к поверхности $F(x,y,z)=0$ в точке $A(x_0;y_0;z_0)$ задается формулой

$$
F_x(A)(x-x_0)+F_y(A)(y-y_0)+F_z(A)(z-z_0)=0.
$$

### Проверим, что точка принадлежит поверхности

Подставим координаты точки:

$$
\frac{(\sqrt3)^2}{9}+\frac{(\sqrt5)^2}{25}
-\frac{(2\sqrt{30})^2}{225}
=\frac3{9}+\frac5{25}-\frac{120}{225}.
$$

$$
\frac3{9}+\frac5{25}-\frac{120}{225}
=\frac13+\frac15-\frac8{15}
=\frac5{15}+\frac3{15}-\frac8{15}=0.
$$

Точка действительно лежит на поверхности.

### Находим частные производные функции $F$

$$
F_x=\frac{2x}{9},
$$

$$
F_y=\frac{2y}{25},
$$

$$
F_z=-\frac{2z}{225}.
$$

В точке $A(\sqrt3;\sqrt5;2\sqrt{30})$:

$$
F_x(A)=\frac{2\sqrt3}{9},
$$

$$
F_y(A)=\frac{2\sqrt5}{25},
$$

$$
F_z(A)=-\frac{4\sqrt{30}}{225}.
$$

### Уравнение касательной плоскости

Подставляем в формулу:

$$
\frac{2\sqrt3}{9}(x-\sqrt3)
+rac{2\sqrt5}{25}(y-\sqrt5)
-rac{4\sqrt{30}}{225}(z-2\sqrt{30})=0.
$$

Умножим уравнение на $\dfrac{225}{2}$:

$$
25\sqrt3(x-\sqrt3)
+9\sqrt5(y-\sqrt5)
-2\sqrt{30}(z-2\sqrt{30})=0.
$$

Раскроем скобки:

$$
25\sqrt3x-75+9\sqrt5y-45-2\sqrt{30}z+120=0.
$$

Постоянные слагаемые сокращаются:

$$
-75-45+120=0.
$$

Получаем уравнение касательной плоскости:

$$
\boxed{
25\sqrt3x+9\sqrt5y-2\sqrt{30}z=0
}
$$

### Уравнение нормали

Вектор нормали к поверхности равен градиенту функции $F$ в точке $A$:

$$
\vec n=\operatorname{grad}F(A)
=\left(\frac{2\sqrt3}{9};\frac{2\sqrt5}{25};-\frac{4\sqrt{30}}{225}\right).
$$

Можно умножить этот вектор на ненулевую константу $\dfrac{225}{2}$ и взять более удобный направляющий вектор:

$$
\vec n=(25\sqrt3;9\sqrt5;-2\sqrt{30}).
$$

Каноническое уравнение нормали:

$$
\boxed{
\frac{x-\sqrt3}{25\sqrt3}
=
\frac{y-\sqrt5}{9\sqrt5}
=
\frac{z-2\sqrt{30}}{-2\sqrt{30}}
}
$$

---

## №5. Исследование функции на экстремум

Дана функция

$$
z=y^2-18\ln(xy)+6x-7\frac15.
$$

Здесь $-7\frac15$ — постоянное слагаемое. Оно не влияет на положение точек экстремума и их тип.

Область определения задается условием существования логарифма:

$$
xy>0.
$$

То есть функция определена при

$$
x>0,\ y>0
$$

или при

$$
x<0,\ y<0.
$$

### Находим частные производные первого порядка

$$
z_x=\frac{\partial}{\partial x}\left(y^2-18\ln(xy)+6x-7\frac15\right).
$$

Так как

$$
\frac{\partial}{\partial x}\ln(xy)=\frac1x,
$$

получаем:

$$
z_x=-\frac{18}{x}+6.
$$

Теперь производная по $y$:

$$
z_y=\frac{\partial}{\partial y}\left(y^2-18\ln(xy)+6x-7\frac15\right).
$$

Так как

$$
\frac{\partial}{\partial y}\ln(xy)=\frac1y,
$$

получаем:

$$
z_y=2y-\frac{18}{y}.
$$

### Находим стационарные точки

Стационарные точки находятся из системы

$$
\begin{cases}
z_x=0,\\
z_y=0.
\end{cases}
$$

То есть

$$
\begin{cases}
-\dfrac{18}{x}+6=0,\\
2y-\dfrac{18}{y}=0.
\end{cases}
$$

Из первого уравнения:

$$
6=\frac{18}{x},
$$

$$
x=3.
$$

Из второго уравнения:

$$
2y=\frac{18}{y}.
$$

Умножаем на $y$:

$$
2y^2=18.
$$

$$
y^2=9.
$$

$$
y=\pm3.
$$

Но при $x=3$ область определения требует

$$
xy>0.
$$

Если $x=3>0$, то должно быть $y>0$. Следовательно,

$$
y=3.
$$

Стационарная точка:

$$
\boxed{(3;3)}
$$

### Находим частные производные второго порядка

$$
z_{xx}=\frac{\partial}{\partial x}\left(-\frac{18}{x}+6\right)=\frac{18}{x^2}.
$$

$$
z_{yy}=\frac{\partial}{\partial y}\left(2y-\frac{18}{y}\right)=2+\frac{18}{y^2}.
$$

$$
z_{xy}=0.
$$

В точке $(3;3)$:

$$
z_{xx}(3;3)=\frac{18}{3^2}=2,
$$

$$
z_{yy}(3;3)=2+\frac{18}{3^2}=2+2=4,
$$

$$
z_{xy}(3;3)=0.
$$

Обозначим:

$$
a_{11}=z_{xx}(3;3)=2,
$$

$$
a_{22}=z_{yy}(3;3)=4,
$$

$$
a_{12}=z_{xy}(3;3)=0.
$$

Определитель Гессе:

$$
\Delta=a_{11}a_{22}-a_{12}^2.
$$

Подставляем значения:

$$
\Delta=2\cdot4-0^2=8.
$$

Так как

$$
\Delta>0
$$

и

$$
a_{11}>0,
$$

то в точке $(3;3)$ функция имеет минимум.

### Значение функции в точке минимума

$$
z(3;3)=3^2-18\ln(3\cdot3)+6\cdot3-7\frac15.
$$

$$
z(3;3)=9-18\ln9+18-7\frac15.
$$

Так как

$$
7\frac15=\frac{36}{5},
$$

то

$$
z(3;3)=27-\frac{36}{5}-18\ln9.
$$

$$
27=\frac{135}{5},
$$

следовательно,

$$
z(3;3)=\frac{135}{5}-\frac{36}{5}-18\ln9.
$$

$$
z(3;3)=\frac{99}{5}-18\ln9.
$$

Также можно записать через $\ln3$:

$$
\ln9=2\ln3,
$$

поэтому

$$
z(3;3)=\frac{99}{5}-36\ln3.
$$

Ответ:

$$
\boxed{
(3;3) \text{ — точка минимума}
}
$$

$$
\boxed{
z_{\min}=\frac{99}{5}-18\ln9=\frac{99}{5}-36\ln3
}
$$

---

# Итоговые ответы

1. Для функции

$$
z=\frac{\cos y}{\sqrt{\ln(x^2+y-9)}}
$$

частные производные первого порядка:

$$
\boxed{
\frac{\partial z}{\partial x}
=-\frac{x\cos y}{(x^2+y-9)\left(\ln(x^2+y-9)\right)^{\frac32}}
}
$$

$$
\boxed{
\frac{\partial z}{\partial y}
=-\frac{\sin y}{\sqrt{\ln(x^2+y-9)}}
-\frac{\cos y}{2(x^2+y-9)\left(\ln(x^2+y-9)\right)^{\frac32}}
}
$$

2. Для функции

$$
z=e^{\frac{x}{y}}-\operatorname{arctg}(5y^2+2y)
$$

смешанные производные равны:

$$
\boxed{
\frac{\partial^2 z}{\partial y\partial x}
=
\frac{\partial^2 z}{\partial x\partial y}
=-\frac{(x+y)e^{\frac{x}{y}}}{y^3}
}
$$

3. Производная по направлению $\overrightarrow{AB}$:

$$
\boxed{
\frac{\partial u}{\partial l}=-\frac{37}{6}
}
$$

4. Касательная плоскость:

$$
\boxed{
25\sqrt3x+9\sqrt5y-2\sqrt{30}z=0
}
$$

Нормаль:

$$
\boxed{
\frac{x-\sqrt3}{25\sqrt3}
=
\frac{y-\sqrt5}{9\sqrt5}
=
\frac{z-2\sqrt{30}}{-2\sqrt{30}}
}
$$

5. Функция имеет минимум в точке

$$
\boxed{(3;3)}.
$$

Значение функции в точке минимума:

$$
\boxed{
z_{\min}=\frac{99}{5}-18\ln9=\frac{99}{5}-36\ln3
}
$$
