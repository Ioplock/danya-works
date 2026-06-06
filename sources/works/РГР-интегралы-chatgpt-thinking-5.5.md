# Решение интегралов. Вариант 21

Во всех заданиях \(C\) — произвольная постоянная интегрирования.

---

## 1

\[
I_1=\int \frac{dx}{x\ln^{41}x}
\]

Сделаем замену:

\[
u=\ln x, \qquad du=\frac{dx}{x}.
\]

Тогда

\[
I_1=\int u^{-41}\,du=\frac{u^{-40}}{-40}+C.
\]

Возвращаемся к переменной \(x\):

\[
\boxed{I_1=-\frac{1}{40\ln^{40}x}+C}
\]

---

## 2

\[
I_2=\int \sqrt{\frac{8-\arcsin x}{1-x^2}}\,dx
\]

Запишем подынтегральное выражение так:

\[
I_2=\int \sqrt{8-\arcsin x}\,\frac{dx}{\sqrt{1-x^2}}.
\]

Сделаем замену:

\[
u=8-\arcsin x, \qquad du=-\frac{dx}{\sqrt{1-x^2}}.
\]

Тогда

\[
I_2=-\int u^{1/2}\,du=-\frac{2}{3}u^{3/2}+C.
\]

Ответ:

\[
\boxed{I_2=-\frac{2}{3}(8-\arcsin x)^{3/2}+C}
\]

---

## 3

\[
I_3=\int \frac{x^8\,dx}{\cos^2(14x^9-2)}
\]

Используем то, что

\[
\frac{1}{\cos^2 u}=\sec^2 u.
\]

Сделаем замену:

\[
u=14x^9-2, \qquad du=126x^8\,dx.
\]

Значит,

\[
x^8\,dx=\frac{du}{126}.
\]

Тогда

\[
I_3=\frac{1}{126}\int \sec^2 u\,du=\frac{1}{126}\tg u+C.
\]

Ответ:

\[
\boxed{I_3=\frac{1}{126}\tg(14x^9-2)+C}
\]

---

## 4

\[
I_4=\int 20^x\sin(7\cdot 20^x)\,dx
\]

Сделаем замену:

\[
u=7\cdot 20^x.
\]

Тогда

\[
du=7\ln 20\cdot 20^x\,dx,
\qquad
20^x\,dx=\frac{du}{7\ln 20}.
\]

Получаем:

\[
I_4=\frac{1}{7\ln 20}\int \sin u\,du
=-\frac{\cos u}{7\ln 20}+C.
\]

Ответ:

\[
\boxed{I_4=-\frac{\cos(7\cdot 20^x)}{7\ln 20}+C}
\]

---

## 5

\[
I_5=\int \frac{(6-x)\,dx}{x\sqrt{x-2}}
\]

Сделаем замену:

\[
t=\sqrt{x-2}, \qquad x=t^2+2, \qquad dx=2t\,dt.
\]

Тогда

\[
6-x=6-(t^2+2)=4-t^2.
\]

Подставляем:

\[
I_5=\int \frac{4-t^2}{(t^2+2)t}\cdot 2t\,dt
=\int \frac{2(4-t^2)}{t^2+2}\,dt.
\]

Преобразуем дробь:

\[
4-t^2=6-(t^2+2),
\]

поэтому

\[
\frac{2(4-t^2)}{t^2+2}
=\frac{12}{t^2+2}-2.
\]

Тогда

\[
I_5=\int \left(\frac{12}{t^2+2}-2\right)dt
=12\int \frac{dt}{t^2+2}-2t+C.
\]

Так как

\[
\int \frac{dt}{t^2+a^2}=\frac{1}{a}\arctg\frac{t}{a},
\qquad a=\sqrt2,
\]

получаем:

\[
I_5=\frac{12}{\sqrt2}\arctg\frac{t}{\sqrt2}-2t+C
=6\sqrt2\arctg\frac{t}{\sqrt2}-2t+C.
\]

Возвращаемся к \(x\):

\[
\boxed{I_5=6\sqrt2\arctg\frac{\sqrt{x-2}}{\sqrt2}-2\sqrt{x-2}+C}
\]

---

## 6

\[
I_6=\int \frac{\sqrt{x+6}\,dx}{4x+1}
\]

Сделаем замену:

\[
t=\sqrt{x+6}, \qquad x=t^2-6, \qquad dx=2t\,dt.
\]

Тогда

\[
4x+1=4(t^2-6)+1=4t^2-23.
\]

Подставим:

\[
I_6=\int \frac{t\cdot 2t\,dt}{4t^2-23}
=\int \frac{2t^2}{4t^2-23}\,dt.
\]

Разделим дробь:

\[
\frac{2t^2}{4t^2-23}=\frac12+\frac{23}{2(4t^2-23)}.
\]

Тогда

\[
I_6=\frac{t}{2}+\frac{23}{2}\int \frac{dt}{4t^2-23}.
\]

Преобразуем знаменатель:

\[
4t^2-23=4\left(t^2-\frac{23}{4}\right).
\]

Используем формулу

\[
\int \frac{dt}{t^2-a^2}=\frac{1}{2a}\ln\left|\frac{t-a}{t+a}\right|.
\]

Здесь

\[
a=\frac{\sqrt{23}}{2}.
\]

Поэтому

\[
\int \frac{dt}{4t^2-23}
=\frac{1}{4\sqrt{23}}\ln\left|\frac{2t-\sqrt{23}}{2t+\sqrt{23}}\right|.
\]

Итак,

\[
I_6=\frac{t}{2}+\frac{\sqrt{23}}{8}
\ln\left|\frac{2t-\sqrt{23}}{2t+\sqrt{23}}\right|+C.
\]

Ответ:

\[
\boxed{I_6=\frac{\sqrt{x+6}}{2}+\frac{\sqrt{23}}{8}
\ln\left|\frac{2\sqrt{x+6}-\sqrt{23}}{2\sqrt{x+6}+\sqrt{23}}\right|+C}
\]

---

## 7

\[
I_7=\int \frac{dx}{(1-9x)\sqrt{x}}
\]

Сделаем замену:

\[
t=\sqrt{x}, \qquad x=t^2, \qquad dx=2t\,dt.
\]

Тогда

\[
I_7=\int \frac{2t\,dt}{(1-9t^2)t}
=2\int \frac{dt}{1-9t^2}.
\]

Запишем знаменатель:

\[
1-9t^2=1-(3t)^2.
\]

Используем формулу

\[
\int \frac{dz}{1-z^2}=\frac12\ln\left|\frac{1+z}{1-z}\right|.
\]

При \(z=3t\), \(dz=3dt\), поэтому

\[
I_7=\frac{2}{3}\int \frac{dz}{1-z^2}
=\frac13\ln\left|\frac{1+z}{1-z}\right|+C.
\]

Ответ:

\[
\boxed{I_7=\frac13\ln\left|\frac{1+3\sqrt{x}}{1-3\sqrt{x}}\right|+C}
\]

---

## 8

\[
I_8=\int \frac{4\cdot 19^x+1}{5\cdot 19^x+1}\,dx
\]

Сделаем замену:

\[
t=19^x, \qquad dt=19^x\ln 19\,dx=t\ln 19\,dx.
\]

Отсюда

\[
dx=\frac{dt}{t\ln 19}.
\]

Тогда

\[
I_8=\frac{1}{\ln 19}\int \frac{4t+1}{t(5t+1)}\,dt.
\]

Разложим на простые дроби:

\[
\frac{4t+1}{t(5t+1)}=\frac{A}{t}+\frac{B}{5t+1}.
\]

Тогда

\[
4t+1=A(5t+1)+Bt=(5A+B)t+A.
\]

Получаем систему:

\[
A=1, \qquad 5A+B=4.
\]

Отсюда

\[
B=-1.
\]

Значит,

\[
I_8=\frac{1}{\ln 19}\int \left(\frac1t-\frac{1}{5t+1}\right)dt.
\]

Интегрируем:

\[
I_8=\frac{1}{\ln 19}\left(\ln|t|-\frac15\ln|5t+1|\right)+C.
\]

Так как \(t=19^x\), то \(\ln t=x\ln 19\). Поэтому

\[
\boxed{I_8=x-\frac{1}{5\ln 19}\ln(5\cdot 19^x+1)+C}
\]

---

## 9

\[
I_9=\int e^{-\sqrt{6-x}}\,dx
\]

Сделаем замену:

\[
t=\sqrt{6-x}, \qquad t^2=6-x, \qquad x=6-t^2.
\]

Тогда

\[
dx=-2t\,dt.
\]

Подставляем:

\[
I_9=-2\int t e^{-t}\,dt.
\]

Найдем интеграл по частям:

\[
\int t e^{-t}\,dt=-(t+1)e^{-t}+C.
\]

Значит,

\[
I_9=2(t+1)e^{-t}+C.
\]

Возвращаемся к \(x\):

\[
\boxed{I_9=2(\sqrt{6-x}+1)e^{-\sqrt{6-x}}+C}
\]

---

## 10

\[
I_{10}=\int x^2\arctg(6x)\,dx
\]

Используем интегрирование по частям:

\[
\int u\,dv=uv-\int v\,du.
\]

Берем

\[
u=\arctg(6x), \qquad dv=x^2\,dx.
\]

Тогда

\[
du=\frac{6}{1+36x^2}\,dx, \qquad v=\frac{x^3}{3}.
\]

Получаем:

\[
I_{10}=\frac{x^3}{3}\arctg(6x)-\int \frac{x^3}{3}\cdot \frac{6}{1+36x^2}\,dx.
\]

То есть

\[
I_{10}=\frac{x^3}{3}\arctg(6x)-2\int \frac{x^3}{1+36x^2}\,dx.
\]

Преобразуем дробь:

\[
\frac{x^3}{1+36x^2}=\frac{x}{36}-\frac{x}{36(1+36x^2)}.
\]

Тогда

\[
\int \frac{x^3}{1+36x^2}\,dx
=\frac{x^2}{72}-\frac{1}{36}\int \frac{x\,dx}{1+36x^2}.
\]

Так как

\[
\int \frac{x\,dx}{1+36x^2}=\frac{1}{72}\ln(1+36x^2),
\]

получаем:

\[
\int \frac{x^3}{1+36x^2}\,dx
=\frac{x^2}{72}-\frac{1}{2592}\ln(1+36x^2).
\]

Значит,

\[
I_{10}=\frac{x^3}{3}\arctg(6x)-\frac{x^2}{36}+\frac{1}{1296}\ln(1+36x^2)+C.
\]

Ответ:

\[
\boxed{I_{10}=\frac{x^3}{3}\arctg(6x)-\frac{x^2}{36}+\frac{1}{1296}\ln(1+36x^2)+C}
\]

---

## 11

\[
I_{11}=\int (x-\ln x)^2\,dx
\]

Раскроем квадрат:

\[
(x-\ln x)^2=x^2-2x\ln x+\ln^2 x.
\]

Тогда

\[
I_{11}=\int x^2\,dx-2\int x\ln x\,dx+\int \ln^2x\,dx.
\]

Первый интеграл:

\[
\int x^2\,dx=\frac{x^3}{3}.
\]

Второй интеграл найдем по частям:

\[
\int x\ln x\,dx=\frac{x^2}{2}\ln x-\int \frac{x^2}{2}\cdot \frac{1}{x}\,dx
=\frac{x^2}{2}\ln x-\frac{x^2}{4}.
\]

Значит,

\[
-2\int x\ln x\,dx=-x^2\ln x+\frac{x^2}{2}.
\]

Третий интеграл:

\[
\int \ln^2x\,dx=x\ln^2x-2\int \ln x\,dx.
\]

Так как

\[
\int \ln x\,dx=x\ln x-x,
\]

получаем:

\[
\int \ln^2x\,dx=x\ln^2x-2x\ln x+2x.
\]

Итог:

\[
\boxed{I_{11}=\frac{x^3}{3}-x^2\ln x+\frac{x^2}{2}+x\ln^2x-2x\ln x+2x+C}
\]

---

## 12

\[
I_{12}=\int e^{-x}\arctg(e^x)\,dx
\]

Используем интегрирование по частям:

\[
u=\arctg(e^x), \qquad dv=e^{-x}\,dx.
\]

Тогда

\[
du=\frac{e^x}{1+e^{2x}}\,dx,
\qquad
v=-e^{-x}.
\]

Получаем:

\[
I_{12}=-e^{-x}\arctg(e^x)+\int \frac{dx}{1+e^{2x}}.
\]

Вычислим оставшийся интеграл. Пусть

\[
t=e^x, \qquad dx=\frac{dt}{t}.
\]

Тогда

\[
\int \frac{dx}{1+e^{2x}}
=\int \frac{dt}{t(1+t^2)}.
\]

Разложим:

\[
\frac{1}{t(1+t^2)}=\frac1t-\frac{t}{1+t^2}.
\]

Значит,

\[
\int \frac{dt}{t(1+t^2)}=\ln|t|-\frac12\ln(1+t^2)+C.
\]

Возвращаемся к \(x\):

\[
\ln t=x,
\qquad
\ln(1+t^2)=\ln(1+e^{2x}).
\]

Ответ:

\[
\boxed{I_{12}=-e^{-x}\arctg(e^x)+x-\frac12\ln(1+e^{2x})+C}
\]

---

## 13

\[
I_{13}=\int \frac{(6x-1)\,dx}{x^2-x-1}
\]

Обозначим знаменатель:

\[
D=x^2-x-1.
\]

Его производная:

\[
D'=2x-1.
\]

Представим числитель через производную знаменателя:

\[
6x-1=3(2x-1)+2.
\]

Тогда

\[
I_{13}=3\int \frac{2x-1}{x^2-x-1}\,dx+2\int \frac{dx}{x^2-x-1}.
\]

Первый интеграл:

\[
3\int \frac{2x-1}{x^2-x-1}\,dx=3\ln|x^2-x-1|.
\]

Для второго интеграла выделим полный квадрат:

\[
x^2-x-1=\left(x-\frac12\right)^2-\frac54.
\]

Тогда

\[
x^2-x-1=\left(x-\frac12\right)^2-\left(\frac{\sqrt5}{2}\right)^2.
\]

Используем формулу:

\[
\int \frac{dy}{y^2-a^2}=\frac{1}{2a}\ln\left|\frac{y-a}{y+a}\right|.
\]

Здесь

\[
y=x-\frac12, \qquad a=\frac{\sqrt5}{2}.
\]

Поэтому

\[
\int \frac{dx}{x^2-x-1}
=\frac{1}{\sqrt5}\ln\left|\frac{2x-1-\sqrt5}{2x-1+\sqrt5}\right|.
\]

Ответ:

\[
\boxed{I_{13}=3\ln|x^2-x-1|+\frac{2}{\sqrt5}\ln\left|\frac{2x-1-\sqrt5}{2x-1+\sqrt5}\right|+C}
\]

---

## 14

\[
I_{14}=\int \frac{(x+1)\,dx}{\sqrt{x+4x^2}}
\]

Обозначим:

\[
R=x+4x^2.
\]

Тогда

\[
R'=1+8x.
\]

Выразим числитель через производную подкоренного выражения:

\[
x+1=\frac18(8x+1)+\frac78.
\]

Тогда

\[
I_{14}=\frac18\int \frac{8x+1}{\sqrt{x+4x^2}}\,dx
+\frac78\int \frac{dx}{\sqrt{x+4x^2}}.
\]

Первый интеграл:

\[
\frac18\int \frac{R'}{\sqrt R}\,dx
=\frac18\cdot 2\sqrt R
=\frac14\sqrt{x+4x^2}.
\]

Теперь вычислим второй интеграл:

\[
J=\int \frac{dx}{\sqrt{x+4x^2}}.
\]

Заметим, что

\[
x+4x^2=\frac{(8x+1)^2-1}{16}.
\]

Положим

\[
u=8x+1, \qquad du=8dx.
\]

Тогда

\[
\sqrt{x+4x^2}=\frac14\sqrt{u^2-1},
\qquad dx=\frac{du}{8}.
\]

Следовательно,

\[
J=\frac12\int \frac{du}{\sqrt{u^2-1}}
=\frac12\ln|u+\sqrt{u^2-1}|+C.
\]

Возвращаемся к \(x\):

\[
J=\frac12\ln\left|8x+1+4\sqrt{x+4x^2}\right|+C.
\]

Значит,

\[
I_{14}=\frac14\sqrt{x+4x^2}+\frac{7}{16}\ln\left|8x+1+4\sqrt{x+4x^2}\right|+C.
\]

Ответ:

\[
\boxed{I_{14}=\frac14\sqrt{x+4x^2}+\frac{7}{16}\ln\left|8x+1+4\sqrt{x+4x^2}\right|+C}
\]

---

## 15

\[
I_{15}=\int \frac{dx}{x\sqrt{6x-x^2}}
\]

Представим подкоренное выражение:

\[
6x-x^2=x(6-x).
\]

Сделаем тригонометрическую замену:

\[
x=6\sin^2 t.
\]

Тогда

\[
dx=12\sin t\cos t\,dt,
\]

а также

\[
\sqrt{6x-x^2}=\sqrt{36\sin^2t\cos^2t}=6\sin t\cos t.
\]

Подставляем:

\[
I_{15}=\int \frac{12\sin t\cos t\,dt}{6\sin^2t\cdot 6\sin t\cos t}
=\frac13\int \csc^2t\,dt.
\]

Так как

\[
\int \csc^2t\,dt=-\ctg t,
\]

получаем:

\[
I_{15}=-\frac13\ctg t+C.
\]

Из замены

\[
\sin^2t=\frac{x}{6},
\qquad
\cos^2t=\frac{6-x}{6}.
\]

Значит,

\[
\ctg t=\sqrt{\frac{6-x}{x}}.
\]

Ответ:

\[
\boxed{I_{15}=-\frac13\sqrt{\frac{6-x}{x}}+C}
\]

---

## 16

\[
I_{16}=\int \frac{(7x^2+9)\,dx}{(x+6)(x^2-11x+30)}
\]

Разложим квадратный множитель:

\[
x^2-11x+30=(x-5)(x-6).
\]

Тогда

\[
I_{16}=\int \frac{7x^2+9}{(x+6)(x-5)(x-6)}\,dx.
\]

Разложим дробь на простые дроби:

\[
\frac{7x^2+9}{(x+6)(x-5)(x-6)}
=\frac{A}{x+6}+\frac{B}{x-5}+\frac{C}{x-6}.
\]

После приведения к общему знаменателю:

\[
7x^2+9=A(x-5)(x-6)+B(x+6)(x-6)+C(x+6)(x-5).
\]

Подстановка удобных значений дает:

\[
x=-6: \qquad 7\cdot36+9=A(-11)(-12),
\]

\[
261=132A, \qquad A=\frac{87}{44}.
\]

\[
x=5: \qquad 7\cdot25+9=B(11)(-1),
\]

\[
184=-11B, \qquad B=-\frac{184}{11}.
\]

\[
x=6: \qquad 7\cdot36+9=C(12)(1),
\]

\[
261=12C, \qquad C=\frac{87}{4}.
\]

Следовательно,

\[
I_{16}=\int \left(\frac{87}{44(x+6)}-\frac{184}{11(x-5)}+\frac{87}{4(x-6)}\right)dx.
\]

Ответ:

\[
\boxed{I_{16}=\frac{87}{44}\ln|x+6|-\frac{184}{11}\ln|x-5|+\frac{87}{4}\ln|x-6|+C}
\]

---

## 17

\[
I_{17}=\int \frac{dx}{[x(x+3)]^2}
\]

Перепишем знаменатель:

\[
[x(x+3)]^2=x^2(x+3)^2.
\]

Ищем разложение:

\[
\frac{1}{x^2(x+3)^2}=\frac{A}{x}+\frac{B}{x^2}+\frac{C}{x+3}+\frac{D}{(x+3)^2}.
\]

Для этой дроби получается:

\[
\frac{1}{x^2(x+3)^2}
=-\frac{2}{27x}+\frac{1}{9x^2}+\frac{2}{27(x+3)}+\frac{1}{9(x+3)^2}.
\]

Тогда

\[
I_{17}=\int \left(-\frac{2}{27x}+\frac{1}{9x^2}+\frac{2}{27(x+3)}+\frac{1}{9(x+3)^2}\right)dx.
\]

Интегрируем по частям суммы:

\[
I_{17}=-\frac{2}{27}\ln|x|-\frac{1}{9x}+\frac{2}{27}\ln|x+3|-\frac{1}{9(x+3)}+C.
\]

Ответ можно записать компактно:

\[
\boxed{I_{17}=\frac{2}{27}\ln\left|\frac{x+3}{x}\right|-\frac{1}{9x}-\frac{1}{9(x+3)}+C}
\]

---

## 18

\[
I_{18}=\int \frac{x\,dx}{x^3+2x^2+3x+6}
\]

Разложим знаменатель группировкой:

\[
x^3+2x^2+3x+6=x^2(x+2)+3(x+2)=(x+2)(x^2+3).
\]

Тогда

\[
I_{18}=\int \frac{x\,dx}{(x+2)(x^2+3)}.
\]

Разложим дробь:

\[
\frac{x}{(x+2)(x^2+3)}=\frac{A}{x+2}+\frac{Bx+C}{x^2+3}.
\]

Умножим на общий знаменатель:

\[
x=A(x^2+3)+(Bx+C)(x+2).
\]

После нахождения коэффициентов получаем:

\[
\frac{x}{(x+2)(x^2+3)}=-\frac{2}{7(x+2)}+\frac{2x+3}{7(x^2+3)}.
\]

Тогда

\[
I_{18}=-\frac27\int \frac{dx}{x+2}+\frac17\int \frac{2x\,dx}{x^2+3}+\frac37\int \frac{dx}{x^2+3}.
\]

Вычислим:

\[
-\frac27\int \frac{dx}{x+2}=-\frac27\ln|x+2|,
\]

\[
\frac17\int \frac{2x\,dx}{x^2+3}=\frac17\ln(x^2+3),
\]

\[
\frac37\int \frac{dx}{x^2+3}=\frac37\cdot\frac{1}{\sqrt3}\arctg\frac{x}{\sqrt3}
=\frac{\sqrt3}{7}\arctg\frac{x}{\sqrt3}.
\]

Ответ:

\[
\boxed{I_{18}=\frac17\ln(x^2+3)-\frac27\ln|x+2|+\frac{\sqrt3}{7}\arctg\frac{x}{\sqrt3}+C}
\]

---

## 19

\[
I_{19}=\int \cos^5(8x)\,dx
\]

Выделим один множитель \(\cos(8x)\):

\[
\cos^5(8x)=\cos^4(8x)\cos(8x).
\]

Используем тождество:

\[
\cos^2(8x)=1-\sin^2(8x).
\]

Тогда

\[
\cos^4(8x)=(1-\sin^2(8x))^2.
\]

Сделаем замену:

\[
u=\sin(8x), \qquad du=8\cos(8x)\,dx.
\]

Значит,

\[
\cos(8x)\,dx=\frac{du}{8}.
\]

Получаем:

\[
I_{19}=\frac18\int (1-u^2)^2\,du.
\]

Раскрываем квадрат:

\[
(1-u^2)^2=1-2u^2+u^4.
\]

Тогда

\[
I_{19}=\frac18\left(u-\frac{2u^3}{3}+\frac{u^5}{5}\right)+C.
\]

Ответ:

\[
\boxed{I_{19}=\frac18\sin(8x)-\frac{1}{12}\sin^3(8x)+\frac{1}{40}\sin^5(8x)+C}
\]

---

## 20

\[
I_{20}=\int \sin^2(7x)\cos^6(7x)\,dx
\]

Используем формулу понижения степени. Для переменной \(t=7x\):

\[
\sin^2t\cos^6t=\frac{5}{128}+\frac{1}{32}\cos 2t-\frac{1}{32}\cos 4t-\frac{1}{32}\cos 6t-\frac{1}{128}\cos 8t.
\]

Так как \(t=7x\), получаем:

\[
\sin^2(7x)\cos^6(7x)=\frac{5}{128}+\frac{1}{32}\cos(14x)-\frac{1}{32}\cos(28x)-\frac{1}{32}\cos(42x)-\frac{1}{128}\cos(56x).
\]

Интегрируем почленно:

\[
I_{20}=\frac{5x}{128}+\frac{1}{32}\cdot\frac{\sin(14x)}{14}
-\frac{1}{32}\cdot\frac{\sin(28x)}{28}
-\frac{1}{32}\cdot\frac{\sin(42x)}{42}
-\frac{1}{128}\cdot\frac{\sin(56x)}{56}+C.
\]

Ответ:

\[
\boxed{I_{20}=\frac{5x}{128}+\frac{\sin(14x)}{448}-\frac{\sin(28x)}{896}-\frac{\sin(42x)}{1344}-\frac{\sin(56x)}{7168}+C}
\]

---

## 21

\[
I_{21}=\int \tg^6(3x)\,dx
\]

Сделаем замену:

\[
t=3x, \qquad dt=3dx, \qquad dx=\frac{dt}{3}.
\]

Тогда

\[
I_{21}=\frac13\int \tg^6t\,dt.
\]

Используем тождество:

\[
\tg^2t=\sec^2t-1.
\]

Преобразуем:

\[
\int \tg^6t\,dt=\int \tg^4t(\sec^2t-1)\,dt.
\]

Тогда

\[
\int \tg^6t\,dt=\int \tg^4t\sec^2t\,dt-\int \tg^4t\,dt.
\]

Первый интеграл:

\[
\int \tg^4t\sec^2t\,dt=\frac{\tg^5t}{5}.
\]

Теперь

\[
\int \tg^4t\,dt=\int \tg^2t(\sec^2t-1)\,dt
=\frac{\tg^3t}{3}-\int \tg^2t\,dt.
\]

Но

\[
\int \tg^2t\,dt=\int(\sec^2t-1)dt=\tg t-t.
\]

Значит,

\[
\int \tg^4t\,dt=\frac{\tg^3t}{3}-\tg t+t.
\]

Следовательно,

\[
\int \tg^6t\,dt=\frac{\tg^5t}{5}-\frac{\tg^3t}{3}+\tg t-t.
\]

Возвращаемся к \(x\):

\[
I_{21}=\frac13\left(\frac{\tg^5(3x)}{5}-\frac{\tg^3(3x)}{3}+\tg(3x)-3x\right)+C.
\]

Ответ:

\[
\boxed{I_{21}=\frac{\tg^5(3x)}{15}-\frac{\tg^3(3x)}{9}+\frac{\tg(3x)}{3}-x+C}
\]

---

## 22

\[
I_{22}=\int \frac{\cos^{1/13}x\,dx}{\sin^{27/13}x}
\]

Преобразуем подынтегральное выражение:

\[
\frac{\cos^{1/13}x}{\sin^{27/13}x}
=\frac{\cos^{1/13}x}{\sin^{1/13}x}\cdot\frac{1}{\sin^2x}.
\]

То есть

\[
\frac{\cos^{1/13}x}{\sin^{27/13}x}=\ctg^{1/13}x\cdot\csc^2x.
\]

Сделаем замену:

\[
u=\ctg x, \qquad du=-\csc^2x\,dx.
\]

Тогда

\[
I_{22}=-\int u^{1/13}\,du.
\]

Интегрируем:

\[
I_{22}=-\frac{u^{14/13}}{14/13}+C=-\frac{13}{14}u^{14/13}+C.
\]

Ответ:

\[
\boxed{I_{22}=-\frac{13}{14}\ctg^{14/13}x+C}
\]

---

## 23

\[
I_{23}=\int \frac{dx}{\sin x\cos^3x}
\]

Сделаем замену:

\[
t=\tg x, \qquad dt=\sec^2x\,dx=\frac{dx}{\cos^2x}.
\]

Преобразуем интеграл:

\[
\frac{dx}{\sin x\cos^3x}
=\frac{1}{\sin x\cos x}\cdot \frac{dx}{\cos^2x}.
\]

Так как

\[
\sin x=\tg x\cos x=t\cos x,
\]

то

\[
\sin x\cos x=t\cos^2x.
\]

Через \(t=\tg x\):

\[
\frac{1}{\sin x\cos x}\,dt
=\frac{1}{t\cos^2x}\,dt.
\]

Но

\[
\frac{1}{\cos^2x}=1+\tg^2x=1+t^2.
\]

Следовательно,

\[
I_{23}=\int \frac{1+t^2}{t}\,dt
=\int \left(t+\frac1t\right)dt.
\]

Получаем:

\[
I_{23}=\frac{t^2}{2}+\ln|t|+C.
\]

Ответ:

\[
\boxed{I_{23}=\frac12\tg^2x+\ln|\tg x|+C}
\]

---

## 24

\[
I_{24}=\int \frac{dx}{7\sin^2(10x)-\cos(20x)}
\]

Используем формулу:

\[
\cos(20x)=1-2\sin^2(10x).
\]

Тогда знаменатель:

\[
7\sin^2(10x)-\cos(20x)=7\sin^2(10x)-1+2\sin^2(10x)=9\sin^2(10x)-1.
\]

Значит,

\[
I_{24}=\int \frac{dx}{9\sin^2(10x)-1}.
\]

Сделаем замену:

\[
t=\tg(10x), \qquad dt=10(1+t^2)\,dx.
\]

Отсюда

\[
dx=\frac{dt}{10(1+t^2)}.
\]

Также

\[
\sin^2(10x)=\frac{t^2}{1+t^2}.
\]

Тогда

\[
9\sin^2(10x)-1=\frac{9t^2}{1+t^2}-1
=\frac{8t^2-1}{1+t^2}.
\]

Подставляем:

\[
I_{24}=\int \frac{1+t^2}{8t^2-1}\cdot\frac{dt}{10(1+t^2)}
=\frac1{10}\int \frac{dt}{8t^2-1}.
\]

Пусть

\[
z=2\sqrt2\,t, \qquad dz=2\sqrt2\,dt.
\]

Тогда

\[
8t^2-1=z^2-1,
\qquad
dt=\frac{dz}{2\sqrt2}.
\]

Получаем:

\[
I_{24}=\frac{1}{20\sqrt2}\int \frac{dz}{z^2-1}.
\]

Используем формулу:

\[
\int \frac{dz}{z^2-1}=\frac12\ln\left|\frac{z-1}{z+1}\right|.
\]

Следовательно,

\[
I_{24}=\frac{1}{40\sqrt2}\ln\left|\frac{z-1}{z+1}\right|+C.
\]

Возвращаемся к \(x\):

\[
\boxed{I_{24}=\frac{1}{40\sqrt2}\ln\left|\frac{2\sqrt2\tg(10x)-1}{2\sqrt2\tg(10x)+1}\right|+C}
\]

---

## 25

\[
I_{25}=\int \frac{\sin x\,dx}{\sin x+4}
\]

Преобразуем дробь:

\[
\frac{\sin x}{\sin x+4}=\frac{\sin x+4-4}{\sin x+4}=1-\frac{4}{\sin x+4}.
\]

Тогда

\[
I_{25}=\int dx-4\int \frac{dx}{4+
\sin x}
=x-4J,
\]

где

\[
J=\int \frac{dx}{4+\sin x}.
\]

Для \(J\) используем универсальную тригонометрическую замену:

\[
t=\tg\frac{x}{2}.
\]

Тогда

\[
\sin x=\frac{2t}{1+t^2},
\qquad
dx=\frac{2dt}{1+t^2}.
\]

Подставим:

\[
J=\int \frac{\frac{2dt}{1+t^2}}{4+\frac{2t}{1+t^2}}
=\int \frac{2dt}{4(1+t^2)+2t}.
\]

Сократим на 2:

\[
J=\int \frac{dt}{2t^2+t+2}.
\]

Используем формулу:

\[
\int \frac{dt}{at^2+bt+c}=\frac{2}{\sqrt{4ac-b^2}}\arctg\frac{2at+b}{\sqrt{4ac-b^2}}+C.
\]

Здесь

\[
a=2, \qquad b=1, \qquad c=2.
\]

Тогда

\[
4ac-b^2=4\cdot 2\cdot 2-1=15.
\]

Значит,

\[
J=\frac{2}{\sqrt{15}}\arctg\frac{4t+1}{\sqrt{15}}+C.
\]

Возвращаемся к \(x\):

\[
J=\frac{2}{\sqrt{15}}\arctg\frac{4\tg\frac{x}{2}+1}{\sqrt{15}}+C.
\]

Следовательно,

\[
\boxed{I_{25}=x-\frac{8}{\sqrt{15}}\arctg\frac{4\tg\frac{x}{2}+1}{\sqrt{15}}+C}
\]

---

## 26

\[
I_{26}=\int \cos^2(2x)\sin(3x)\,dx
\]

Используем формулу понижения степени:

\[
\cos^2(2x)=\frac{1+\cos(4x)}{2}.
\]

Тогда

\[
I_{26}=\frac12\int \sin(3x)\,dx+\frac12\int \sin(3x)\cos(4x)\,dx.
\]

Используем формулу произведения в сумму:

\[
\sin a\cos b=\frac12[\sin(a+b)+\sin(a-b)].
\]

Получаем:

\[
\sin(3x)\cos(4x)=\frac12[\sin(7x)+\sin(-x)]
=\frac12[\sin(7x)-\sin x].
\]

Тогда

\[
I_{26}=\frac12\int \sin(3x)\,dx
+\frac14\int \sin(7x)\,dx
-\frac14\int \sin x\,dx.
\]

Интегрируем:

\[
I_{26}=-\frac{\cos(3x)}{6}-\frac{\cos(7x)}{28}+\frac{\cos x}{4}+C.
\]

Ответ:

\[
\boxed{I_{26}=-\frac{\cos(3x)}{6}-\frac{\cos(7x)}{28}+\frac{\cos x}{4}+C}
\]

---

## 27

\[
I_{27}=\int \frac{dx}{x^2\sqrt{x^2-40}}
\]

Используем стандартный результат:

\[
\frac{d}{dx}\left(\frac{\sqrt{x^2-a^2}}{x}\right)=\frac{a^2}{x^2\sqrt{x^2-a^2}}.
\]

Здесь

\[
a^2=40.
\]

Поэтому

\[
\frac{d}{dx}\left(\frac{\sqrt{x^2-40}}{40x}\right)=\frac{1}{x^2\sqrt{x^2-40}}.
\]

Ответ:

\[
\boxed{I_{27}=\frac{\sqrt{x^2-40}}{40x}+C}
\]

---

## 28

\[
I_{28}=\int \frac{x^2\,dx}{\sqrt{(x^2+4)^5}}
\]

Перепишем:

\[
\sqrt{(x^2+4)^5}=(x^2+4)^{5/2}.
\]

Тогда

\[
I_{28}=\int \frac{x^2\,dx}{(x^2+4)^{5/2}}.
\]

Сделаем тригонометрическую замену:

\[
x=2\tg t.
\]

Тогда

\[
dx=2\sec^2t\,dt,
\]

а

\[
x^2+4=4\tg^2t+4=4\sec^2t.
\]

Следовательно,

\[
(x^2+4)^{5/2}=(4\sec^2t)^{5/2}=32\sec^5t.
\]

Подставляем:

\[
I_{28}=\int \frac{4\tg^2t\cdot 2\sec^2t}{32\sec^5t}\,dt
=\frac14\int \tg^2t\cos^3t\,dt.
\]

Так как

\[
\tg^2t\cos^3t=\frac{\sin^2t}{\cos^2t}\cos^3t=\sin^2t\cos t,
\]

то

\[
I_{28}=\frac14\int \sin^2t\cos t\,dt.
\]

Сделаем замену:

\[
u=\sin t, \qquad du=\cos t\,dt.
\]

Тогда

\[
I_{28}=\frac14\int u^2\,du=\frac{u^3}{12}+C.
\]

Возвращаемся к \(x\). Из \(x=2\tg t\):

\[
\sin t=\frac{x}{\sqrt{x^2+4}}.
\]

Значит,

\[
\boxed{I_{28}=\frac{x^3}{12(x^2+4)^{3/2}}+C}
\]

---

## 29

\[
I_{29}=\int \frac{x^2\,dx}{\sqrt{(19-x^2)^3}}
\]

Перепишем знаменатель:

\[
\sqrt{(19-x^2)^3}=(19-x^2)^{3/2}.
\]

Тогда

\[
I_{29}=\int \frac{x^2\,dx}{(19-x^2)^{3/2}}.
\]

Сделаем замену:

\[
x=\sqrt{19}\sin t.
\]

Тогда

\[
dx=\sqrt{19}\cos t\,dt.
\]

Также

\[
19-x^2=19-19\sin^2t=19\cos^2t.
\]

Следовательно,

\[
(19-x^2)^{3/2}=19^{3/2}\cos^3t.
\]

Подставляем:

\[
I_{29}=\int \frac{19\sin^2t\cdot \sqrt{19}\cos t}{19^{3/2}\cos^3t}\,dt
=\int \tg^2t\,dt.
\]

Так как

\[
\tg^2t=\sec^2t-1,
\]

то

\[
I_{29}=\int(\sec^2t-1)dt=\tg t-t+C.
\]

Возвращаемся к \(x\):

\[
\sin t=\frac{x}{\sqrt{19}},
\qquad
\tg t=\frac{x}{\sqrt{19-x^2}}.
\]

Значит,

\[
t=\arcsin\frac{x}{\sqrt{19}}.
\]

Ответ:

\[
\boxed{I_{29}=\frac{x}{\sqrt{19-x^2}}-\arcsin\frac{x}{\sqrt{19}}+C}
\]
