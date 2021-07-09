from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error as MSE
from sklearn.model_selection import GridSearchCV, train_test_split
from data import load_bike_sharing_data


bikes = load_bike_sharing_data()
X = bikes.drop(columns=["cnt"])
y = bikes["cnt"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1)

SEED = 1
rf = RandomForestRegressor(random_state=SEED)

# Define the dictionary 'params_rf'
params_rf = {
    "n_estimators": [100, 350, 500],
    "max_features": ["log2", "auto", "sqrt"],
    "min_samples_leaf": [2, 10, 30]
}

# Instantiate grid_rf
grid_rf = GridSearchCV(estimator=rf, param_grid=params_rf, scoring="neg_mean_squared_error",
                       cv=3, verbose=1, n_jobs=-1)

grid_rf.fit(X_train, y_train)

# Extract the best estimator
best_model = grid_rf.best_estimator_

# Predict test set labels
y_pred = best_model.predict(X_test)

# Compute rmse_test
rmse_test = MSE(y_test, y_pred)**(1/2)

# Print rmse_test
print('Test RMSE of best model: {:.3f}'.format(rmse_test))
