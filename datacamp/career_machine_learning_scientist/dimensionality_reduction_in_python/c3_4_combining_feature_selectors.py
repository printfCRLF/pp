
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso, LassoCV, LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import VarianceThreshold, RFE
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestRegressor
from data import load_ansur_ii_male_data, load_ansur_ii_female_data


def prepare_data():
    ansur_ii_male = load_ansur_ii_male_data().sample(1000)
    cols = ['acromialheight', 'axillaheight', 'bideltoidbreadth', 'buttockcircumference', 'buttockkneelength', 'buttockpopliteallength', 'cervicaleheight', 'chestcircumference', 'chestheight',
            'earprotrusion', 'footbreadthhorizontal', 'forearmcircumferenceflexed', 'handlength', 'headbreadth', 'heelbreadth', 'hipbreadth', 'iliocristaleheight', 'interscyeii',
            'lateralfemoralepicondyleheight', 'lateralmalleolusheight', 'neckcircumferencebase', 'radialestylionlength', 'shouldercircumference', 'shoulderelbowlength', 'sleeveoutseam',
            'thighcircumference', 'thighclearance', 'verticaltrunkcircumferenceusa', 'waistcircumference', 'waistdepth', 'wristheight', 'BMI']
    X = ansur_ii_male[cols]
    y = ansur_ii_male["bicepscircumferenceflexed"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    return X_train, X_test, y_train, y_test, X, y


def feature_selection_from_lasso(X_train, X_test, y_train, y_test):
    # Create and fit the LassoCV model on the training set
    lcv = LassoCV()
    lcv.fit(X_train, y_train)
    print('Optimal alpha = {0:.3f}'.format(lcv.alpha_))

    # Calculate R squared on the test set
    r_squared = lcv.score(X_test, y_test)
    print(
        'The model explains {0:.1%} of the test set variance'.format(r_squared))

    # Create a mask for coefficients not equal to zero
    lcv_mask = lcv.coef_ != 0
    print('{} features out of {} selected'.format(sum(lcv_mask), len(lcv_mask)))

    return lcv_mask


def selected_feature_by_rfe(X_train, X_test, y_train, y_test):
    # Select 10 features with RFE on a GradientBoostingRegressor, drop 3 features on each step
    rfe_gb = RFE(estimator=GradientBoostingRegressor(),
                 n_features_to_select=10, step=3, verbose=1)
    rfe_gb.fit(X_train, y_train)

    # Calculate the R squared on the test set
    r_squared = rfe_gb.score(X_test, y_test)
    print('The model can explain {0:.1%} of the variance in the test set'.format(
        r_squared))

    # Assign the support array to gb_mask
    gb_mask = rfe_gb.support_

    return gb_mask


def selected_feature_from_random_forrest(X_train, X_test, y_train, y_test):
    # Select 10 features with RFE on a RandomForestRegressor, drop 3 features on each step
    rfe_rf = RFE(estimator=RandomForestRegressor(),
                 n_features_to_select=10, step=3, verbose=1)
    rfe_rf.fit(X_train, y_train)

    # Calculate the R squared on the test set
    r_squared = rfe_rf.score(X_test, y_test)
    print('The model can explain {0:.1%} of the variance in the test set'.format(
        r_squared))

    # Assign the support array to gb_mask
    rf_mask = rfe_rf.support_

    return rf_mask


def meta_feature_selection(lcv_mask, rf_mask, gb_mask, X, y):
    # Sum the votes of the three models
    votes = np.sum([lcv_mask, rf_mask, gb_mask], axis=0)

    # Create a mask for features selected by all 3 models
    meta_mask = votes >= 3

    # Apply the dimensionality reduction on X
    X_reduced = X.loc[:, meta_mask]

    # Plug the reduced dataset into a linear regression pipeline
    X_train, X_test, y_train, y_test = train_test_split(
        X_reduced, y, test_size=0.3, random_state=0)
    lm = LinearRegression()
    scaler = StandardScaler()
    lm.fit(scaler.fit_transform(X_train), y_train)
    r_squared = lm.score(scaler.transform(X_test), y_test)
    print('The model can explain {0:.1%} of the variance in the test set using {1:} features.'.format(
        r_squared, len(lm.coef_)))


X_train, X_test, y_train, y_test, X, y = prepare_data()
lcv_mask = feature_selection_from_lasso(X_train, X_test, y_train, y_test)
gb_mask = selected_feature_by_rfe(X_train, X_test, y_train, y_test)
rf_mask = selected_feature_from_random_forrest(
    X_train, X_test, y_train, y_test)
meta_feature_selection(lcv_mask, rf_mask, gb_mask, X, y)
