Привет! Я подготовил подробные пошаговые решения для всех 29 интегралов из твоего варианта. Решения оформлены с использованием LaTeX для математических формул, как ты и просил.

---

### Интеграл 1

**Задание:**


$$\int\frac{dx}{x\ln^{41}x}$$


**Решение:**
Выполним замену переменной. Пусть $u=\ln x$, тогда дифференциал $du=\frac{1}{x}dx$.
Подставим в интеграл:


$$\int u^{-41}du$$


Интегрируем по формуле степенной функции:


$$\int u^{-41}du=\frac{u^{-40}}{-40}+C$$


Возвращаемся к исходной переменной $x$:


$$-\frac{1}{40\ln^{40}x}+C$$


**Ответ:** $-\frac{1}{40\ln^{40}x}+C$

---

### Интеграл 2

**Задание:**


$$\int\sqrt{\frac{8-\arcsin x}{1-x^2}}dx$$


**Решение:**
Перепишем подынтегральное выражение в более удобном виде:


$$\int(8-\arcsin x)^{1/2}\frac{1}{\sqrt{1-x^2}}dx$$


Сделаем замену $u=8-\arcsin x$. Тогда $du=-\frac{1}{\sqrt{1-x^2}}dx$, откуда $\frac{dx}{\sqrt{1-x^2}}=-du$.
Подставляем в интеграл:


$$\int u^{1/2}(-du)=-\frac{u^{3/2}}{3/2}+C=-\frac{2}{3}u^{3/2}+C$$


Возвращаемся к $x$:


$$-\frac{2}{3}(8-\arcsin x)^{3/2}+C$$


**Ответ:** $-\frac{2}{3}(8-\arcsin x)^{3/2}+C$

---

### Интеграл 3

**Задание:**


$$\int\frac{x^8dx}{\cos^2(14x^9-2)}$$


**Решение:**
Сделаем замену $u=14x^9-2$. Тогда $du=126x^8dx$, откуда $x^8dx=\frac{du}{126}$.
Подставляем:


$$\int\frac{1}{\cos^2u}\frac{du}{126}=\frac{1}{126}\int\frac{du}{\cos^2u}$$


Это табличный интеграл:


$$\frac{1}{126}\operatorname{tg}u+C$$


Возвращаемся к $x$:


$$\frac{1}{126}\operatorname{tg}(14x^9-2)+C$$


**Ответ:** $\frac{1}{126}\operatorname{tg}(14x^9-2)+C$

---

### Интеграл 4

**Задание:**


$$\int 20^x\sin(7\cdot20^x)dx$$


**Решение:**
Сделаем замену $u=7\cdot20^x$. Тогда $du=7\cdot20^x\ln(20)dx$, откуда $20^xdx=\frac{du}{7\ln(20)}$.
Подставляем:


$$\int\sin(u)\frac{du}{7\ln(20)}=\frac{1}{7\ln(20)}\int\sin(u)du$$


Интегрируем:


$$-\frac{1}{7\ln(20)}\cos(u)+C$$


Возвращаемся к $x$:


$$-\frac{\cos(7\cdot20^x)}{7\ln(20)}+C$$


**Ответ:** $-\frac{\cos(7\cdot20^x)}{7\ln(20)}+C$

---

### Интеграл 5

**Задание:**


$$\int\frac{(6-x)dx}{x\sqrt{x-2}}$$


**Решение:**
Сделаем замену $u=\sqrt{x-2}$. Тогда $x=u^2+2$, а $dx=2udu$.
Подставим в интеграл:


$$\int\frac{6-(u^2+2)}{(u^2+2)u}2udu=2\int\frac{4-u^2}{u^2+2}du$$


Выделим целую часть дроби:


$$2\int\frac{6-(u^2+2)}{u^2+2}du=2\int\left(\frac{6}{u^2+2}-1\right)du=12\int\frac{du}{u^2+2}-2\int du$$


Интегрируем, применяя формулу для арктангенса:


$$12\frac{1}{\sqrt{2}}\operatorname{arctg}\left(\frac{u}{\sqrt{2}}\right)-2u+C=6\sqrt{2}\operatorname{arctg}\left(\frac{u}{\sqrt{2}}\right)-2u+C$$


Возвращаемся к $x$:


$$6\sqrt{2}\operatorname{arctg}\sqrt{\frac{x-2}{2}}-2\sqrt{x-2}+C$$


**Ответ:** $6\sqrt{2}\operatorname{arctg}\sqrt{\frac{x-2}{2}}-2\sqrt{x-2}+C$

---

### Интеграл 6

**Задание:**


$$\int\frac{\sqrt{x+6}dx}{4x+1}$$


**Решение:**
Сделаем замену $u=\sqrt{x+6}$, тогда $x=u^2-6$, а $dx=2udu$.
Знаменатель примет вид: $4(u^2-6)+1=4u^2-23$.
Подставляем:


$$\int\frac{u\cdot2udu}{4u^2-23}=2\int\frac{u^2}{4u^2-23}du=\frac{1}{2}\int\frac{4u^2-23+23}{4u^2-23}du$$

$$=\frac{1}{2}\int\left(1+\frac{23}{4u^2-23}\right)du=\frac{u}{2}+\frac{23}{2}\int\frac{du}{(2u)^2-(\sqrt{23})^2}$$


Применяем формулу "высокого логарифма":


$$\frac{u}{2}+\frac{23}{2}\frac{1}{2\sqrt{23}}\ln\left|\frac{2u-\sqrt{23}}{2u+\sqrt{23}}\right|+C$$


Возвращаемся к $x$:


$$\frac{\sqrt{x+6}}{2}+\frac{23}{4\sqrt{23}}\ln\left|\frac{2\sqrt{x+6}-\sqrt{23}}{2\sqrt{x+6}+\sqrt{23}}\right|+C$$


**Ответ:** $\frac{\sqrt{x+6}}{2}+\frac{\sqrt{23}}{4}\ln\left|\frac{2\sqrt{x+6}-\sqrt{23}}{2\sqrt{x+6}+\sqrt{23}}\right|+C$

---

### Интеграл 7

**Задание:**


$$\int\frac{dx}{(1-9x)\sqrt{x}}$$


**Решение:**
Сделаем замену $u=\sqrt{x}$, тогда $x=u^2$ и $dx=2udu$.
Подставляем:


$$\int\frac{2udu}{(1-9u^2)u}=2\int\frac{du}{1-9u^2}=2\int\frac{du}{1-(3u)^2}$$


Интегрируем:


$$2\cdot\frac{1}{3}\cdot\frac{1}{2}\ln\left|\frac{1+3u}{1-3u}\right|+C=\frac{1}{3}\ln\left|\frac{1+3u}{1-3u}\right|+C$$


Возвращаемся к $x$:


$$\frac{1}{3}\ln\left|\frac{1+3\sqrt{x}}{1-3\sqrt{x}}\right|+C$$


**Ответ:** $\frac{1}{3}\ln\left|\frac{1+3\sqrt{x}}{1-3\sqrt{x}}\right|+C$

---

### Интеграл 8

**Задание:**


$$\int\frac{4\cdot19^x+1}{5\cdot19^x+1}dx$$


**Решение:**
Представим числитель в виде линейной комбинации знаменателя и его производной:


$$4\cdot19^x+1=A(5\cdot19^x+1)+B(5\cdot19^x\ln19)$$


Приравнивая коэффициенты, получаем:
$A=1$ (свободный член), $5A+5B\ln19=4$, откуда $5+5B\ln19=4 \Rightarrow B=-\frac{1}{5\ln19}$.
Интеграл разбивается на две части:


$$\int\left(1-\frac{1}{5\ln19}\frac{5\cdot19^x\ln19}{5\cdot19^x+1}\right)dx$$


Интегрируем:


$$x-\frac{1}{5\ln19}\ln(5\cdot19^x+1)+C$$


**Ответ:** $x-\frac{1}{5\ln19}\ln(5\cdot19^x+1)+C$

---

### Интеграл 9

**Задание:**


$$\int e^{-\sqrt{6-x}}dx$$


**Решение:**
Замена $u=\sqrt{6-x}$, тогда $x=6-u^2$ и $dx=-2udu$.


$$\int e^{-u}(-2u)du=-2\int ue^{-u}du$$


Используем интегрирование по частям. Пусть $w=u$, $dv=e^{-u}du$. Тогда $dw=du$, $v=-e^{-u}$.


$$-2\left(-ue^{-u}-\int(-e^{-u})du\right)=-2(-ue^{-u}-e^{-u})+C=2e^{-u}(u+1)+C$$


Возвращаемся к $x$:


$$2e^{-\sqrt{6-x}}(\sqrt{6-x}+1)+C$$


**Ответ:** $2e^{-\sqrt{6-x}}(\sqrt{6-x}+1)+C$

---

### Интеграл 10

**Задание:**


$$\int x^2\operatorname{arctg}(6x)dx$$


**Решение:**
Интегрируем по частям. Пусть $u=\operatorname{arctg}(6x)$, $dv=x^2dx$. Тогда $du=\frac{6}{1+36x^2}dx$, $v=\frac{x^3}{3}$.


$$\int u dv=uv-\int v du=\frac{x^3}{3}\operatorname{arctg}(6x)-2\int\frac{x^3}{1+36x^2}dx$$


Рассмотрим $\int\frac{x^3}{1+36x^2}dx$. Выделим целую часть дроби:


$$x^3=\frac{x}{36}(36x^2+1-1)=\frac{x}{36}(1+36x^2)-\frac{x}{36}$$

$$\int\frac{x^3}{1+36x^2}dx=\int\left(\frac{x}{36}-\frac{x}{36(1+36x^2)}\right)dx=\frac{x^2}{72}-\frac{1}{36}\frac{1}{72}\ln(1+36x^2)$$


Подставляем обратно:


$$\frac{x^3}{3}\operatorname{arctg}(6x)-2\left(\frac{x^2}{72}-\frac{\ln(1+36x^2)}{2592}\right)+C$$

$$\frac{x^3}{3}\operatorname{arctg}(6x)-\frac{x^2}{36}+\frac{\ln(1+36x^2)}{1296}+C$$


**Ответ:** $\frac{x^3}{3}\operatorname{arctg}(6x)-\frac{x^2}{36}+\frac{\ln(1+36x^2)}{1296}+C$

---

### Интеграл 11

**Задание:**


$$\int(x-\ln x)^2dx$$


**Решение:**
Раскроем скобки:


$$\int(x^2-2x\ln x+\ln^2x)dx=\int x^2dx-2\int x\ln xdx+\int\ln^2xdx$$

1. $\int x^2dx=\frac{x^3}{3}$
2. Для $\int x\ln xdx$ по частям ($u=\ln x$, $dv=xdx \Rightarrow v=x^2/2$): $\frac{x^2}{2}\ln x-\int\frac{x}{2}dx=\frac{x^2}{2}\ln x-\frac{x^2}{4}$
3. Для $\int\ln^2xdx$ по частям ($u=\ln^2x$, $dv=dx$): $x\ln^2x-2\int\ln xdx=x\ln^2x-2(x\ln x-x)$
Суммируем всё:

$$\frac{x^3}{3}-2\left(\frac{x^2}{2}\ln x-\frac{x^2}{4}\right)+x\ln^2x-2x\ln x+2x+C$$



**Ответ:** $\frac{x^3}{3}-x^2\ln x+\frac{x^2}{2}+x\ln^2x-2x\ln x+2x+C$

---

### Интеграл 12

**Задание:**


$$\int e^{-x}\operatorname{arctg}(e^x)dx$$


**Решение:**
Интегрируем по частям. $u=\operatorname{arctg}(e^x) \Rightarrow du=\frac{e^x}{1+e^{2x}}dx$. $dv=e^{-x}dx \Rightarrow v=-e^{-x}$.


$$-e^{-x}\operatorname{arctg}(e^x)+\int\frac{1}{1+e^{2x}}dx$$


Во втором интеграле сделаем замену $t=e^x$, $dx=\frac{dt}{t}$:


$$\int\frac{dt}{t(1+t^2)}=\int\left(\frac{1}{t}-\frac{t}{1+t^2}\right)dt=\ln|t|-\frac{1}{2}\ln(1+t^2)=x-\frac{1}{2}\ln(1+e^{2x})$$


**Ответ:** $-e^{-x}\operatorname{arctg}(e^x)+x-\frac{1}{2}\ln(1+e^{2x})+C$

---

### Интеграл 13

**Задание:**


$$\int\frac{(6x-1)dx}{x^2-x-1}$$


**Решение:**
Производная знаменателя равна $2x-1$. Представим числитель: $6x-1=3(2x-1)+2$.


$$\int\frac{3(2x-1)+2}{x^2-x-1}dx=3\int\frac{2x-1}{x^2-x-1}dx+2\int\frac{dx}{(x-0.5)^2-1.25}$$

$$=3\ln|x^2-x-1|+2\int\frac{dx}{(x-1/2)^2-(\sqrt{5}/2)^2}$$

$$=3\ln|x^2-x-1|+2\frac{1}{\sqrt{5}}\ln\left|\frac{x-1/2-\sqrt{5}/2}{x-1/2+\sqrt{5}/2}\right|+C$$


**Ответ:** $3\ln|x^2-x-1|+\frac{2}{\sqrt{5}}\ln\left|\frac{2x-1-\sqrt{5}}{2x-1+\sqrt{5}}\right|+C$

---

### Интеграл 14

**Задание:**


$$\int\frac{(x+1)dx}{\sqrt{4x^2+x}}$$


**Решение:**
Производная подкоренного выражения: $8x+1$. Представим числитель: $x+1=\frac{1}{8}(8x+1)+\frac{7}{8}$.


$$\frac{1}{8}\int\frac{8x+1}{\sqrt{4x^2+x}}dx+\frac{7}{8}\int\frac{dx}{\sqrt{4(x^2+x/4)}}$$

$$=\frac{1}{4}\sqrt{4x^2+x}+\frac{7}{16}\int\frac{dx}{\sqrt{(x+1/8)^2-1/64}}$$


Применяем табличный интеграл:
**Ответ:** $\frac{1}{4}\sqrt{4x^2+x}+\frac{7}{16}\ln\left|x+\frac{1}{8}+\sqrt{x^2+\frac{x}{4}}\right|+C$

---

### Интеграл 15

**Задание:**


$$\int\frac{dx}{x\sqrt{6x-x^2}}$$


**Решение:**
Сделаем подстановку $x=\frac{1}{t}$, тогда $dx=-\frac{dt}{t^2}$.


$$\int\frac{-dt/t^2}{(1/t)\sqrt{6/t-1/t^2}}=-\int\frac{dt}{\sqrt{6t-1}}$$

$$=-\frac{1}{6}\cdot2\sqrt{6t-1}+C=-\frac{1}{3}\sqrt{6t-1}+C$$


Возвращаемся к $x$:


$$-\frac{1}{3}\sqrt{\frac{6}{x}-1}+C$$


**Ответ:** $-\frac{\sqrt{6x-x^2}}{3x}+C$

---

### Интеграл 16

**Задание:**


$$\int\frac{(7x^2+9)dx}{(x+6)(x^2-11x+30)}$$


**Решение:**
Корни квадратного трехчлена: $x=5$ и $x=6$. Знаменатель раскладывается как $(x+6)(x-5)(x-6)$.
Разложим дробь на простейшие:


$$\frac{7x^2+9}{(x+6)(x-5)(x-6)}=\frac{A}{x+6}+\frac{B}{x-5}+\frac{C}{x-6}$$


Методом подстановки корней находим коэффициенты:
При $x=-6$: $A=\frac{7(36)+9}{(-11)(-12)}=\frac{261}{132}=\frac{87}{44}$
При $x=5$: $B=\frac{7(25)+9}{(11)(-1)}=-\frac{184}{11}$
При $x=6$: $C=\frac{7(36)+9}{(12)(1)}=\frac{261}{12}=\frac{87}{4}$
Интегрируем сумму:
**Ответ:** $\frac{87}{44}\ln|x+6|-\frac{184}{11}\ln|x-5|+\frac{87}{4}\ln|x-6|+C$

---

### Интеграл 17

**Задание:**


$$\int\frac{dx}{x^2(x+3)^2}$$


**Решение:**
Разложим на простейшие дроби:


$$\frac{1}{x^2(x+3)^2}=\frac{A}{x}+\frac{B}{x^2}+\frac{C}{x+3}+\frac{D}{(x+3)^2}$$


$1=Ax(x+3)^2+B(x+3)^2+Cx^2(x+3)+Dx^2$
Подставим $x=0 \Rightarrow B=1/9$. Подставим $x=-3 \Rightarrow D=1/9$.
Сравнивая коэффициенты при $x^3$, получаем $A+C=0$. При $x$: $9A+6B=0 \Rightarrow 9A=-6/9 \Rightarrow A=-2/27$, $C=2/27$.
Интегрируем:
**Ответ:** $-\frac{2}{27}\ln|x|-\frac{1}{9x}+\frac{2}{27}\ln|x+3|-\frac{1}{9(x+3)}+C$

---

### Интеграл 18

**Задание:**


$$\int\frac{xdx}{x^3+2x^2+3x+6}$$


**Решение:**
Группируем знаменатель: $x^2(x+2)+3(x+2)=(x+2)(x^2+3)$.


$$\frac{x}{(x+2)(x^2+3)}=\frac{A}{x+2}+\frac{Bx+C}{x^2+3}$$


$x=A(x^2+3)+(Bx+C)(x+2)$.
При $x=-2 \Rightarrow A=-2/7$.
При $x=0 \Rightarrow 0=3(-2/7)+2C \Rightarrow C=3/7$.
Сравнивая коэффициенты при $x^2$: $A+B=0 \Rightarrow B=2/7$.
Интегрируем:


$$\int\left(-\frac{2/7}{x+2}+\frac{1}{7}\frac{2x+3}{x^2+3}\right)dx=-\frac{2}{7}\ln|x+2|+\frac{1}{7}\int\frac{2x}{x^2+3}dx+\frac{3}{7}\int\frac{dx}{x^2+3}$$


**Ответ:** $-\frac{2}{7}\ln|x+2|+\frac{1}{7}\ln(x^2+3)+\frac{3}{7\sqrt{3}}\operatorname{arctg}\left(\frac{x}{\sqrt{3}}\right)+C$

---

### Интеграл 19

**Задание:**


$$\int\cos^5(8x)dx$$


**Решение:**
Отделим один косинус и выразим остальное через синус:


$$\int(1-\sin^2(8x))^2\cos(8x)dx$$


Замена $u=\sin(8x)$, $du=8\cos(8x)dx \Rightarrow \cos(8x)dx=\frac{du}{8}$:


$$\frac{1}{8}\int(1-2u^2+u^4)du=\frac{1}{8}\left(u-\frac{2u^3}{3}+\frac{u^5}{5}\right)+C$$


**Ответ:** $\frac{\sin(8x)}{8}-\frac{\sin^3(8x)}{12}+\frac{\sin^5(8x)}{40}+C$

---

### Интеграл 20

**Задание:**


$$\int\sin^2(7x)\cos^6(7x)dx$$


**Решение:**
Пусть $t=7x$, $dt=7dx$. Интеграл равен $\frac{1}{7}\int\sin^2(t)\cos^6(t)dt$.
Используем формулы понижения степени:


$$\sin^2t\cos^6t=(\sin t\cos t)^2\cos^4t=\frac{\sin^2(2t)}{4}\left(\frac{1+\cos(2t)}{2}\right)^2$$

$$=\frac{1}{16}\sin^2(2t)(1+2\cos(2t)+\cos^2(2t))$$


Интегрируем по частям каждое слагаемое, еще раз применяя формулы понижения степени для квадратов. После приведения подобных:


$$\frac{1}{16}\left(\frac{t}{2}-\frac{\sin(4t)}{8}+\frac{\sin^3(2t)}{3}+\frac{t}{8}-\frac{\sin(8t)}{64}\right)=\frac{5t}{128}-\frac{\sin(4t)}{128}+\frac{\sin^3(2t)}{48}-\frac{\sin(8t)}{1024}$$


Добавляем множитель $\frac{1}{7}$ и возвращаемся к $x$:
**Ответ:** $\frac{5x}{128}-\frac{\sin(28x)}{896}+\frac{\sin^3(14x)}{336}-\frac{\sin(56x)}{7168}+C$

---

### Интеграл 21

**Задание:**


$$\int\operatorname{tg}^6(3x)dx$$


**Решение:**
Замена $t=3x$, $dt=3dx$.


$$\int\operatorname{tg}^6t dt=\int\operatorname{tg}^4t(\sec^2t-1)dt=\frac{\operatorname{tg}^5t}{5}-\int\operatorname{tg}^4tdt$$


Снижаем степень дальше:


$$\int\operatorname{tg}^4tdt=\frac{\operatorname{tg}^3t}{3}-\int\operatorname{tg}^2tdt=\frac{\operatorname{tg}^3t}{3}-(\operatorname{tg}t-t)$$


Собираем всё вместе, не забывая множитель $1/3$:
**Ответ:** $\frac{1}{15}\operatorname{tg}^5(3x)-\frac{1}{9}\operatorname{tg}^3(3x)+\frac{1}{3}\operatorname{tg}(3x)-x+C$

---

### Интеграл 22

**Задание:**


$$\int\frac{\cos^{1/13}x}{\sin^{27/13}x}dx$$


**Решение:**
Перепишем интеграл:


$$\int\frac{\cos^{1/13}x}{\sin^{1/13}x\cdot\sin^2x}dx=\int\operatorname{ctg}^{1/13}(x)\csc^2(x)dx$$


Замена $u=\operatorname{ctg}x$, $du=-\csc^2xdx$.


$$\int u^{1/13}(-du)=-\frac{u^{14/13}}{14/13}+C=-\frac{13}{14}u^{14/13}+C$$


**Ответ:** $-\frac{13}{14}\operatorname{ctg}^{14/13}(x)+C$

---

### Интеграл 23

**Задание:**


$$\int\frac{dx}{\sin x\cos^3x}$$


**Решение:**
Разделим числитель и знаменатель на $\cos^4x$:


$$\int\frac{\sec^4x}{\operatorname{tg}x}dx=\int\frac{1+\operatorname{tg}^2x}{\operatorname{tg}x}\sec^2xdx$$


Замена $u=\operatorname{tg}x$, $du=\sec^2xdx$.


$$\int\frac{1+u^2}{u}du=\int\left(\frac{1}{u}+u\right)du=\ln|u|+\frac{u^2}{2}+C$$


**Ответ:** $\ln|\operatorname{tg}x|+\frac{1}{2}\operatorname{tg}^2x+C$

---

### Интеграл 24

**Задание:**


$$\int\frac{dx}{7\sin^2(10x)-\cos(20x)}$$


**Решение:**
Выразим $\cos(20x)$ через синус: $\cos(20x)=1-2\sin^2(10x)$.
Знаменатель: $7\sin^2(10x)-1+2\sin^2(10x)=9\sin^2(10x)-1$.
Альтернативно можно выразить через $\cos^2$ и $\sin^2$: знаменатель равен $8\sin^2(10x)-\cos^2(10x)$. Разделим числитель и знаменатель на $\cos^2(10x)$:


$$\int\frac{\sec^2(10x)}{8\operatorname{tg}^2(10x)-1}dx$$


Замена $u=\operatorname{tg}(10x)$, $du=10\sec^2(10x)dx$.


$$\frac{1}{10}\int\frac{du}{8u^2-1}=\frac{1}{80}\int\frac{du}{u^2-1/8}=\frac{1}{80}\frac{1}{2(1/\sqrt{8})}\ln\left|\frac{u-1/\sqrt{8}}{u+1/\sqrt{8}}\right|$$


**Ответ:** $\frac{\sqrt{2}}{80}\ln\left|\frac{2\sqrt{2}\operatorname{tg}(10x)-1}{2\sqrt{2}\operatorname{tg}(10x)+1}\right|+C$

---

### Интеграл 25

**Задание:**


$$\int\frac{\sin xdx}{\sin x+4}$$


**Решение:**
Выделим целую часть:


$$\int\left(1-\frac{4}{\sin x+4}\right)dx=x-4\int\frac{dx}{\sin x+4}$$


Используем универсальную тригонометрическую подстановку $t=\operatorname{tg}(x/2)$, $dx=\frac{2dt}{1+t^2}$, $\sin x=\frac{2t}{1+t^2}$.


$$4\int\frac{\frac{2dt}{1+t^2}}{\frac{2t}{1+t^2}+4}=8\int\frac{dt}{4t^2+2t+4}=2\int\frac{dt}{t^2+t/2+1}$$


Выделяем полный квадрат: $t^2+t/2+1=(t+1/4)^2+15/16$.


$$2\int\frac{dt}{(t+1/4)^2+(\sqrt{15}/4)^2}=\frac{8}{\sqrt{15}}\operatorname{arctg}\left(\frac{4t+1}{\sqrt{15}}\right)$$


**Ответ:** $x-\frac{8}{\sqrt{15}}\operatorname{arctg}\left(\frac{4\operatorname{tg}(x/2)+1}{\sqrt{15}}\right)+C$

---

### Интеграл 26

**Задание:**


$$\int\cos^2(2x)\sin(3x)dx$$


**Решение:**
Понижаем степень: $\cos^2(2x)=\frac{1+\cos(4x)}{2}$.


$$\frac{1}{2}\int\sin(3x)dx+\frac{1}{2}\int\cos(4x)\sin(3x)dx$$


Применяем формулу произведения: $\cos(4x)\sin(3x)=\frac{1}{2}(\sin(7x)-\sin(x))$.


$$\int=-\frac{\cos(3x)}{6}+\frac{1}{4}\int(\sin(7x)-\sin(x))dx$$


**Ответ:** $-\frac{1}{6}\cos(3x)-\frac{1}{28}\cos(7x)+\frac{1}{4}\cos x+C$

---

### Интеграл 27

**Задание:**


$$\int\frac{dx}{x^2\sqrt{x^2-40}}$$


**Решение:**
Сделаем замену $x=\frac{1}{u}$, $dx=-\frac{du}{u^2}$.


$$\int\frac{-du/u^2}{(1/u^2)\sqrt{1/u^2-40}}=-\int\frac{udu}{\sqrt{1-40u^2}}$$


Замена $w=1-40u^2$, $dw=-80udu \Rightarrow udu=-\frac{dw}{80}$.


$$-\int\left(-\frac{1}{80}\right)\frac{dw}{\sqrt{w}}=\frac{1}{40}\sqrt{w}+C=\frac{\sqrt{1-40u^2}}{40}+C$$


Возвращаемся к $x$:
**Ответ:** $\frac{\sqrt{x^2-40}}{40x}+C$

---

### Интеграл 28

**Задание:**


$$\int\frac{x^2dx}{\sqrt{(x^2+4)^5}}$$


**Решение:**
Тригонометрическая подстановка $x=2\operatorname{tg}t$, $dx=\frac{2}{\cos^2t}dt$. $\sqrt{x^2+4}=\frac{2}{\cos t}$.


$$\int\frac{4\operatorname{tg}^2t\cdot2/\cos^2t}{(2/\cos t)^5}dt=\frac{8}{32}\int\frac{\sin^2t}{\cos^4t}\cos^5t dt=\frac{1}{4}\int\sin^2t\cos t dt$$


Замена $u=\sin t$, $du=\cos t dt$.


$$\frac{1}{4}\int u^2du=\frac{u^3}{12}+C=\frac{\sin^3t}{12}+C$$


Учитывая, что $\operatorname{tg}t=\frac{x}{2}$, находим $\sin t=\frac{x}{\sqrt{x^2+4}}$.
**Ответ:** $\frac{x^3}{12(x^2+4)^{3/2}}+C$

---

### Интеграл 29

**Задание:**


$$\int\frac{x^2dx}{\sqrt{(19-x^2)^3}}$$


**Решение:**
Подстановка $x=\sqrt{19}\sin t$, $dx=\sqrt{19}\cos t dt$. $\sqrt{19-x^2}=\sqrt{19}\cos t$.


$$\int\frac{19\sin^2t\sqrt{19}\cos t}{19\sqrt{19}\cos^3t}dt=\int\frac{\sin^2t}{\cos^2t}dt=\int\operatorname{tg}^2t dt=\int(\sec^2t-1)dt=\operatorname{tg}t-t+C$$


Возвращаемся к $x$, где $\sin t=\frac{x}{\sqrt{19}}$ и $\operatorname{tg}t=\frac{x}{\sqrt{19-x^2}}$:
**Ответ:** $\frac{x}{\sqrt{19-x^2}}-\arcsin\left(\frac{x}{\sqrt{19}}\right)+C$