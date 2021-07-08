from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as MSE
from data import load_automobile_data


def instantiate_the_model():
    # Instantiate a DecisionTreeRegressor dt
    dt = DecisionTreeRegressor(
        max_depth=4, min_samples_leaf=0.26, random_state=SEED)

    return dt


def evaluate_the_10_fold_cv_error(X_train, X_test, y_train, y_test, dt):
    # Compute the array containing the 10-folds CV MSEs
    MSE_CV_scores = - cross_val_score(dt, X_train, y_train, cv=10,
                                      scoring='neg_mean_squared_error',
                                      n_jobs=-1)

    # Compute the 10-folds CV RMSE
    RMSE_CV = (MSE_CV_scores.mean())**(1/2)

    # Print RMSE_CV
    print('CV RMSE: {:.2f}'.format(RMSE_CV))


def evaluate_the_trainning_error(X_train, X_test, y_train, y_test, dt):
    # Fit dt to the training set
    dt.fit(X_train, y_train)

    # Predict the labels of the training set
    y_pred_train = dt.predict(X_train)

    # Evaluate the training set RMSE of dt
    RMSE_train = (MSE(y_train, y_pred_train))**(1/2)

    # Print RMSE_train
    print('Train RMSE: {:.2f}'.format(RMSE_train))


X, y = load_automobile_data()
SEED = 1
# Split the data into 70% train and 30% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=SEED)
dt = instantiate_the_model()
evaluate_the_10_fold_cv_error(X_train, X_test, y_train, y_test, dt)
evaluate_the_trainning_error(X_train, X_test, y_train, y_test, dt)


baseline_RMSE = 5.1
print("baseline RMSE above which a model is considered to be underfitting and \
    below which the model is considered good  enough", baseline_RMSE)

# Even if CV error and Training error are close to each other, we shall still perfer 
# CV error to training error
# CV error is an improved version of training error, it still uses training data set. 
