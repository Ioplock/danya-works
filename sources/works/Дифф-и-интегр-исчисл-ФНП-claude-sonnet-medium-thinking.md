# РГР — Дифференциальное исчисление ФНП. Вариант 21

---

## Задача 1. Частные производные первого порядка

$$z = \frac{\cos y}{\sqrt{\ln(x^2 + y - 9)}}$$

Перепишем функцию в удобном виде:

$$z = \cos y \cdot \bigl[\ln(x^2+y-9)\bigr]^{-1/2}$$

### Частная производная по $x$ ($y = \text{const}$)

Дифференцируем по $x$, применяя правило дифференцирования степенной функции со сложным аргументом:

$$\frac{\partial z}{\partial x} = \cos y \cdot \left(-\frac{1}{2}\right)\bigl[\ln(x^2+y-9)\bigr]^{-3/2} \cdot \frac{1}{x^2+y-9} \cdot 2x$$

$$\boxed{\frac{\partial z}{\partial x} = -\frac{x\cos y}{(x^2+y-9)\,\bigl[\ln(x^2+y-9)\bigr]^{3/2}}}$$

### Частная производная по $y$ ($x = \text{const}$)

Здесь $y$ входит в оба множителя, поэтому применяем правило произведения:

$$\frac{\partial z}{\partial y} = \underbrace{(-\sin y)}_{\text{произв. }\cos y} \cdot \bigl[\ln(x^2+y-9)\bigr]^{-1/2}
\;+\; \cos y \cdot \left(-\frac{1}{2}\right)\bigl[\ln(x^2+y-9)\bigr]^{-3/2} \cdot \frac{1}{x^2+y-9}$$

$$\boxed{\frac{\partial z}{\partial y} = -\frac{\sin y}{\sqrt{\ln(x^2+y-9)}} - \frac{\cos y}{2\,(x^2+y-9)\,\bigl[\ln(x^2+y-9)\bigr]^{3/2}}}$$

---

## Задача 2. Проверка равенства смешанных производных второго порядка

$$z = e^{x/y} - \operatorname{arctg}(5y^2 + 2y)$$

Необходимо убедиться, что $\dfrac{\partial^2 z}{\partial y\,\partial x} = \dfrac{\partial^2 z}{\partial x\,\partial y}$.

### Первые частные производные

$$\frac{\partial z}{\partial x} = e^{x/y} \cdot \frac{1}{y} = \frac{e^{x/y}}{y}$$

$$\frac{\partial z}{\partial y} = e^{x/y} \cdot \left(-\frac{x}{y^2}\right) - \frac{10y+2}{1+(5y^2+2y)^2} = -\frac{x}{y^2}\,e^{x/y} - \frac{10y+2}{1+(5y^2+2y)^2}$$

### Вычисление $\dfrac{\partial^2 z}{\partial y\,\partial x}$ (дифференцируем $z'_x$ по $y$)

$$\frac{\partial^2 z}{\partial y\,\partial x} = \frac{\partial}{\partial y}\!\left(\frac{e^{x/y}}{y}\right)$$

Применяем правило произведения ($u = e^{x/y}$, $v = 1/y$):

$$= \frac{1}{y} \cdot e^{x/y} \cdot \left(-\frac{x}{y^2}\right) + e^{x/y} \cdot \left(-\frac{1}{y^2}\right)
= -\frac{x}{y^3}\,e^{x/y} - \frac{1}{y^2}\,e^{x/y}
= -\frac{e^{x/y}}{y^2}\left(\frac{x}{y}+1\right)$$

$$\frac{\partial^2 z}{\partial y\,\partial x} = -\frac{(x+y)\,e^{x/y}}{y^3}$$

### Вычисление $\dfrac{\partial^2 z}{\partial x\,\partial y}$ (дифференцируем $z'_y$ по $x$)

Второе слагаемое $z'_y$ от $x$ не зависит, поэтому:

$$\frac{\partial^2 z}{\partial x\,\partial y} = \frac{\partial}{\partial x}\!\left(-\frac{x}{y^2}\,e^{x/y}\right)
= -\frac{1}{y^2}\,e^{x/y} - \frac{x}{y^2}\cdot e^{x/y}\cdot\frac{1}{y}
= -\frac{e^{x/y}}{y^2}\left(1+\frac{x}{y}\right)$$

$$\frac{\partial^2 z}{\partial x\,\partial y} = -\frac{(x+y)\,e^{x/y}}{y^3}$$

### Вывод

$$\frac{\partial^2 z}{\partial y\,\partial x} = \frac{\partial^2 z}{\partial x\,\partial y} = -\frac{(x+y)\,e^{x/y}}{y^3} \quad \checkmark$$

Равенство смешанных производных подтверждено (функция имеет непрерывные частные производные, что гарантируется теоремой Шварца).

---

## Задача 3. Производная по направлению вектора $\overrightarrow{AB}$

$$u = xy + \sqrt{z} + 4zx, \qquad A(1;\,2;\,1), \quad B(-1;\,0;\,0)$$

Вариант 21 — нечётный, поэтому вычисляем производную в направлении вектора $\overrightarrow{AB}$.

### Шаг 1. Вектор направления и его длина

$$\overrightarrow{AB} = B - A = (-1-1;\;0-2;\;0-1) = (-2;\;-2;\;-1)$$

$$|\overrightarrow{AB}| = \sqrt{(-2)^2+(-2)^2+(-1)^2} = \sqrt{4+4+1} = \sqrt{9} = 3$$

### Шаг 2. Направляющие косинусы

$$\cos\alpha = \frac{-2}{3}, \qquad \cos\beta = \frac{-2}{3}, \qquad \cos\gamma = \frac{-1}{3}$$

### Шаг 3. Частные производные $u$ и их значения в точке $A$

$$\frac{\partial u}{\partial x} = y + 4z \quad\Rightarrow\quad \frac{\partial u}{\partial x}\bigg|_A = 2 + 4\cdot1 = 6$$

$$\frac{\partial u}{\partial y} = x \quad\Rightarrow\quad \frac{\partial u}{\partial y}\bigg|_A = 1$$

$$\frac{\partial u}{\partial z} = \frac{1}{2\sqrt{z}} + 4x \quad\Rightarrow\quad \frac{\partial u}{\partial z}\bigg|_A = \frac{1}{2\sqrt{1}} + 4\cdot1 = \frac{1}{2}+4 = \frac{9}{2}$$

### Шаг 4. Производная по направлению

По формуле:

$$\frac{\partial u}{\partial l} = \frac{\partial u}{\partial x}\cos\alpha + \frac{\partial u}{\partial y}\cos\beta + \frac{\partial u}{\partial z}\cos\gamma$$

$$= 6\cdot\left(-\frac{2}{3}\right) + 1\cdot\left(-\frac{2}{3}\right) + \frac{9}{2}\cdot\left(-\frac{1}{3}\right)$$

$$= -4 - \frac{2}{3} - \frac{3}{2} = -\frac{24}{6} - \frac{4}{6} - \frac{9}{6}$$

$$\boxed{\frac{\partial u}{\partial l}\bigg|_A = -\frac{37}{6} \approx -6{,}17}$$

Отрицательное значение означает, что функция убывает в направлении из $A$ в $B$.

---

## Задача 4. Касательная плоскость и нормаль к поверхности

$$\frac{x^2}{9}+\frac{y^2}{25}-\frac{z^2}{225}=0, \qquad A\!\left(\sqrt{3};\;\sqrt{5};\;2\sqrt{30}\right)$$

Поверхность задана неявно: $F(x,y,z) = \dfrac{x^2}{9}+\dfrac{y^2}{25}-\dfrac{z^2}{225}$.

### Проверка принадлежности точки $A$ поверхности

$$F\!\left(\sqrt{3};\sqrt{5};2\sqrt{30}\right)=\frac{3}{9}+\frac{5}{25}-\frac{4\cdot30}{225}=\frac{1}{3}+\frac{1}{5}-\frac{120}{225}=\frac{5}{15}+\frac{3}{15}-\frac{8}{15}=0\;\checkmark$$

### Частные производные $F$

$$F_x = \frac{2x}{9}, \qquad F_y = \frac{2y}{25}, \qquad F_z = -\frac{2z}{225}$$

В точке $A$:

$$F_x\big|_A = \frac{2\sqrt{3}}{9}, \qquad F_y\big|_A = \frac{2\sqrt{5}}{25}, \qquad F_z\big|_A = -\frac{4\sqrt{30}}{225}$$

### Уравнение касательной плоскости

$$F_x(x-x_0)+F_y(y-y_0)+F_z(z-z_0)=0$$

$$\frac{2\sqrt{3}}{9}(x-\sqrt{3})+\frac{2\sqrt{5}}{25}(y-\sqrt{5})-\frac{4\sqrt{30}}{225}(z-2\sqrt{30})=0$$

Умножим на $\dfrac{225}{2}$:

$$25\sqrt{3}(x-\sqrt{3})+9\sqrt{5}(y-\sqrt{5})-2\sqrt{30}(z-2\sqrt{30})=0$$

$$25\sqrt{3}\,x - 75 + 9\sqrt{5}\,y - 45 - 2\sqrt{30}\,z + 120 = 0$$

$$25\sqrt{3}\,x + 9\sqrt{5}\,y - 2\sqrt{30}\,z + (-75-45+120) = 0$$

$$\boxed{25\sqrt{3}\,x + 9\sqrt{5}\,y - 2\sqrt{30}\,z = 0}$$

### Уравнение нормали

Направляющий вектор нормали: $\vec{n} = (25\sqrt{3};\;9\sqrt{5};\;-2\sqrt{30})$

$$\frac{x-\sqrt{3}}{25\sqrt{3}} = \frac{y-\sqrt{5}}{9\sqrt{5}} = \frac{z-2\sqrt{30}}{-2\sqrt{30}}$$

---

## Задача 5. Исследование функции на экстремум

$$z = y^2 - 18\ln(xy) + 6x - \frac{36}{5}, \qquad x>0,\;y>0$$

Область определения: $x > 0$, $y > 0$ (условие существования $\ln(xy)$).

### Шаг 1. Нахождение стационарных точек

Используем $\ln(xy) = \ln x + \ln y$ и вычисляем частные производные:

$$\frac{\partial z}{\partial x} = -\frac{18}{x} + 6$$

$$\frac{\partial z}{\partial y} = 2y - \frac{18}{y}$$

Приравниваем к нулю:

$$\frac{\partial z}{\partial x} = 0:\quad -\frac{18}{x}+6=0 \;\Rightarrow\; x = 3$$

$$\frac{\partial z}{\partial y} = 0:\quad 2y - \frac{18}{y} = 0 \;\Rightarrow\; 2y^2 = 18 \;\Rightarrow\; y^2 = 9 \;\Rightarrow\; y = 3 \quad(y>0)$$

**Единственная стационарная точка:** $M(3;\,3)$.

### Шаг 2. Вторые частные производные

$$\frac{\partial^2 z}{\partial x^2} = \frac{18}{x^2}, \qquad \frac{\partial^2 z}{\partial y^2} = 2+\frac{18}{y^2}, \qquad \frac{\partial^2 z}{\partial x\,\partial y} = 0$$

В точке $M(3;\,3)$:

$$a_{11} = \frac{\partial^2 z}{\partial x^2}\bigg|_M = \frac{18}{9} = 2$$

$$a_{22} = \frac{\partial^2 z}{\partial y^2}\bigg|_M = 2 + \frac{18}{9} = 4$$

$$a_{12} = \frac{\partial^2 z}{\partial x\,\partial y}\bigg|_M = 0$$

### Шаг 3. Проверка достаточного условия

$$\Delta = \begin{vmatrix} a_{11} & a_{12} \\ a_{12} & a_{22} \end{vmatrix} = a_{11}\,a_{22} - a_{12}^2 = 2\cdot4 - 0^2 = 8 > 0$$

Так как $\Delta = 8 > 0$ и $a_{11} = 2 > 0$, точка $M(3;\,3)$ является **точкой минимума**.

### Шаг 4. Значение функции в точке минимума

$$z_{\min} = z(3,3) = 3^2 - 18\ln(3\cdot3) + 6\cdot3 - \frac{36}{5}$$

$$= 9 - 18\ln 9 + 18 - \frac{36}{5} = 27 - \frac{36}{5} - 18\ln 9$$

$$= \frac{135-36}{5} - 36\ln 3$$

$$\boxed{z_{\min} = \frac{99}{5} - 36\ln 3 \approx 19{,}8 - 39{,}55 \approx -19{,}75}$$

**Вывод:** функция $z = y^2 - 18\ln(xy) + 6x - \dfrac{36}{5}$ имеет единственный минимум в точке $(3;\,3)$ со значением $\dfrac{99}{5} - 36\ln 3$.
