from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error as MSE
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pylab as plt
from data import load_bike_sharing_data


def random_forest_in_action(X_train, X_test, y_train, y_test):
    # Instantiate rf
    rf = RandomForestRegressor(n_estimators=25, random_state=2)
    # Fit rf to the training set
    rf.fit(X_train, y_train)

    # Predict the test set labels
    y_pred = rf.predict(X_test)
    # Evaluate the test set RMSE
    rmse_test = MSE(y_test, y_pred)**(1/2)
    # Print rmse_test
    print('Test set RMSE of rf: {:.2f}'.format(rmse_test))

    # Create a pd.Series of features importances
    importances = pd.Series(data=rf.feature_importances_,
                            index=X_train.columns)

    # Sort importances
    importances_sorted = importances.sort_values()

    # Draw a horizontal barplot of importances_sorted
    importances_sorted.plot(kind='barh', color='lightgreen')
    plt.title('Features Importances')
    plt.show()


bikes = load_bike_sharing_data()
X = bikes.drop(columns=["cnt"])
y = bikes["cnt"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
random_forest_in_action(X_train, X_test, y_train, y_test)
