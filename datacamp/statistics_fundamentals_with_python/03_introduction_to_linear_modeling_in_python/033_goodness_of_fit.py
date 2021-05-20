import numpy as np
import util 


def model_fit_and_predict(x, y):
    a0=150
    a1=25
    ym = a0 + (a1*x)
    return ym

x_data, y_data = util.load_data()
y_model = model_fit_and_predict(x_data, y_data)

def rmse_step_by_step():   
    residuals = y_model - y_data

    # Compute the RSS, MSE, and RMSE and print the results
    RSS = np.sum(np.square(residuals))
    MSE = RSS/len(residuals)
    RMSE = np.sqrt(MSE)
    print('RMSE = {:0.2f}, MSE = {:0.2f}, RSS = {:0.2f}'.format(RMSE, MSE, RSS))


def r_squared(): 
    # Compute the residuals and the deviations
    residuals = y_model - y_data
    deviations = np.mean(y_data) - y_data

    # Compute the variance of the residuals and deviations
    var_residuals = np.mean(np.square(residuals))
    var_deviations = np.mean(np.square(deviations))

    # Compute r_squared as 1 - the ratio of RSS/Variance
    r_squared = 1 - (var_residuals / var_deviations)
    print('R-squared is {:0.2f}'.format(r_squared))


rmse_step_by_step()
r_squared()


