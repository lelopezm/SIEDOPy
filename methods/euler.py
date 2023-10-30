# Purpose: Funciones para resolver ecuaciones diferenciales ordinarias
# En el metodo de euler se ingresa t inicial, t final, x inicial, a y N

class Euler():
    """ Clase Euler para resolver ecuaciones diferenciales ordinarias """

    def __init__(
            self,
            t: float = 10,
            t0: float = 0,
            x0: float = 2,
            a: float = 0.35,
            N: int = 100
    ):
        """ Constructor de la clase Euler
        :param t: tiempo final
        :param t0: tiempo inicial
        :param x0: valor inicial de x
        :param a: constante a
        :param N: numero de subintervalos
        """
        self.t: float = t
        self.t0: float = t0
        self.x0: float = x0
        self.a: float = a
        self.N: int = N

        self.T: list[float] = []
        self.X: list[float] = []

    def get_h(self) -> float:
        """
        Calcula el tamaño de paso
        :return: tamaño de paso
        """
        return (self.t - self.t0) / self.N

    def set_t(self) -> None:
        """
        Calcula los tiempos de la solucion
        :return: None
        """
        self.T = [self.t0 + i * self.get_h() for i in range(self.N + 1)]
        return

    def set_x(self) -> None:
        """
        Calcula la solucion numerica
        :return: None
        """
        self.X = [self.x0]
        for i in range(self.N):
            self.X.append(
                self.X[i] + (self.get_h() * self.f(self.X[i]))
            )
        return

    def f(self, x: float) -> float:
        """
        Funcion f(x) = a * x
        :param t: tiempo
        :param x: valor de x
        :return: valor de f(t, x)
        """
        return self.a * x

    def solve(self) -> None:
        """
        Calcula la solucion numerica
        :return: None
        """
        self.set_t()
        self.set_x()
        return

    def get_solution(self) -> tuple[list[float], list[float]]:
        """
        Devuelve los tiempos y la solucion
        :return: (tiempos, solucion)
        """
        return self.T, self.X