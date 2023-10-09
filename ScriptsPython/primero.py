# The code is importing two libraries: PySimpleGUI and matplotlib.pyplot.
import PySimpleGUI as sg
import matplotlib.pyplot as plt

def x_prime(x, a):
    """
    The function `x_prime` takes two parameters `x` and `a` and returns the product of `x` and
    `a`.
    
    :param x: The parameter x is a number that will be multiplied by the value of a
    :param a: The parameter "a" is a constant value that will be multiplied by the input value
    "x"
    :return: the product of `a` and `x`.
    """
    return a * x

def euler(x0, a, Tf, N):
    """
    The function `euler` implements the Euler method to approximate the solution of a
    first-order ordinary differential equation.
    
    :param x0: The initial value of x at t=0
    :param a: The parameter "a" is not defined in the given code. It seems to be a missing
    piece of information. Could you please provide more details about what "a" represents in
    this context?
    :param Tf: Tf is the final time at which we want to evaluate the solution
    :param N: N is the number of steps in the Euler method. It determines the granularity of
    the approximation
    :return: two lists: t and x. The list t contains the time values at each step, and the
    list x contains the corresponding values of x at each step.
    """
    h = (Tf - 0) / N
    t = [0]
    x = [x0]
    for i in range(N):
        x.append(x[-1] + h * x_prime(x[-1], a))
        t.append(t[-1] + h)
    return t, x

# Define the layout of the GUI
# The `layout` variable is defining the structure and components of the graphical user
# interface (GUI) window. It is a list of lists, where each inner list represents a row in
# the GUI window.
layout = [
    [sg.Text("Valor de a (Tasa de Crecimiento) :"), sg.Input(key="-A-")],
    [sg.Text("Valor de x0 (Valor Inicial) :"), sg.Input(key="-X0-")],
    [sg.Text("Valor de Tf (Tiempo Final) :"), sg.Input(key="-TF-")],
    [sg.Text("Valor de N (Numero de intervalos de tiempo) :"), sg.Input(key="-N-")],
    [sg.Button("Graficar"), sg.Button("Salir")]
]

# Create the window
window = sg.Window("Crecimiento exponencial", layout)

# Event loop
# The code block you provided is the event loop of the graphical user interface (GUI)
# window. It continuously listens for events and performs actions based on the event that
# occurs.
while True:
    event, values = window.read()
    if event == "Salir" or event == sg.WIN_CLOSED:
        break
    elif event == "Graficar":
        a = float(values["-A-"])
        x0 = float(values["-X0-"])
        Tf = float(values["-TF-"])
        N = int(values["-N-"])
        t, x = euler(x0, a, Tf, N)
        plt.plot(t, x)
        plt.xlabel("t")
        plt.ylabel("x")
        plt.title("Crecimiento exponencial")
        plt.show()

# Close the window
window.close()