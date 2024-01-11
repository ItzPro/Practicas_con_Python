# Importar las bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Generar datos ficticios
np.random.seed(42)
X = np.random.rand(100, 1)
y = 2 * X.squeeze() + np.random.randn(100)  # y = 2x + ruido

# Crear un DataFrame usando Pandas
data = pd.DataFrame({'X': X.squeeze(), 'y': y})

# Visualizar los datos
plt.scatter(data['X'], data['y'])
plt.title('Datos generados')
plt.xlabel('X')
plt.ylabel('y')
plt.show()

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar un modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
print(f'Error cuadrático medio: {mse}')

# Visualizar la línea de regresión
plt.scatter(X_test, y_test)
plt.plot(X_test, y_pred, color='red')
plt.title('Regresión lineal')
plt.xlabel('X')
plt.ylabel('y')
plt.show()
