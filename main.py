from methods.euler import Euler
import matplotlib.pyplot as plt

def main():
    ''' Application initializer. '''
    modelo: Euler = Euler()
    modelo.solve()

    print(
        f'Euler Method X: {modelo.X[-1]}'
    )

    plt.plot(modelo.T, modelo.X, color='blue', linewidth=2, linestyle='-', marker='o', markersize=5, markerfacecolor='red', markeredgewidth=1, markeredgecolor='black')
    plt.title('ODE Solution')
    plt.xlabel('Time (s)')
    plt.ylabel('Value of X')
    plt.grid(True)

    plt.show()

if __name__ == '__main__':
    main()