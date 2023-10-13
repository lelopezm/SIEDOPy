import os
from django.db import models
import matplotlib.pyplot as plt
import server.settings as settings
from sympy import symbols, sqrt, simplify
# import pandas as pd


class Euler_NM(models.Model):
    ''' Class Euler_nm is used to approximate. '''
    nombre: str = models.CharField(max_length=63, blank=False, null=False)
    func: str = models.CharField(
        max_length=255, blank=False, null=False, default='x'
    )
    x0: float = models.FloatField(default=0.0)  # Known
    y0: float = models.FloatField(default=0.0)  # Known
    N: float = models.FloatField(default=0.0)   # given
    h: float = models.FloatField(default=0.0)   # given

    x: str = models.FloatField(default=0.0)  # given
    resultado: float = models.FloatField(default=0.0)
    # a: float = models.FloatField(default=1.0)   # given

    x_n_val: list[int] = []
    # dataf: pd.Dataframe = pd.DataFrame()

    def __str__(self):
        return self.nombre

    def doblar(self):
        self.resultado *= 2
        self.save()
        return self.resultado

    def generate_graph(self):
        # Generar la gráfica usando matplotlib
        data: int = self.algoritmo()

        n: int = data['n']
        y: int = data['y']

        plt.plot(n, y)
        plt.xlabel('Time')
        plt.ylabel('Result')
        plt.title('Result vs. Time')

        # Guardar la gráfica en el directorio media/
        filename = f'euler_nm_plot_id{self.id}.png'
        image_path = os.path.join(settings.MEDIA_ROOT, filename)
        plt.savefig(image_path)
        plt.close()

        # Guardar la URL de la imagen en el modelo
        self.image_url = os.path.join(settings.MEDIA_URL, filename)
        self.save()

    def delta_x(self):
        valor_delta_x = (self.x - self.x0) / self.N
        if self.h != 0:
            valor_delta_x = self.h
        return valor_delta_x

    def x_n(self):
        self.x_n_val = [
            self.x0 + (i * self.delta_x()) for i in range(0, int(self.N)+1)
        ]

    def evaluar_f(self, x_i, y_i):
        # Definir las variables de la ecuación (x y y, por ejemplo)
        # Usar un selector con botones? O fijo, siempre x, t o y, x.
        y, x = symbols('y x')

        # Reemplazar las variables en la ecuación
        f_evaluada = self.func.replace(
            'x', str(x_i)
        ).replace(
            'y', str(y_i)
        )

        # Evaluar la ecuación
        resultado = simplify(f_evaluada)

        return resultado

    def algoritmo(self):
        self.x_n()

        data: dict = {
            'n': [i for i in range(0, int(self.N) + 1)],
            'x': self.x_n_val,
            'f': [self.evaluar_f(self.x0, self.y0)],
            'y': [self.y0],
        }

        for i in range(1, int(self.N)+1):
            data['y'].append(data['y'][i-1]+(self.delta_x()*data['f'][i-1]))

            f_value = self.evaluar_f(data['x'][i], data['y'][i])
            data['f'].append(f_value)

        return data

    def get_data(self) -> dict:
        data: int = self.algoritmo()

        self.resultado = data['y'][-1]
        self.save()

        serialized_data: list = []

        for i in range(0, int(self.N)+1):  # Asegúrate de incluir el valor N en el rango
            serialized_data.append({
                'n': str(data['n'][i]),
                'x': str(data['x'][i]),
                'f': str(data['f'][i]),
                'y': str(data['y'][i]),
            })

        return serialized_data
