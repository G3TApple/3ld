import matplotlib.pyplot as plt
# import mplcursors
import numpy as np

def function(x, a, b):
    return ((x ** 2 - a) ** 2) / b - 1

def bisection(a, b, epsilon):
    l = 0
    r = 10
    L = r - l
    function_calls = 1
    step = 0

    xm = (l + r) / 2
    fm = function(xm, a, b)

    tries_x = []
    tries_y = []

    while L >= epsilon:
        x1 = l + L / 4
        x2 = r - L / 4

        function_calls += 2

        f_x1 = function(x1, a, b)
        f_x2 = function(x2, a, b)

        tries_x.extend([x1, xm, x2])
        tries_y.extend([f_x1, fm, f_x2]) 

        if f_x1 < fm:
            r = xm
            xm = x1
            fm = f_x1
        elif f_x2 < fm:
            l = xm
            xm = x2
            fm = f_x2
        else:
            l = x1
            r = x2

        L = r - l
        step += 1

    return xm, step, tries_x, tries_y, function_calls

card_number = 1214162

a = int(str(card_number)[-2])
b = int(str(card_number)[-1])

if b == 0:
    b = sum(int(digit) for digit in str(card_number))
    while b >= 10:
        b = sum(int(digit) for digit in str(b))

epsilon = 0.0001

solution, steps, tries_x, tries_y, function_calls = bisection(a, b, epsilon)
print("Sprendinys:", solution)
print("F-jos minimumo įvertis:", function(solution, a, b))
print("Žingsnių skaičius:", steps)
print("Skaičiavimų skaičius:", function_calls)

x = np.linspace(0, 10) 
y = function(x, a, b)
plt.plot(x, y, label='f(x)')
plt.scatter(tries_x, tries_y, color='c', label='Bandymo taškai', alpha=0.5, edgecolors='red')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Intervalo Dalijimo Pusiau Metodas')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(solution, color='red', linestyle='--', linewidth=1, label='Sprendinys')
plt.legend()
plt.grid(True)
# mplcursors.cursor(hover=True)
plt.show()