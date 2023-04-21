import matplotlib.pyplot as plt
import numpy as np

# Creamos un arreglo de números complejos z
x = np.linspace(-2, 2, 200)
y = np.linspace(-2, 2, 200)
z = x[:,None] + y[None,:]*1j

# Aplicamos el mapeo w = z^2
w = z**2

# Graficamos los resultados
plt.figure(figsize=(8,6))
plt.imshow(np.angle(w), cmap='hsv', extent=[-2,2,-2,2])
plt.title('Mapeo complejo w = z^2')
plt.xlabel('Parte real de z')
plt.ylabel('Parte imaginaria de z')
plt.colorbar()
plt.show()
