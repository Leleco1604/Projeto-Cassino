import random
import numpy as np
from sklearn.linear_model import LogisticRegression

# Gerar conjunto de dados de treinamento
num_jogadas = 1000
num_features = 10
X = np.zeros((num_jogadas, num_features))
y = np.zeros(num_jogadas)

for i in range(num_jogadas):
    numeros = []
    for j in range(num_features):
        numeros.append(random.randint(0, 30))
        if numeros[-1] % 2 == 0:
            X[i, j] = 1
    if numeros[-1] % 2 == 0:
        y[i] = 1

# Treinar modelo de regressão logística
modelo = LogisticRegression()
modelo.fit(X, y)

# Função para prever próximo resultado do jogo de cassino
def prever_proximo(numeros):
    X_pred = np.zeros(num_features)
    for i in range(num_features):
        if numeros[i] % 2 == 0:
            X_pred[i] = 1
    y_pred = modelo.predict(X_pred.reshape(1, -1))
    if y_pred[0] == 1:
        return "vermelho"
    else:
        return "preto"

# Exemplo de uso
numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(prever_proximo(numeros))
