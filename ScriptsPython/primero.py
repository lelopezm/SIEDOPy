# The code is importing two libraries: PySimpleGUI and matplotlib.pyplot.
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import math as Math


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

def lessgrafic(x, er):
    les = []
    for i in range(len(x)):
        les.append(x[i] - er[i]) #DEBE GRAFICAR SOLO er

    return les

def Log_Er(er):
    log = [0]
    for i in range(1,len(er)):
        val = Math.log10(er[i])
        log.append(val)
    #print(log)
    #print(er)
        
    return log
    

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
    er = [0]
    for i in range(N):
        x.append(x[-1] + h * x_prime(x[-1], a))
        t.append(t[-1] + h)
        er.append(abs(x[-1] - x_prime(x0, Math.exp(a * t[-1]))))

    return t, x, er


# Define the layout of the GUI
# The `layout` variable is defining the structure and components of the graphical user
# interface (GUI) window. It is a list of lists, where each inner list represents a row in
# the GUI window.
layout = [
    [sg.Text("Valor de a (Tasa de Crecimiento) :"), sg.Input(key="-A-")],
    [sg.Text("Valor de x0 (Valor Inicial) :"), sg.Input(key="-X0-")],
    [sg.Text("Valor de Tf (Tiempo Final) :"), sg.Input(key="-TF-")],
    [sg.Text("Valor de N (Numero de divisiones) :"),
     sg.Input(key="-N-")],
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
        t, x, er = euler(x0, a, Tf, N)
        les = lessgrafic(x, er)  
        log_er = Log_Er(er)
        
        graf_Euler, graf_Error = plt.subplot(1, 2, 1), plt.subplot(1, 2, 2)
        #set propiedades de la primera grafica
        graf_Euler.set_title("Crecimiento exponencial")
        graf_Euler.set_xlabel("t")
        graf_Euler.set_ylabel("x")
        graf_Euler.plot(t, x, label="Euler")
        graf_Euler.plot(t, les, label="Solucion exacta")
        graf_Euler.legend()
        graf_Euler.grid()
        
        #set propiedades de la segunda grafica
        graf_Error.plot(t, log_er, label="Error")
        graf_Error.set_title("Error")
        graf_Error.set_xlabel("t")
        graf_Error.set_ylabel("Log(E)")
        graf_Error.legend()
        graf_Error.grid()
        plt.show()

# Close the window
window.close()