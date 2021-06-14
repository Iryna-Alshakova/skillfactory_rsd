from sklearn.datasets import load_breast_cancer
X, y = load_breast_cancer(return_X_y=True)
X = X[:, 0].reshape(-1,1)

from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(X,y)

import pickle
with open('cancer_predictor.pkl', 'wb') as output:
    pickle.dump(log_reg, output)