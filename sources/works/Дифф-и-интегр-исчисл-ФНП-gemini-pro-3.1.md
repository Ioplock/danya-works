Вот подробное решение всех пяти заданий 21-го варианта расчетно-графической работы.

---

### Задание 1

**Вычислить частные производные первого порядка для функции:**


$$z = \frac{\cos y}{\sqrt{\ln(x^2+y-9)}}$$

Для нахождения частной производной по $x$, считаем переменную $y$ постоянной. Применяем правило дифференцирования сложной функции:


$$\frac{\partial z}{\partial x} = \cos y \cdot \left( -\frac{1}{2} (\ln(x^2+y-9))^{-3/2} \right) \cdot \frac{\partial}{\partial x} (\ln(x^2+y-9))$$

$$\frac{\partial z}{\partial x} = -\frac{\cos y}{2 \sqrt{\ln^3(x^2+y-9)}} \cdot \frac{2x}{x^2+y-9} = -\frac{x \cos y}{(x^2+y-9)\sqrt{\ln^3(x^2+y-9)}}$$

Для нахождения частной производной по $y$, считаем переменную $x$ постоянной. Используем правило дифференцирования дроби (или произведения):


$$\frac{\partial z}{\partial y} = \frac{\partial}{\partial y}\left( \cos y \right) \cdot (\ln(x^2+y-9))^{-1/2} + \cos y \cdot \frac{\partial}{\partial y}\left( (\ln(x^2+y-9))^{-1/2} \right)$$

$$\frac{\partial z}{\partial y} = -\sin y \cdot (\ln(x^2+y-9))^{-1/2} + \cos y \cdot \left( -\frac{1}{2} (\ln(x^2+y-9))^{-3/2} \right) \cdot \frac{1}{x^2+y-9}$$

$$\frac{\partial z}{\partial y} = -\frac{\sin y}{\sqrt{\ln(x^2+y-9)}} - \frac{\cos y}{2(x^2+y-9)\sqrt{\ln^3(x^2+y-9)}}$$

---

### Задание 2

**Проверить равенство смешанных производных второго порядка:**


$$z = e^{\frac{x}{y}} - \operatorname{arctg}(5y^2+2y)$$

Сначала найдем частные производные первого порядка:


$$\frac{\partial z}{\partial x} = e^{\frac{x}{y}} \cdot \frac{1}{y}$$

$$\frac{\partial z}{\partial y} = e^{\frac{x}{y}} \cdot \left(-\frac{x}{y^2}\right) - \frac{1}{1+(5y^2+2y)^2} \cdot (10y+2) = -\frac{x}{y^2}e^{\frac{x}{y}} - \frac{10y+2}{1+(5y^2+2y)^2}$$

Теперь найдем смешанные производные второго порядка.
Дифференцируем $\frac{\partial z}{\partial x}$ по переменной $y$:


$$\frac{\partial^2 z}{\partial y \partial x} = \frac{\partial}{\partial y} \left( \frac{1}{y} e^{\frac{x}{y}} \right) = \left(-\frac{1}{y^2}\right) e^{\frac{x}{y}} + \frac{1}{y} \left( e^{\frac{x}{y}} \cdot \left(-\frac{x}{y^2}\right) \right) = -e^{\frac{x}{y}} \left( \frac{1}{y^2} + \frac{x}{y^3} \right) = -\frac{y+x}{y^3} e^{\frac{x}{y}}$$

Дифференцируем $\frac{\partial z}{\partial y}$ по переменной $x$ (второе слагаемое от $x$ не зависит, поэтому его производная равна нулю):


$$\frac{\partial^2 z}{\partial x \partial y} = \frac{\partial}{\partial x} \left( -\frac{x}{y^2}e^{\frac{x}{y}} - \frac{10y+2}{1+(5y^2+2y)^2} \right) = -\frac{1}{y^2} \left( 1 \cdot e^{\frac{x}{y}} + x \cdot e^{\frac{x}{y}} \cdot \frac{1}{y} \right) = -\frac{1}{y^2} e^{\frac{x}{y}} - \frac{x}{y^3} e^{\frac{x}{y}} = -\frac{y+x}{y^3} e^{\frac{x}{y}}$$

**Вывод:** Равенство выполняется, так как $\frac{\partial^2 z}{\partial y \partial x} = \frac{\partial^2 z}{\partial x \partial y} = -\frac{y+x}{y^3} e^{\frac{x}{y}}$.

---

### Задание 3

**Вычислить производную по направлению $\frac{\partial u}{\partial l}$ для функции $u = xy + \sqrt{z} + 4zx$ в точке $A(1; 2; 1)$ в направлении вектора $\overrightarrow{AB}$, если $B(-1; 0; 0)$.**

Найдем вектор $\overrightarrow{l} = \overrightarrow{AB}$ и его направляющие косинусы:


$$\overrightarrow{AB} = (-1-1;\; 0-2;\; 0-1) = (-2;\; -2;\; -1)$$


Длина вектора: $|\overrightarrow{AB}| = \sqrt{(-2)^2 + (-2)^2 + (-1)^2} = \sqrt{4 + 4 + 1} = \sqrt{9} = 3$.
Направляющие косинусы:


$$\cos\alpha = -\frac{2}{3}, \quad \cos\beta = -\frac{2}{3}, \quad \cos\gamma = -\frac{1}{3}$$

Найдем частные производные функции в произвольной точке и вычислим их значения в точке $A(1; 2; 1)$:

* $\frac{\partial u}{\partial x} = y + 4z \implies \left. \frac{\partial u}{\partial x} \right|_A = 2 + 4(1) = 6$
* $\frac{\partial u}{\partial y} = x \implies \left. \frac{\partial u}{\partial y} \right|_A = 1$
* $\frac{\partial u}{\partial z} = \frac{1}{2\sqrt{z}} + 4x \implies \left. \frac{\partial u}{\partial z} \right|_A = \frac{1}{2\sqrt{1}} + 4(1) = 4.5 = \frac{9}{2}$

Производная по направлению вычисляется по формуле:


$$\frac{\partial u}{\partial l} = \frac{\partial u}{\partial x}\cos\alpha + \frac{\partial u}{\partial y}\cos\beta + \frac{\partial u}{\partial z}\cos\gamma$$

$$\frac{\partial u}{\partial l} = 6 \cdot \left(-\frac{2}{3}\right) + 1 \cdot \left(-\frac{2}{3}\right) + \frac{9}{2} \cdot \left(-\frac{1}{3}\right) = -4 - \frac{2}{3} - \frac{3}{2} = -\frac{24}{6} - \frac{4}{6} - \frac{9}{6} = -\frac{37}{6} = -6\frac{1}{6}$$

---

### Задание 4

**Выписать уравнение касательной плоскости и нормали к поверхности $\frac{x^2}{9} + \frac{y^2}{25} - \frac{z^2}{225} = 0$ в точке $A(\sqrt{3}; \sqrt{5}; 2\sqrt{30})$.**

Поверхность задана неявно уравнением $F(x,y,z) = 0$. Обозначим $F(x,y,z) = \frac{x^2}{9} + \frac{y^2}{25} - \frac{z^2}{225}$.
Найдем значения частных производных в точке $A$:

* $F'_x = \frac{2x}{9} \implies F'_x(A) = \frac{2\sqrt{3}}{9}$
* $F'_y = \frac{2y}{25} \implies F'_y(A) = \frac{2\sqrt{5}}{25}$
* $F'_z = -\frac{2z}{225} \implies F'_z(A) = -\frac{4\sqrt{30}}{225}$

**Уравнение касательной плоскости**:


$$F'_x(A)(x-x_0) + F'_y(A)(y-y_0) + F'_z(A)(z-z_0) = 0$$

$$\frac{2\sqrt{3}}{9}(x-\sqrt{3}) + \frac{2\sqrt{5}}{25}(y-\sqrt{5}) - \frac{4\sqrt{30}}{225}(z-2\sqrt{30}) = 0$$


Для удобства умножим обе части на $\frac{225}{2}$:


$$25\sqrt{3}(x-\sqrt{3}) + 9\sqrt{5}(y-\sqrt{5}) - 2\sqrt{30}(z-2\sqrt{30}) = 0$$


Раскроем скобки:


$$25\sqrt{3}x - 75 + 9\sqrt{5}y - 45 - 2\sqrt{30}z + 120 = 0$$

$$25\sqrt{3}x + 9\sqrt{5}y - 2\sqrt{30}z = 0$$

**Уравнение нормали**:


$$\frac{x-x_0}{F'_x(A)} = \frac{y-y_0}{F'_y(A)} = \frac{z-z_0}{F'_z(A)}$$

$$\frac{x-\sqrt{3}}{\frac{2\sqrt{3}}{9}} = \frac{y-\sqrt{5}}{\frac{2\sqrt{5}}{25}} = \frac{z-2\sqrt{30}}{-\frac{4\sqrt{30}}{225}}$$


Можно записать проще, умножив знаменатели на $\frac{225}{2}$:


$$\frac{x-\sqrt{3}}{25\sqrt{3}} = \frac{y-\sqrt{5}}{9\sqrt{5}} = \frac{z-2\sqrt{30}}{-2\sqrt{30}}$$

---

### Задание 5

**Исследовать на экстремум функцию:**


$$z = y^2 - 18\ln(xy) + 6x - 7\frac{1}{5}$$

Область определения функции: $xy > 0$ (переменные $x$ и $y$ должны быть одного знака).
Найдем стационарные точки, приравняв частные производные первого порядка к нулю:


$$\frac{\partial z}{\partial x} = 0 - 18 \cdot \frac{1}{xy} \cdot y + 6 = -\frac{18}{x} + 6 = 0 \implies \frac{18}{x} = 6 \implies x = 3$$

$$\frac{\partial z}{\partial y} = 2y - 18 \cdot \frac{1}{xy} \cdot x + 0 = 2y - \frac{18}{y} = 0 \implies \frac{2y^2 - 18}{y} = 0 \implies 2y^2 = 18 \implies y = \pm 3$$

Получаем две стационарные точки: $M_1(3; 3)$ и $M_2(3; -3)$.
Проверим их на принадлежность области определения ($xy > 0$):

* Для $M_1(3; 3)$: $3 \cdot 3 = 9 > 0$ (входит в область).
* Для $M_2(3; -3)$: $3 \cdot (-3) = -9 < 0$ (не входит в область определения).
Исследуем только точку $M_1(3; 3)$.

Найдем частные производные второго порядка:


$$a_{11} = \frac{\partial^2 z}{\partial x^2} = \frac{\partial}{\partial x}\left(-\frac{18}{x} + 6\right) = \frac{18}{x^2}$$

$$a_{22} = \frac{\partial^2 z}{\partial y^2} = \frac{\partial}{\partial y}\left(2y - \frac{18}{y}\right) = 2 + \frac{18}{y^2}$$

$$a_{12} = \frac{\partial^2 z}{\partial x \partial y} = 0$$

Вычислим значения в точке $M_1(3; 3)$:


$$A = a_{11}(3; 3) = \frac{18}{3^2} = 2$$

$$C = a_{22}(3; 3) = 2 + \frac{18}{3^2} = 4$$

$$B = a_{12}(3; 3) = 0$$

Составим дискриминант $\Delta = AC - B^2$:


$$\Delta = 2 \cdot 4 - 0^2 = 8$$

Так как $\Delta > 0$ и $a_{11} = 2 > 0$, то в точке $M_1(3; 3)$ функция имеет **минимум**.
Вычислим минимальное значение:


$$z_{min}(3; 3) = 3^2 - 18\ln(3 \cdot 3) + 6(3) - 7.2 = 9 - 18\ln 9 + 18 - 7.2 = 19.8 - 18\ln 9$$