# Расчётно-графическая работа: Неопределённый интеграл — Вариант 21

---

## Задача 1

$$\int \frac{dx}{x\ln^{41}x}$$

**Метод:** подстановка $t = \ln x$.

Пусть $t = \ln x$, тогда $dt = \dfrac{dx}{x}$.

$$\int \frac{dx}{x\ln^{41}x} = \int t^{-41}\,dt = \frac{t^{-40}}{-40} + C$$

**Ответ:**

$$\boxed{-\frac{1}{40\ln^{40}x} + C}$$

---

## Задача 2

$$\int \sqrt{\frac{8-\arcsin x}{1-x^2}}\,dx$$

**Метод:** подстановка $t = \arcsin x$.

Пусть $t = \arcsin x$, тогда $dt = \dfrac{dx}{\sqrt{1-x^2}}$.

$$\int \sqrt{8-t}\,dt$$

Пусть $u = 8 - t$, $du = -dt$:

$$-\int u^{1/2}\,du = -\frac{2}{3}u^{3/2} + C = -\frac{2}{3}(8-t)^{3/2} + C$$

**Ответ:**

$$\boxed{-\frac{2}{3}(8-\arcsin x)^{3/2} + C}$$

---

## Задача 3

$$\int \frac{x^8\,dx}{\cos^2(14x^9-2)}$$

**Метод:** подстановка $t = 14x^9 - 2$.

Пусть $t = 14x^9 - 2$, тогда $dt = 126x^8\,dx$, откуда $x^8\,dx = \dfrac{dt}{126}$.

$$\frac{1}{126}\int \frac{dt}{\cos^2 t} = \frac{1}{126}\int \sec^2 t\,dt = \frac{\tan t}{126} + C$$

**Ответ:**

$$\boxed{\frac{\tan(14x^9-2)}{126} + C}$$

---

## Задача 4

$$\int 20^x\sin(7\cdot 20^x)\,dx$$

**Метод:** подстановка $t = 20^x$.

Пусть $t = 20^x$, тогда $dt = 20^x\ln 20\,dx$, откуда $20^x\,dx = \dfrac{dt}{\ln 20}$.

$$\frac{1}{\ln 20}\int \sin(7t)\,dt = \frac{1}{\ln 20}\cdot\left(-\frac{\cos(7t)}{7}\right) + C$$

**Ответ:**

$$\boxed{-\frac{\cos(7\cdot 20^x)}{7\ln 20} + C}$$

---

## Задача 5

$$\int \frac{(6-x)\,dx}{x\sqrt{x-2}}$$

**Метод:** подстановка $t = \sqrt{x-2}$.

Пусть $t = \sqrt{x-2}$, тогда $x = t^2+2$, $dx = 2t\,dt$.

$$\int \frac{(6-t^2-2)}{(t^2+2)\cdot t}\cdot 2t\,dt = 2\int \frac{4-t^2}{t^2+2}\,dt$$

Выделим целую часть:

$$\frac{4-t^2}{t^2+2} = \frac{-(t^2+2)+6}{t^2+2} = -1 + \frac{6}{t^2+2}$$

$$2\int\!\left(-1 + \frac{6}{t^2+2}\right)dt = 2\left(-t + \frac{6}{\sqrt{2}}\arctan\frac{t}{\sqrt{2}}\right) + C = -2t + 6\sqrt{2}\arctan\frac{t}{\sqrt{2}} + C$$

Возвращаясь к $x$: $t = \sqrt{x-2}$, $\dfrac{t}{\sqrt{2}} = \sqrt{\dfrac{x-2}{2}}$.

**Ответ:**

$$\boxed{-2\sqrt{x-2} + 6\sqrt{2}\arctan\!\sqrt{\frac{x-2}{2}} + C}$$

---

## Задача 6

$$\int \frac{\sqrt{x+6}\,dx}{4x+1}$$

**Метод:** подстановка $t = \sqrt{x+6}$.

Пусть $t = \sqrt{x+6}$, тогда $x = t^2-6$, $dx = 2t\,dt$, $4x+1 = 4t^2-23$.

$$\int \frac{t\cdot 2t\,dt}{4t^2-23} = 2\int\frac{t^2}{4t^2-23}\,dt$$

Выделим целую часть:

$$\frac{2t^2}{4t^2-23} = \frac{1}{2} + \frac{23}{2(4t^2-23)}$$

$$\int\frac{2t^2}{4t^2-23}\,dt = \frac{t}{2} + \frac{23}{2}\int\frac{dt}{4t^2-23}$$

Вычислим $\int\dfrac{dt}{4t^2-23}$. Поскольку $4t^2-23 = 4\!\left(t^2-\dfrac{23}{4}\right)$:

$$\int\frac{dt}{4t^2-23} = \frac{1}{4}\int\frac{dt}{t^2-\left(\frac{\sqrt{23}}{2}\right)^2} = \frac{1}{4}\cdot\frac{1}{\sqrt{23}}\ln\left|\frac{2t-\sqrt{23}}{2t+\sqrt{23}}\right|$$

Итого:

$$\frac{t}{2} + \frac{23}{8\sqrt{23}}\ln\left|\frac{2t-\sqrt{23}}{2t+\sqrt{23}}\right| + C = \frac{t}{2} + \frac{\sqrt{23}}{8}\ln\left|\frac{2t-\sqrt{23}}{2t+\sqrt{23}}\right| + C$$

Возвращаясь к $x$: $t = \sqrt{x+6}$.

**Ответ:**

$$\boxed{\frac{\sqrt{x+6}}{2} + \frac{\sqrt{23}}{8}\ln\left|\frac{2\sqrt{x+6}-\sqrt{23}}{2\sqrt{x+6}+\sqrt{23}}\right| + C}$$

---

## Задача 7

$$\int \frac{dx}{(1-9x)\sqrt{x}}$$

**Метод:** подстановка $t = \sqrt{x}$.

Пусть $t = \sqrt{x}$, тогда $x = t^2$, $dx = 2t\,dt$.

$$\int\frac{2t\,dt}{(1-9t^2)\cdot t} = 2\int\frac{dt}{1-9t^2}$$

Разложим на простые дроби: $\dfrac{1}{1-9t^2} = \dfrac{1}{(1-3t)(1+3t)}$.

Методом неопределённых коэффициентов: $\dfrac{1}{2}\cdot\dfrac{1}{1-3t} + \dfrac{1}{2}\cdot\dfrac{1}{1+3t}$.

$$2\int\!\left(\frac{1/2}{1-3t} + \frac{1/2}{1+3t}\right)dt = -\frac{1}{3}\ln|1-3t| + \frac{1}{3}\ln|1+3t| + C = \frac{1}{3}\ln\left|\frac{1+3t}{1-3t}\right| + C$$

Возвращаясь к $x$: $t = \sqrt{x}$.

**Ответ:**

$$\boxed{\frac{1}{3}\ln\left|\frac{1+3\sqrt{x}}{1-3\sqrt{x}}\right| + C}$$

---

## Задача 8

$$\int \frac{4\cdot 19^x+1}{5\cdot 19^x+1}\,dx$$

**Метод:** выделение целой части, затем логарифмическое интегрирование.

Запишем $4\cdot 19^x + 1 = A(5\cdot 19^x + 1) + B$:

$$A = \frac{4}{5},\quad B = 1 - A = \frac{1}{5}$$

$$\frac{4\cdot 19^x+1}{5\cdot 19^x+1} = \frac{4}{5} + \frac{1}{5(5\cdot 19^x+1)}$$

$$\int\frac{4\cdot 19^x+1}{5\cdot 19^x+1}\,dx = \frac{4x}{5} + \frac{1}{5}\int\frac{dx}{5\cdot 19^x+1}$$

Для оставшегося интеграла сделаем подстановку $t = 19^x$, $dt = 19^x\ln 19\,dx$:

$$\int\frac{dx}{5\cdot 19^x+1} = \frac{1}{\ln 19}\int\frac{dt}{t(5t+1)} = \frac{1}{\ln 19}\int\!\left(\frac{1}{t} - \frac{5}{5t+1}\right)dt = \frac{1}{\ln 19}\ln\left|\frac{t}{5t+1}\right| + C$$

Подставляя обратно:

$$= \frac{4x}{5} + \frac{1}{5\ln 19}\ln\frac{19^x}{5\cdot 19^x+1} + C = \frac{4x}{5} + \frac{1}{5\ln 19}\bigl(x\ln 19 - \ln(5\cdot 19^x+1)\bigr) + C$$

$$= \frac{4x}{5} + \frac{x}{5} - \frac{\ln(5\cdot 19^x+1)}{5\ln 19} + C$$

**Ответ:**

$$\boxed{x - \frac{\ln(5\cdot 19^x+1)}{5\ln 19} + C}$$

---

## Задача 9

$$\int e^{-\sqrt{6-x}}\,dx$$

**Метод:** подстановка $t = \sqrt{6-x}$, затем интегрирование по частям.

Пусть $t = \sqrt{6-x}$, тогда $x = 6-t^2$, $dx = -2t\,dt$.

$$\int e^{-t}(-2t)\,dt = -2\int t e^{-t}\,dt$$

Интегрирование по частям ($u = t$, $dv = e^{-t}dt$, $v = -e^{-t}$):

$$-2\!\left[-te^{-t} - \int(-e^{-t})\,dt\right] = -2\!\left[-te^{-t} - e^{-t}\right] = 2e^{-t}(t+1) + C$$

Возвращаясь к $x$: $t = \sqrt{6-x}$.

**Ответ:**

$$\boxed{2e^{-\sqrt{6-x}}\!\left(\sqrt{6-x}+1\right) + C}$$

---

## Задача 10

$$\int x^2\operatorname{arctg}(6x)\,dx$$

**Метод:** интегрирование по частям, затем подстановка.

$u = \operatorname{arctg}(6x)$, $dv = x^2\,dx$, $du = \dfrac{6\,dx}{1+36x^2}$, $v = \dfrac{x^3}{3}$:

$$= \frac{x^3}{3}\operatorname{arctg}(6x) - 2\int\frac{x^3\,dx}{1+36x^2}$$

Вычислим $\int\dfrac{x^3\,dx}{1+36x^2}$. Подстановка $t = 1+36x^2$, $dt = 72x\,dx$, $x^2 = \dfrac{t-1}{36}$:

$$\int\frac{x^3}{1+36x^2}\,dx = \int\frac{x^2\cdot x\,dx}{1+36x^2} = \int\frac{(t-1)}{36t}\cdot\frac{dt}{72} = \frac{1}{2592}\int\!\left(1-\frac{1}{t}\right)dt = \frac{1+36x^2-\ln(1+36x^2)}{2592}$$

Подставляя:

$$\frac{x^3}{3}\operatorname{arctg}(6x) - \frac{2(1+36x^2)}{2592} + \frac{2\ln(1+36x^2)}{2592} + C$$

Константа $-\dfrac{2}{2592} = -\dfrac{1}{1296}$ поглощается в $C$, $\dfrac{72x^2}{2592} = \dfrac{x^2}{36}$:

**Ответ:**

$$\boxed{\frac{x^3}{3}\operatorname{arctg}(6x) - \frac{x^2}{36} + \frac{\ln(1+36x^2)}{1296} + C}$$

---

## Задача 11

$$\int (x-\ln x)^2\,dx$$

**Метод:** раскрытие скобок, интегрирование по частям.

Раскроем квадрат:

$$(x-\ln x)^2 = x^2 - 2x\ln x + \ln^2 x$$

**Слагаемое $\int x^2\,dx$:**

$$\frac{x^3}{3}$$

**Слагаемое $\int x\ln x\,dx$** (IBP: $u=\ln x$, $dv = x\,dx$):

$$\frac{x^2}{2}\ln x - \int\frac{x}{2}\,dx = \frac{x^2\ln x}{2} - \frac{x^2}{4}$$

**Слагаемое $\int\ln^2 x\,dx$** (IBP: $u = \ln^2 x$, $dv=dx$):

$$x\ln^2 x - 2\int\ln x\,dx = x\ln^2 x - 2(x\ln x - x) = x\ln^2 x - 2x\ln x + 2x$$

Собираем всё вместе:

$$\frac{x^3}{3} - 2\!\left(\frac{x^2\ln x}{2} - \frac{x^2}{4}\right) + x\ln^2 x - 2x\ln x + 2x + C$$

**Ответ:**

$$\boxed{\frac{x^3}{3} - x^2\ln x + \frac{x^2}{2} + x\ln^2 x - 2x\ln x + 2x + C}$$

---

## Задача 12

$$\int e^{-x}\operatorname{arctg}(e^x)\,dx$$

**Метод:** интегрирование по частям.

$u = \operatorname{arctg}(e^x)$, $dv = e^{-x}dx$, $du = \dfrac{e^x}{1+e^{2x}}dx$, $v = -e^{-x}$:

$$= -e^{-x}\operatorname{arctg}(e^x) + \int\frac{e^{-x}\cdot e^x\,dx}{1+e^{2x}} = -e^{-x}\operatorname{arctg}(e^x) + \int\frac{dx}{1+e^{2x}}$$

Вычислим $\int\dfrac{dx}{1+e^{2x}}$. Подстановка $u = e^x$, $du = e^x\,dx$:

$$\int\frac{du}{u(1+u^2)} = \int\!\left(\frac{1}{u} - \frac{u}{1+u^2}\right)du = \ln u - \frac{\ln(1+u^2)}{2} = x - \frac{\ln(1+e^{2x})}{2}$$

**Ответ:**

$$\boxed{-e^{-x}\operatorname{arctg}(e^x) + x - \frac{\ln(1+e^{2x})}{2} + C}$$

---

## Задача 13

$$\int \frac{(6x-1)\,dx}{x^2-x-1}$$

**Метод:** выделение логарифмической части и интеграла от дроби $\dfrac{1}{x^2-x-1}$.

Запишем $6x-1 = 3(2x-1) + 2$:

$$\int\frac{6x-1}{x^2-x-1}\,dx = 3\int\frac{2x-1}{x^2-x-1}\,dx + 2\int\frac{dx}{x^2-x-1}$$

Первый интеграл: числитель — производная знаменателя, поэтому

$$3\int\frac{(x^2-x-1)'}{x^2-x-1}\,dx = 3\ln|x^2-x-1|$$

Второй интеграл: выделим полный квадрат

$$x^2-x-1 = \left(x-\frac{1}{2}\right)^2 - \frac{5}{4}$$

$$\int\frac{dx}{\left(x-\frac{1}{2}\right)^2-\left(\frac{\sqrt{5}}{2}\right)^2} = \frac{1}{\sqrt{5}}\ln\left|\frac{x-\dfrac{1}{2}-\dfrac{\sqrt{5}}{2}}{x-\dfrac{1}{2}+\dfrac{\sqrt{5}}{2}}\right| = \frac{1}{\sqrt{5}}\ln\left|\frac{2x-1-\sqrt{5}}{2x-1+\sqrt{5}}\right|$$

**Ответ:**

$$\boxed{3\ln|x^2-x-1| + \frac{2}{\sqrt{5}}\ln\left|\frac{2x-1-\sqrt{5}}{2x-1+\sqrt{5}}\right| + C}$$

---

## Задача 14

$$\int \frac{(x+1)\,dx}{\sqrt{x+4x^2}}$$

**Метод:** выделение части с логарифмической производной знаменателя.

$(4x^2+x)' = 8x+1$. Запишем $x+1 = A(8x+1) + B$:

$$8A = 1 \Rightarrow A = \frac{1}{8},\quad A+B = 1 \Rightarrow B = \frac{7}{8}$$

$$\int\frac{x+1}{\sqrt{4x^2+x}}\,dx = \frac{1}{8}\int\frac{8x+1}{\sqrt{4x^2+x}}\,dx + \frac{7}{8}\int\frac{dx}{\sqrt{4x^2+x}}$$

**Первый интеграл:** по формуле $\int\dfrac{f'}{2\sqrt{f}} = \sqrt{f}$:

$$\frac{1}{8}\cdot 2\sqrt{4x^2+x} = \frac{\sqrt{4x^2+x}}{4}$$

**Второй интеграл:** дополним до полного квадрата

$$4x^2+x = 4\!\left(x+\frac{1}{8}\right)^2 - \frac{1}{16}$$

$$\int\frac{dx}{\sqrt{4x^2+x}} = \frac{1}{2}\int\frac{dx}{\sqrt{\left(x+\frac{1}{8}\right)^2-\frac{1}{64}}} = \frac{1}{2}\ln\left|x+\frac{1}{8}+\sqrt{\left(x+\frac{1}{8}\right)^2-\frac{1}{64}}\right|$$

$$= \frac{1}{2}\ln\left|8x+1+4\sqrt{4x^2+x}\right| + C_1$$

Итого:

$$\frac{\sqrt{4x^2+x}}{4} + \frac{7}{8}\cdot\frac{1}{2}\ln\left|8x+1+4\sqrt{4x^2+x}\right| + C$$

**Ответ:**

$$\boxed{\frac{\sqrt{x+4x^2}}{4} + \frac{7}{16}\ln\!\left|8x+1+4\sqrt{x+4x^2}\right| + C}$$

---

## Задача 15

$$\int \frac{dx}{x\sqrt{6x-x^2}}$$

**Метод:** подстановка $x = 1/t$.

Пусть $x = \dfrac{1}{t}$, тогда $dx = -\dfrac{dt}{t^2}$. Выразим:

$$6x - x^2 = \frac{6}{t} - \frac{1}{t^2} = \frac{6t-1}{t^2},\qquad \sqrt{6x-x^2} = \frac{\sqrt{6t-1}}{t}\quad(t>0)$$

$$\int\frac{dx}{x\sqrt{6x-x^2}} = \int\frac{-dt/t^2}{(1/t)\cdot(\sqrt{6t-1}/t)} = \int\frac{-dt}{\sqrt{6t-1}} = -\frac{\sqrt{6t-1}}{3} + C$$

Возвращаясь к $x$: $6t-1 = \dfrac{6}{x}-1 = \dfrac{6-x}{x}$.

$$-\frac{1}{3}\sqrt{\frac{6-x}{x}} + C$$

**Ответ:**

$$\boxed{-\frac{1}{3}\sqrt{\frac{6-x}{x}} + C}$$

---

## Задача 16

$$\int \frac{(7x^2+9)\,dx}{(x+6)(x^2-11x+30)}$$

**Метод:** разложение на простые дроби.

Заметим, что $x^2-11x+30 = (x-5)(x-6)$, поэтому знаменатель равен $(x+6)(x-5)(x-6)$.

Разложение:

$$\frac{7x^2+9}{(x+6)(x-5)(x-6)} = \frac{A}{x+6} + \frac{B}{x-5} + \frac{C}{x-6}$$

Умножаем обе части на знаменатель:

$$7x^2+9 = A(x-5)(x-6) + B(x+6)(x-6) + C(x+6)(x-5)$$

При $x = -6$: $\ 7\cdot 36+9 = 261 = A(-11)(-12) = 132A\ \Rightarrow\ A = \dfrac{261}{132} = \dfrac{87}{44}$

При $x = 5$: $\ 7\cdot 25+9 = 184 = B(11)(-1) = -11B\ \Rightarrow\ B = -\dfrac{184}{11}$

При $x = 6$: $\ 7\cdot 36+9 = 261 = C(12)(1) = 12C\ \Rightarrow\ C = \dfrac{261}{12} = \dfrac{87}{4}$

**Ответ:**

$$\boxed{\frac{87}{44}\ln|x+6| - \frac{184}{11}\ln|x-5| + \frac{87}{4}\ln|x-6| + C}$$

---

## Задача 17

$$\int \frac{dx}{[x(x+3)]^2} = \int\frac{dx}{x^2(x+3)^2}$$

**Метод:** разложение на простые дроби.

$$\frac{1}{x^2(x+3)^2} = \frac{A}{x} + \frac{B}{x^2} + \frac{C}{x+3} + \frac{D}{(x+3)^2}$$

$$1 = Ax(x+3)^2 + B(x+3)^2 + Cx^2(x+3) + Dx^2$$

При $x=0$: $1 = 9B \Rightarrow B = \dfrac{1}{9}$

При $x=-3$: $1 = 9D \Rightarrow D = \dfrac{1}{9}$

Из коэффициента при $x^3$: $A + C = 0$.

Из коэффициента при $x$: $9A + 6B = 0 \Rightarrow A = -\dfrac{2}{27}$, $C = \dfrac{2}{27}$.

$$\int\frac{dx}{x^2(x+3)^2} = -\frac{2}{27}\ln|x| - \frac{1}{9x} + \frac{2}{27}\ln|x+3| - \frac{1}{9(x+3)} + C$$

Объединяем рациональные слагаемые:

$$-\frac{1}{9x} - \frac{1}{9(x+3)} = -\frac{2x+3}{9x(x+3)}$$

**Ответ:**

$$\boxed{\frac{2}{27}\ln\left|\frac{x+3}{x}\right| - \frac{2x+3}{9x(x+3)} + C}$$

---

## Задача 18

$$\int \frac{x\,dx}{x^3+2x^2+3x+6}$$

**Метод:** факторизация знаменателя, разложение на простые дроби.

Группируем: $x^3+2x^2+3x+6 = x^2(x+2)+3(x+2) = (x^2+3)(x+2)$.

$$\frac{x}{(x+2)(x^2+3)} = \frac{A}{x+2} + \frac{Bx+C}{x^2+3}$$

При $x=-2$: $-2 = 7A \Rightarrow A = -\dfrac{2}{7}$.

Из коэффициентов: $A+B = 0 \Rightarrow B = \dfrac{2}{7}$; $\quad 2B+C = 1 \Rightarrow C = \dfrac{3}{7}$.

$$\int\frac{x\,dx}{(x+2)(x^2+3)} = -\frac{2}{7}\ln|x+2| + \frac{1}{7}\int\frac{2x+3}{x^2+3}\,dx$$

Разбиваем: $\dfrac{2x+3}{x^2+3} = \dfrac{2x}{x^2+3} + \dfrac{3}{x^2+3}$:

$$\frac{1}{7}\int\frac{2x}{x^2+3}\,dx = \frac{\ln(x^2+3)}{7}$$

$$\frac{3}{7}\int\frac{dx}{x^2+3} = \frac{3}{7}\cdot\frac{1}{\sqrt{3}}\arctan\frac{x}{\sqrt{3}} = \frac{\sqrt{3}}{7}\arctan\frac{x}{\sqrt{3}}$$

**Ответ:**

$$\boxed{-\frac{2}{7}\ln|x+2| + \frac{\ln(x^2+3)}{7} + \frac{\sqrt{3}}{7}\arctan\frac{x}{\sqrt{3}} + C}$$

---

## Задача 19

$$\int \cos^5(8x)\,dx$$

**Метод:** понижение степени, подстановка.

$$\int\cos^5(8x)\,dx = \int\cos^4(8x)\cdot\cos(8x)\,dx = \int\!\left(1-\sin^2(8x)\right)^2\!\cos(8x)\,dx$$

Раскроем скобки:

$$= \int\!\left(1-2\sin^2(8x)+\sin^4(8x)\right)\cos(8x)\,dx$$

Подстановка $t = \sin(8x)$, $dt = 8\cos(8x)\,dx$:

$$\frac{1}{8}\int\!\left(1-2t^2+t^4\right)dt = \frac{1}{8}\!\left(t - \frac{2t^3}{3} + \frac{t^5}{5}\right) + C$$

**Ответ:**

$$\boxed{\frac{\sin(8x)}{8} - \frac{\sin^3(8x)}{12} + \frac{\sin^5(8x)}{40} + C}$$

---

## Задача 20

$$\int \sin^2(7x)\cos^6(7x)\,dx$$

**Метод:** понижение степени через формулы кратных углов.

Сделаем замену $\theta = 7x$ (потом вернёмся). Используем тождества:

$$\sin^2\theta\cos^6\theta = \cos^4\theta\cdot\underbrace{\sin^2\theta\cos^2\theta}_{\frac{\sin^2 2\theta}{4}} = \frac{1}{4}\cos^4\theta\cdot\sin^2 2\theta$$

Выразим $\cos^4\theta = \dfrac{3+4\cos 2\theta+\cos 4\theta}{8}$ и $\sin^2 2\theta = \dfrac{1-\cos 4\theta}{2}$, перемножим и раскроем:

$$\sin^2\theta\cos^6\theta = \frac{(3+4\cos 2\theta+\cos 4\theta)\sin^2 2\theta}{32}$$

Раскрываем произведение (применяя формулы произведения косинусов):

$$3\sin^2 2\theta = \frac{3}{2} - \frac{3\cos 4\theta}{2}$$

$$4\cos 2\theta\sin^2 2\theta = \cos 2\theta - \cos 6\theta$$

$$\cos 4\theta\sin^2 2\theta = \frac{\cos 4\theta}{2} - \frac{1}{4} - \frac{\cos 8\theta}{4}$$

Суммируем:

$$\sin^2\theta\cos^6\theta = \frac{1}{32}\!\left(\frac{5}{4} + \cos 2\theta - \cos 4\theta - \cos 6\theta - \frac{\cos 8\theta}{4}\right)$$

Интегрируем по $\theta$, затем учитываем $\theta = 7x$ ($d\theta = 7\,dx$):

$$\int\sin^2(7x)\cos^6(7x)\,dx = \frac{1}{7}\int\sin^2\theta\cos^6\theta\,d\theta = \frac{1}{224}\!\left[\frac{5\theta}{4}+\frac{\sin 2\theta}{2}-\frac{\sin 4\theta}{4}-\frac{\sin 6\theta}{6}-\frac{\sin 8\theta}{32}\right] + C$$

Подставляя $\theta = 7x$:

**Ответ:**

$$\boxed{\frac{5x}{128} + \frac{\sin(14x)}{448} - \frac{\sin(28x)}{896} - \frac{\sin(42x)}{1344} - \frac{\sin(56x)}{7168} + C}$$

---

## Задача 21

$$\int \operatorname{tg}^6(3x)\,dx$$

**Метод:** рекуррентное понижение степени через $\operatorname{tg}^2 = \sec^2 - 1$.

$$\operatorname{tg}^6 = \operatorname{tg}^4(\sec^2-1) = \operatorname{tg}^4\sec^2 - \operatorname{tg}^4$$

$$\operatorname{tg}^4 = \operatorname{tg}^2(\sec^2-1) = \operatorname{tg}^2\sec^2 - \operatorname{tg}^2 = \operatorname{tg}^2\sec^2 - \sec^2+1$$

Итого:

$$\operatorname{tg}^6(3x) = \operatorname{tg}^4(3x)\sec^2(3x) - \operatorname{tg}^2(3x)\sec^2(3x) + \sec^2(3x) - 1$$

Каждое слагаемое интегрируем (используя $\int\operatorname{tg}^n\sec^2 u\,du = \dfrac{\operatorname{tg}^{n+1}u}{n+1}$, $u=3x$, и деля на $3$):

$$\int\operatorname{tg}^6(3x)\,dx = \frac{1}{3}\!\left[\frac{\operatorname{tg}^5(3x)}{5} - \frac{\operatorname{tg}^3(3x)}{3} + \operatorname{tg}(3x)\right] - x + C$$

**Ответ:**

$$\boxed{\frac{\operatorname{tg}^5(3x)}{15} - \frac{\operatorname{tg}^3(3x)}{9} + \frac{\operatorname{tg}(3x)}{3} - x + C}$$

---

## Задача 22

$$\int \frac{\cos^{1/13}x\,dx}{\sin^{27/13}x}$$

**Метод:** представление через $\operatorname{ctg}$ и $\csc^2$.

Запишем $\dfrac{27}{13} = \dfrac{1}{13} + 2$:

$$\frac{\cos^{1/13}x}{\sin^{27/13}x} = \frac{\cos^{1/13}x}{\sin^{1/13}x\cdot\sin^2 x} = \operatorname{ctg}^{1/13}x\cdot\csc^2 x$$

Подстановка $t = \operatorname{ctg}\,x$, $dt = -\csc^2 x\,dx$:

$$\int\operatorname{ctg}^{1/13}x\cdot\csc^2 x\,dx = -\int t^{1/13}\,dt = -\frac{t^{14/13}}{14/13} + C = -\frac{13}{14}\operatorname{ctg}^{14/13}x + C$$

**Ответ:**

$$\boxed{-\frac{13}{14}\operatorname{ctg}^{14/13}x + C}$$

---

## Задача 23

$$\int \frac{dx}{\sin x\cos^3 x}$$

**Метод:** умножение и деление на $\cos^4 x$, подстановка $t = \operatorname{tg}\,x$.

$$\frac{1}{\sin x\cos^3 x}\cdot\frac{\sec^4 x}{\sec^4 x} = \frac{\sec^4 x}{\operatorname{tg}\,x} = \frac{(1+\operatorname{tg}^2 x)\sec^2 x}{\operatorname{tg}\,x} = \frac{\sec^2 x}{\operatorname{tg}\,x} + \operatorname{tg}\,x\sec^2 x$$

Подстановка $t = \operatorname{tg}\,x$, $dt = \sec^2 x\,dx$:

$$\int\frac{\sec^2 x}{\operatorname{tg}\,x}\,dx + \int\operatorname{tg}\,x\sec^2 x\,dx = \int\frac{dt}{t} + \int t\,dt = \ln|\operatorname{tg}\,x| + \frac{\operatorname{tg}^2 x}{2} + C$$

**Ответ:**

$$\boxed{\ln|\operatorname{tg}\,x| + \frac{\operatorname{tg}^2 x}{2} + C}$$

---

## Задача 24

$$\int \frac{dx}{7\sin^2(10x)-\cos(20x)}$$

**Метод:** упрощение знаменателя, подстановка $t = \operatorname{tg}(10x)$.

Применяем $\cos(20x) = 1-2\sin^2(10x)$:

$$7\sin^2(10x)-\cos(20x) = 7\sin^2(10x)-(1-2\sin^2(10x)) = 9\sin^2(10x)-1$$

Используем тождество $\sin^2+\cos^2=1$:

$$9\sin^2(10x)-1 = 8\sin^2(10x)-\cos^2(10x) = \cos^2(10x)\!\left(8\operatorname{tg}^2(10x)-1\right)$$

Следовательно:

$$\int\frac{dx}{\cos^2(10x)\!\left(8\operatorname{tg}^2(10x)-1\right)} = \int\frac{\sec^2(10x)\,dx}{8\operatorname{tg}^2(10x)-1}$$

Подстановка $t = \operatorname{tg}(10x)$, $dt = 10\sec^2(10x)\,dx$:

$$\frac{1}{10}\int\frac{dt}{8t^2-1} = \frac{1}{10}\cdot\frac{1}{8}\int\frac{dt}{t^2-\frac{1}{8}}$$

Используем $\int\dfrac{dt}{t^2-a^2} = \dfrac{1}{2a}\ln\left|\dfrac{t-a}{t+a}\right|$ с $a = \dfrac{1}{2\sqrt{2}}$:

$$\frac{1}{80}\cdot\sqrt{2}\cdot\ln\left|\frac{t-\frac{1}{2\sqrt{2}}}{t+\frac{1}{2\sqrt{2}}}\right| = \frac{\sqrt{2}}{80}\ln\left|\frac{2\sqrt{2}\,t-1}{2\sqrt{2}\,t+1}\right|$$

**Ответ:**

$$\boxed{\frac{\sqrt{2}}{80}\ln\left|\frac{2\sqrt{2}\operatorname{tg}(10x)-1}{2\sqrt{2}\operatorname{tg}(10x)+1}\right| + C}$$

---

## Задача 25

$$\int \frac{\sin x\,dx}{\sin x+4}$$

**Метод:** выделение целой части, подстановка Вейерштрасса.

$$\frac{\sin x}{\sin x+4} = 1 - \frac{4}{\sin x+4}$$

$$\int\frac{\sin x\,dx}{\sin x+4} = x - 4\int\frac{dx}{\sin x+4}$$

Подстановка Вейерштрасса: $t = \operatorname{tg}\dfrac{x}{2}$, $\sin x = \dfrac{2t}{1+t^2}$, $dx = \dfrac{2\,dt}{1+t^2}$:

$$\int\frac{dx}{\sin x+4} = \int\frac{\frac{2}{1+t^2}}{\frac{2t}{1+t^2}+4}\,dt = \int\frac{dt}{2t^2+t+2}$$

Выделяем полный квадрат: $2t^2+t+2 = 2\!\left(t+\dfrac{1}{4}\right)^2+\dfrac{15}{8}$.

$$\int\frac{dt}{2t^2+t+2} = \frac{1}{2}\int\frac{dt}{\left(t+\frac{1}{4}\right)^2+\frac{15}{16}} = \frac{1}{2}\cdot\frac{4}{\sqrt{15}}\arctan\frac{4t+1}{\sqrt{15}} = \frac{2}{\sqrt{15}}\arctan\frac{4\operatorname{tg}\frac{x}{2}+1}{\sqrt{15}}$$

**Ответ:**

$$\boxed{x - \frac{8}{\sqrt{15}}\arctan\frac{4\operatorname{tg}\frac{x}{2}+1}{\sqrt{15}} + C}$$

---

## Задача 26

$$\int \cos^2(2x)\sin(3x)\,dx$$

**Метод:** понижение степени, формула произведения.

$$\cos^2(2x) = \frac{1+\cos(4x)}{2}$$

$$\int\cos^2(2x)\sin(3x)\,dx = \frac{1}{2}\int\sin(3x)\,dx + \frac{1}{2}\int\cos(4x)\sin(3x)\,dx$$

$$\frac{1}{2}\int\sin(3x)\,dx = -\frac{\cos(3x)}{6}$$

Для второго интеграла используем $\cos\alpha\sin\beta = \dfrac{\sin(\alpha+\beta)-\sin(\alpha-\beta)}{2}$... 

Или напрямую: $\cos 4x\sin 3x = \dfrac{\sin(7x)+\sin(-x)}{2} = \dfrac{\sin(7x)-\sin x}{2}$.

$$\frac{1}{2}\int\cos(4x)\sin(3x)\,dx = \frac{1}{4}\int(\sin(7x)-\sin x)\,dx = \frac{1}{4}\!\left(-\frac{\cos(7x)}{7}+\cos x\right)$$

$$= -\frac{\cos(7x)}{28} + \frac{\cos x}{4}$$

**Ответ:**

$$\boxed{-\frac{\cos(3x)}{6} - \frac{\cos(7x)}{28} + \frac{\cos x}{4} + C}$$

---

## Задача 27

$$\int \frac{dx}{x^2\sqrt{x^2-40}}$$

**Метод:** тригонометрическая подстановка $x = 2\sqrt{10}\sec\theta$.

Пусть $x = 2\sqrt{10}\sec\theta$, тогда $dx = 2\sqrt{10}\sec\theta\tan\theta\,d\theta$, $\sqrt{x^2-40} = 2\sqrt{10}\tan\theta$.

$$\int\frac{2\sqrt{10}\sec\theta\tan\theta\,d\theta}{40\sec^2\theta\cdot 2\sqrt{10}\tan\theta} = \int\frac{d\theta}{40\sec\theta} = \frac{1}{40}\int\cos\theta\,d\theta = \frac{\sin\theta}{40} + C$$

Из прямоугольного треугольника: $\sec\theta = \dfrac{x}{2\sqrt{10}}$, поэтому $\sin\theta = \dfrac{\sqrt{x^2-40}}{x}$.

**Ответ:**

$$\boxed{\frac{\sqrt{x^2-40}}{40x} + C}$$

---

## Задача 28

$$\int \frac{x^2\,dx}{\sqrt{(x^2+4)^5}}$$

**Метод:** тригонометрическая подстановка $x = 2\tan\theta$.

Пусть $x = 2\tan\theta$, $dx = 2\sec^2\theta\,d\theta$, $x^2+4 = 4\sec^2\theta$.

$$(x^2+4)^{5/2} = 4^{5/2}\sec^5\theta = 32\sec^5\theta$$

$$\int\frac{4\tan^2\theta\cdot 2\sec^2\theta\,d\theta}{32\sec^5\theta} = \frac{1}{4}\int\frac{\tan^2\theta}{\sec^3\theta}\,d\theta = \frac{1}{4}\int\sin^2\theta\cos\theta\,d\theta$$

Подстановка $u = \sin\theta$:

$$\frac{1}{4}\int u^2\,du = \frac{\sin^3\theta}{12} + C$$

Из прямоугольного треугольника: $\tan\theta = \dfrac{x}{2}$, $\sin\theta = \dfrac{x}{\sqrt{x^2+4}}$.

**Ответ:**

$$\boxed{\frac{x^3}{12(x^2+4)^{3/2}} + C}$$

---

## Задача 29

$$\int \frac{x^2\,dx}{\sqrt{(19-x^2)^3}}$$

**Метод:** тригонометрическая подстановка $x = \sqrt{19}\sin\theta$.

Пусть $x = \sqrt{19}\sin\theta$, $dx = \sqrt{19}\cos\theta\,d\theta$, $19-x^2 = 19\cos^2\theta$.

$$(19-x^2)^{3/2} = 19^{3/2}\cos^3\theta$$

$$\int\frac{19\sin^2\theta\cdot\sqrt{19}\cos\theta\,d\theta}{19^{3/2}\cos^3\theta} = \int\frac{\sin^2\theta}{\cos^2\theta}\,d\theta = \int\operatorname{tg}^2\theta\,d\theta = \int(\sec^2\theta-1)\,d\theta = \operatorname{tg}\theta - \theta + C$$

Из прямоугольного треугольника: $\sin\theta = \dfrac{x}{\sqrt{19}}$, $\operatorname{tg}\theta = \dfrac{x}{\sqrt{19-x^2}}$, $\theta = \arcsin\dfrac{x}{\sqrt{19}}$.

**Ответ:**

$$\boxed{\frac{x}{\sqrt{19-x^2}} - \arcsin\frac{x}{\sqrt{19}} + C}$$
