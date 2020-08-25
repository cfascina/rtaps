# Modelo preditivo de classificação para prever o valor de uma variável binária (true ou false) a partir de dados numéricos

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

# Reduzindo a dimensionalidade para 3 componentes
pca = PCA(n_components = 3) 

# Aplique o PCA aos datasets
newdf_treino = pca.fit_transform(df_treino.drop("target", axis = 1))
newdf_teste = pca.transform(df_teste.drop("target", axis = 1)) 

# Crie dataframes do pandas com o resultado do item anterior
features_treino = pd.DataFrame(newdf_treino)
features_teste = pd.DataFrame(newdf_teste)  

# Crie um modelo de regressão logística
regr = LogisticRegression() 

# Usando o recurso de pipeline do scikit-learn para encadear 2 algoritmos em um mesmo modelo, use o resultado do PCA como entrada para Regressão Logística
pipe = Pipeline([('pca', pca), ('logistic', regr)])
pipe.fit(features_treino, df_treino["target"])

# Faça previsões com o modelo treinado
predictions = pipe.predict(features_teste)

# Imprimindo as previsões
print("\nPrevisões do modelo:")
print(predictions)

