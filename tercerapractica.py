import random

# Libreria para generar grafica
# Para instalar esto necesitas copiar, pegar y ejecutar en terminal
# python -m pip install -U pip
# python -m pip install -U matplotlib
import matplotlib.pyplot as plt

# Genera un numero aleatorio y lo imprime
print(random.randrange(10, 100, 2))

#Declara la lista
lista =[1,2,3,4,5,6,7,8,9]

# Imprime la lista
print('Lista original', lista)

# Randomiza la lista
random.shuffle(lista)

# Imprime la lista mixeada
print('Lista mixeada', lista)

# Genera una grafica de campana de GAUSS
# Genera los datos de la grafica
campana = [random.gauss(1, 0.5) for i in range(1000)]

# Arma la grafica
plt.hist(campana, bins=15)

# muestra la grafica
plt.show()