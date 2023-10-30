class Runge_kutta():
    """ Clase Runge-kutta para resolver ecuaciones diferenciales ordinarias """

    def __init__(
            self,
            t: float = 10,
            t0: float = 0,
            x0: float = 2,
            a: float = 0.35,
            N: int = 100
    ):
        """ Constructor de la clase Runge-kutta
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
            k1 = self.f(self.X[i])
            k2 = self.f(self.X[i] + (self.get_h() / 2) * k1)
            k3 = self.f(self.X[i] + (self.get_h() / 2) * k2)
            k4 = self.f(self.X[i] + self.get_h() * k3)
