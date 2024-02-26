import joblib
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

joblib.dump(model, "py/model.joblib")
