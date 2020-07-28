# Modelo preditivo de classificaçãp para prever o valor de uma variável binária (true ou false) a partir de dados numéricos

# Import dos módulos
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings("ignore")

# Dados de treino
n_train = 10
np.random.seed(0)
df_treino = pd.DataFrame({"var1": np.random.random(n_train), \
                          "var2": np.random.random(n_train), \
                          "var3": np.random.random(n_train), \
                          "var4": np.random.randint(0,2,n_train).astype(bool),\
                          "target": np.random.randint(0,2,n_train).astype(bool)})

# Dados de teste
n_test = 3
np.random.seed(1)
df_teste = pd.DataFrame({"var1": np.random.random(n_test), \
                         "var2": np.random.random(n_test), \
                         "var3": np.random.random(n_test), \
                         "var4": np.random.randint(0,2,n_test).astype(bool),\
                         "target": np.random.randint(0,2,n_test).astype(bool)})

# Crie um modelo com PCA para redução de dimensionalidade com 3 componentes


# Aplique o PCA aos datasets


# Crie dataframes do pandas com o resultado do item anterior


# Crie um modelo de regressão logística

# Usando o recurso de pipeline do scikit-learn para encadear 2 algoritmos em um mesmo modelo, concatene o resultado do PCA e Regressão Logística


# Faça previsões com o modelo treinado

# Imprimindo as previsões


