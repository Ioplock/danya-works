# Вариант 21 — Полное решение

## Задача 1. Площадь фигуры

**Условие:** $y = \sqrt{x+1}$, $y = \sqrt{7-x}$, $y = 0$

### Нахождение точек пересечения

Приравняем кривые:
$$\sqrt{x+1} = \sqrt{7-x} \;\Rightarrow\; x+1 = 7-x \;\Rightarrow\; x = 3, \quad y = 2$$

Кривая $y = \sqrt{x+1}$ пересекает ось $Ox$ при $x = -1$, кривая $y = \sqrt{7-x}$ — при $x = 7$.

На отрезке $[-1, 3]$ верхней границей служит $y = \sqrt{x+1}$; на $[3, 7]$ — $y = \sqrt{7-x}$.

### Вычисление площади

$$S = \int_{-1}^{3} \sqrt{x+1}\, dx + \int_{3}^{7} \sqrt{7-x}\, dx$$

Первый интеграл (замена $u = x+1$):
$$\int_{-1}^{3} \sqrt{x+1}\, dx = \left[\frac{2}{3}(x+1)^{3/2}\right]_{-1}^{3} = \frac{2}{3}\cdot 4^{3/2} - 0 = \frac{2}{3}\cdot 8 = \frac{16}{3}$$

Второй интеграл (замена $u = 7-x$):
$$\int_{3}^{7} \sqrt{7-x}\, dx = \left[-\frac{2}{3}(7-x)^{3/2}\right]_{3}^{7} = 0 - \left(-\frac{2}{3}\cdot 8\right) = \frac{16}{3}$$

$$\boxed{S = \frac{16}{3} + \frac{16}{3} = \frac{32}{3} \text{ (ед}^2\text{)}}$$

---

## Задача 2. Площадь в полярных координатах

**Условие:** $r = 2\cos 3\varphi$, $r \geq 1$

Кривая $r = 2\cos 3\varphi$ — трёхлепестковая роза. Лепестки расположены там, где $\cos 3\varphi \geq 0$.

Первый лепесток: $\varphi \in [-\pi/6,\; \pi/6]$.

### Нахождение угла пересечения с $r = 1$

$$2\cos 3\varphi = 1 \;\Rightarrow\; \cos 3\varphi = \frac{1}{2} \;\Rightarrow\; 3\varphi = \pm\frac{\pi}{3} \;\Rightarrow\; \varphi = \pm\frac{\pi}{9}$$

На каждом лепестке часть, где $r \geq 1$, соответствует $|\varphi| \leq \pi/9$ (в системе отсчёта лепестка).

### Вычисление площади

Площадь одного «внешнего» сегмента (между кривой и окружностью $r = 1$):
$$S_1 = \frac{1}{2}\int_{-\pi/9}^{\pi/9}\left[(2\cos 3\varphi)^2 - 1^2\right]d\varphi = \int_{0}^{\pi/9}\left[4\cos^2 3\varphi - 1\right]d\varphi$$

Используем $4\cos^2 3\varphi = 2(1 + \cos 6\varphi)$:
$$S_1 = \int_{0}^{\pi/9}\left[1 + 2\cos 6\varphi\right]d\varphi = \left[\varphi + \frac{\sin 6\varphi}{3}\right]_{0}^{\pi/9} = \frac{\pi}{9} + \frac{\sin(2\pi/3)}{3} = \frac{\pi}{9} + \frac{\sqrt{3}/2}{3} = \frac{\pi}{9} + \frac{\sqrt{3}}{6}$$

Полная площадь (три одинаковых лепестка):
$$\boxed{S = 3S_1 = \frac{\pi}{3} + \frac{\sqrt{3}}{2} \approx 1{,}91 \text{ (ед}^2\text{)}}$$

---

## Задача 3. Объём тела вращения (вокруг оси $Ox$)

**Условие:** $\dfrac{x^2}{9} - \dfrac{y^2}{25} = 1$ и $\dfrac{x^2}{25} - \dfrac{y^2}{9} = -1$

Перепишем кривые:
- **Гипербола $H_1$:** $\dfrac{x^2}{9} - \dfrac{y^2}{25} = 1$ — вершины при $x = \pm 3$, ветви открываются влево/вправо.
- **Гипербола $H_2$:** $\dfrac{y^2}{9} - \dfrac{x^2}{25} = 1$ — вершины при $y = \pm 3$, ветви открываются вверх/вниз.

### Точки пересечения

Из $H_1$: $y^2 = \dfrac{25x^2 - 225}{9}$. Из $H_2$: $y^2 = \dfrac{225 + 9x^2}{25}$.

Приравниваем:
$$\frac{25x^2 - 225}{9} = \frac{225 + 9x^2}{25}$$
$$625x^2 - 5625 = 2025 + 81x^2 \;\Rightarrow\; 544x^2 = 7650 \;\Rightarrow\; x^2 = \frac{225}{16} \;\Rightarrow\; x = \pm\frac{15}{4}$$

При $x = 15/4$: $y^2 = \dfrac{225}{16}$, то есть $y = \pm\dfrac{15}{4}$.

### Описание области

Область, ограниченная двумя гиперболами, имеет четырёхкратную симметрию. Её сечения:
- при $0 \leq x \leq 3$: $|y| \leq 3\sqrt{1 + x^2/25}$ (граница — $H_2$);
- при $3 \leq x \leq 15/4$: $\dfrac{5}{3}\sqrt{x^2-9} \leq |y| \leq 3\sqrt{1+x^2/25}$ (шайба между $H_1$ и $H_2$).

### Метод шайб

$$V = 2\pi\left[\int_0^3 \left(3\sqrt{1+\frac{x^2}{25}}\right)^2 dx + \int_3^{15/4}\left[\left(3\sqrt{1+\frac{x^2}{25}}\right)^2 - \left(\frac{5}{3}\sqrt{x^2-9}\right)^2\right]dx\right]$$

Вычислим первый интеграл:
$$\int_0^3 9\left(1 + \frac{x^2}{25}\right)dx = \left[9x + \frac{3x^3}{25}\right]_0^3 = 27 + \frac{81}{25} = \frac{756}{25}$$

Подынтегральная функция второго интеграла:
$$9\left(1+\frac{x^2}{25}\right) - \frac{25}{9}(x^2-9) = 34 - \frac{544}{225}x^2$$

Второй интеграл:
$$\int_3^{15/4}\left(34 - \frac{544}{225}x^2\right)dx = \left[34x - \frac{544}{675}x^3\right]_3^{15/4}$$

При $x = 15/4$:
$$34\cdot\frac{15}{4} - \frac{544}{675}\cdot\frac{3375}{64} = \frac{255}{2} - \frac{85}{2} = 85$$

При $x = 3$:
$$102 - \frac{544 \cdot 27}{675} = 102 - \frac{544}{25} = \frac{2006}{25}$$

$$\int_3^{15/4} = 85 - \frac{2006}{25} = \frac{119}{25}$$

Итого:
$$V = 2\pi\left(\frac{756}{25} + \frac{119}{25}\right) = 2\pi\cdot\frac{875}{25} = 2\pi\cdot 35$$

$$\boxed{V = 70\pi \approx 219{,}9 \text{ (ед}^3\text{)}}$$

---

## Задача 4а. Длина дуги (прямоугольные координаты)

**Условие:** $y = \ln(x^2-1)$, $2 \leq x \leq 5$

### Подготовка

$$y' = \frac{2x}{x^2-1}$$

$$1 + (y')^2 = 1 + \frac{4x^2}{(x^2-1)^2} = \frac{(x^2-1)^2 + 4x^2}{(x^2-1)^2} = \frac{(x^2+1)^2}{(x^2-1)^2}$$

$$\sqrt{1+(y')^2} = \frac{x^2+1}{x^2-1} \quad (x > 1)$$

### Интегрирование

Разложим дробь:
$$\frac{x^2+1}{x^2-1} = 1 + \frac{2}{x^2-1} = 1 + \frac{1}{x-1} - \frac{1}{x+1}$$

$$L = \int_2^5\left(1 + \frac{1}{x-1} - \frac{1}{x+1}\right)dx = \left[x + \ln\frac{x-1}{x+1}\right]_2^5$$

$$= \left(5 + \ln\frac{4}{6}\right) - \left(2 + \ln\frac{1}{3}\right) = 3 + \ln\frac{4}{6} - \ln\frac{1}{3} = 3 + \ln\left(\frac{4}{6}\cdot 3\right) = 3 + \ln 2$$

$$\boxed{L = 3 + \ln 2 \approx 3{,}693}$$

---

## Задача 4б. Длина дуги (параметрические уравнения)

**Условие:** $x = 2\cos^3 t$, $y = \sin^3 t$, $0 \leq t \leq \pi/6$

### Производные

$$x'(t) = -6\cos^2 t\sin t, \qquad y'(t) = 3\sin^2 t\cos t$$

$$(x')^2 + (y')^2 = 36\cos^4 t\sin^2 t + 9\sin^4 t\cos^2 t = 9\cos^2 t\sin^2 t\left(4\cos^2 t + \sin^2 t\right)$$

$$= 9\cos^2 t\sin^2 t\,(3\cos^2 t + 1)$$

$$\sqrt{(x')^2+(y')^2} = 3\cos t\sin t\sqrt{3\cos^2 t + 1} \quad \text{(на } [0, \pi/6] \text{)}$$

### Вычисление

$$L = 3\int_0^{\pi/6}\cos t\sin t\sqrt{3\cos^2 t+1}\, dt$$

Замена: $u = \cos^2 t$, $du = -2\cos t\sin t\, dt$. При $t=0$: $u=1$; при $t=\pi/6$: $u = 3/4$.

$$L = \frac{3}{2}\int_{3/4}^{1}\sqrt{3u+1}\, du = \frac{3}{2}\cdot\left[\frac{2}{9}(3u+1)^{3/2}\right]_{3/4}^{1} = \frac{1}{3}\left[(4)^{3/2} - \left(\frac{13}{4}\right)^{3/2}\right]$$

$$= \frac{1}{3}\left[8 - \frac{13\sqrt{13}}{8}\right]$$

$$\boxed{L = \frac{8}{3} - \frac{13\sqrt{13}}{24} \approx 0{,}714}$$

---

## Задача 5. Площадь поверхности вращения (вокруг оси $Ox$)

**Условие:** $x = 2\cos t - \cos 2t$, $y = 2\sin t - \sin 2t$, $0 \leq t \leq 2\pi$

Это эпициклоида (кардиоидоподобная кривая), симметричная относительно оси $Ox$.

### Подготовка

$$x'(t) = -2\sin t + 2\sin 2t, \qquad y'(t) = 2\cos t - 2\cos 2t$$

$$(x')^2 + (y')^2 = 4\left[(\sin 2t - \sin t)^2 + (\cos t - \cos 2t)^2\right]$$
$$= 4\left[2 - 2(\cos t\cos 2t + \sin t\sin 2t)\right] = 8(1 - \cos t) = 16\sin^2\!\frac{t}{2}$$
$$\sqrt{(x')^2+(y')^2} = 4\sin\frac{t}{2} \quad (0 \leq t \leq 2\pi)$$

Преобразуем $y(t)$, используя $\sin t = 2\sin\tfrac{t}{2}\cos\tfrac{t}{2}$ и $1 - \cos t = 2\sin^2\tfrac{t}{2}$:
$$y = 2\sin t(1 - \cos t) = 4\sin\frac{t}{2}\cos\frac{t}{2}\cdot 2\sin^2\frac{t}{2} = 8\sin^3\frac{t}{2}\cos\frac{t}{2}$$

При $t \in (0, \pi)$: $y > 0$; при $t \in (\pi, 2\pi)$: $y < 0$. Кривая симметрична: $y(2\pi - t) = -y(t)$, $x(2\pi - t) = x(t)$. При вращении верхняя ($t \in [0,\pi]$) и нижняя ($t \in [\pi, 2\pi]$) половины описывают **одну и ту же** поверхность, поэтому используем только верхнюю:

### Вычисление

$$S = 2\pi\int_0^{\pi} y(t)\sqrt{(x')^2+(y')^2}\, dt = 2\pi\int_0^{\pi} 8\sin^3\frac{t}{2}\cos\frac{t}{2}\cdot 4\sin\frac{t}{2}\, dt$$

$$= 64\pi\int_0^{\pi}\sin^4\frac{t}{2}\cos\frac{t}{2}\, dt$$

Замена: $u = \sin(t/2)$, $du = \frac{1}{2}\cos(t/2)\, dt$. При $t = 0$: $u = 0$; при $t = \pi$: $u = 1$.

$$S = 64\pi\int_0^1 u^4\cdot 2\, du = 128\pi\cdot\frac{1}{5}$$

$$\boxed{S = \frac{128\pi}{5} \approx 80{,}4 \text{ (ед}^2\text{)}}$$

---

## Задача 6. Несобственные интегралы

### 6а. $\displaystyle I = \int_0^{\infty} e^{-7x}\cos 2x\, dx$

Интегрируем по частям дважды. Полагаем $u = \cos 2x$, $dv = e^{-7x}dx$:

$$I = \left[-\frac{e^{-7x}}{7}\cos 2x\right]_0^{\infty} - \frac{2}{7}\int_0^{\infty} e^{-7x}\sin 2x\, dx = \frac{1}{7} - \frac{2}{7}J$$

где $J = \displaystyle\int_0^{\infty} e^{-7x}\sin 2x\, dx$. Аналогично ($u = \sin 2x$, $dv = e^{-7x}dx$):

$$J = \left[-\frac{e^{-7x}}{7}\sin 2x\right]_0^{\infty} + \frac{2}{7}\int_0^{\infty} e^{-7x}\cos 2x\, dx = 0 + \frac{2}{7}I$$

Подставляем $J = \tfrac{2}{7}I$ в выражение для $I$:

$$I = \frac{1}{7} - \frac{2}{7}\cdot\frac{2}{7}I = \frac{1}{7} - \frac{4}{49}I$$

$$I\left(1 + \frac{4}{49}\right) = \frac{1}{7} \;\Rightarrow\; I\cdot\frac{53}{49} = \frac{1}{7}$$

$$\boxed{I = \frac{7}{53}}$$

---

### 6б. $\displaystyle\int_0^1 \cos\!\left(\frac{\pi}{1-x}\right)\frac{dx}{(1-x)^2}$

Интеграл несобственный (особая точка при $x \to 1^-$).

**Замена:** $t = \dfrac{\pi}{1-x}$, тогда $1 - x = \dfrac{\pi}{t}$, $dx = \dfrac{\pi}{t^2}dt$, $(1-x)^2 = \dfrac{\pi^2}{t^2}$.

$$\frac{dx}{(1-x)^2} = \frac{\pi/t^2\, dt}{\pi^2/t^2} = \frac{dt}{\pi}$$

При $x = 0$: $t = \pi$; при $x \to 1^-$: $t \to +\infty$.

$$\int_0^1 \cos\!\left(\frac{\pi}{1-x}\right)\frac{dx}{(1-x)^2} = \frac{1}{\pi}\int_{\pi}^{+\infty}\cos t\, dt = \frac{1}{\pi}\lim_{b\to+\infty}\left[\sin t\right]_{\pi}^{b} = \frac{1}{\pi}\lim_{b\to+\infty}\sin b$$

Предел $\lim_{b\to+\infty}\sin b$ **не существует** (функция осциллирует).

$$\boxed{\text{Интеграл расходится.}}$$

---

## Задача 7. Работа против сил тяготения

**Условие:** Поднять тело массы $M$ с поверхности Земли (радиус $R$) на высоту $H$.

### Решение

По закону всемирного тяготения сила, действующая на тело на расстоянии $r$ от центра Земли:
$$F(r) = \frac{gMR^2}{r^2}$$

(здесь использовано, что на поверхности $F(R) = Mg$, откуда $GM_{\oplus} = gR^2$).

Элементарная работа при перемещении тела на $dr$:
$$dA = F(r)\, dr = \frac{gMR^2}{r^2}\, dr$$

Полная работа при подъёме с $r = R$ до $r = R + H$:
$$A = \int_R^{R+H}\frac{gMR^2}{r^2}\, dr = gMR^2\left[-\frac{1}{r}\right]_R^{R+H} = gMR^2\left(\frac{1}{R} - \frac{1}{R+H}\right)$$

$$= gMR^2\cdot\frac{H}{R(R+H)}$$

$$\boxed{A = \frac{gMRH}{R+H}}$$

**Частные случаи:**
- При $H \ll R$: $A \approx \frac{gMRH}{R} = MgH$ (работа против равномерного поля) ✓
- При $H \to \infty$: $A \to MgR$ (вторая космическая скорость соответствует $\frac{1}{2}Mv^2 = MgR$) ✓
