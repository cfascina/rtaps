import numpy as np
import pandas as pd

from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Training Data
n_training = 10
np.random.seed(0)
df_training = pd.DataFrame({'var_01': np.random.random(n_training), \
                            'var_02': np.random.random(n_training), \
                            'var_03': np.random.random(n_training), \
                            'var_04': np.random.randint(0, 2, n_training).astype(bool),\
                            'target': np.random.randint(0, 2, n_training).astype(bool)})

# Test Data
n_test = 3
np.random.seed(1)
df_test = pd.DataFrame({'var_01': np.random.random(n_test), \
                        'var_02': np.random.random(n_test), \
                        'var_03': np.random.random(n_test), \
                        'var_04': np.random.randint(0, 2, n_test).astype(bool),\
                        'target': np.random.randint(0, 2, n_test).astype(bool)})

# PCA model for dimensionality reduction with 3 components
pca = PCA(n_components = 3)

# PCA Datasets (excluding the target)
pca_training = pca.fit_transform(df_training.drop('target', axis = 1))
pca_test = pca.transform(df_test.drop('target', axis = 1))

# Convert PCA Datasets to Pandas DataFrames
features_training = pd.DataFrame(pca_training)
features_test = pd.DataFrame(pca_test)

# Logist Regression Model
model = LogisticRegression()

# Usando o recurso de pipeline do scikit-learn para encadear 2 algoritmos em um mesmo modelo, concatene o resultado do PCA e Regressão Logística
pipe = Pipeline([('PCA', pca), ('Logistic Regression', model)])
pipe.fit(features_training, df_training['target'])

# Predictions with the trained model
predictions = pipe.predict(features_test)

# Prints the predictions
print(f'Predictions:\n{predictions}')
