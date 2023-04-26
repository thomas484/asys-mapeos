import matplotlib
import numpy as np

# Creamos un arreglo de números complejos z
x = np.linspace(-2, 2, 200)
y = np.linspace(-2, 2, 200)
z = x[:,None] + y[None,:]*1j

# Aplicamos el mapeo w = z^2
w = z**2

# Graficamos los resultados
matplotlib.figure(figsize=(8,6))
matplotlib.imshow(np.angle(w), cmap='hsv', extent=[-2,2,-2,2])
matplotlib.title('Mapeo complejo w = z^2')
matplotlib.xlabel('Parte real de z')
matplotlib.ylabel('Parte imaginaria de z')
matplotlib.colorbar()
matplotlib.show()
