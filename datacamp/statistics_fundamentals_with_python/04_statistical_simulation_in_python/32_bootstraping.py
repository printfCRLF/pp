import numpy as np
import statsmodels.api as sm
from data import wrench_lengths


def running_a_simple_bootstrap():

    # Draw some random sample with replacement and append mean to mean_lengths.
    mean_lengths, sims = [], 1000
    for i in range(sims):
        temp_sample = np.random.choice(
            wrench_lengths, replace=True, size=len(wrench_lengths))
        sample_mean = np.mean(temp_sample)
        mean_lengths.append(sample_mean)

    # Calculate bootstrapped mean and 95% confidence interval.
    boot_mean = np.mean(mean_lengths)
    boot_95_ci = np.percentile(mean_lengths, [2.5, 97.5])
    print("Bootstrapped Mean Length = {}, 95% CI = {}".format(boot_mean, boot_95_ci))


def non_standard_estimators():
    # Sample with replacement and calculate quantities of interest
    sims, data_size, height_medians, hw_corr = 1000, df.shape[0], [], []
    for i in range(sims):
        tmp_df = df.sample(n=data_size, replace=True)
        height_medians.append(tmp_df['heights'].median())
        hw_corr.append(tmp_df.weights.corr(tmp_df.heights))

    # Calculate confidence intervals
    height_median_ci = np.percentile(height_medians, [2.5, 97.5])
    height_weight_corr_ci = np.percentile(hw_corr, [2.5, 97.5])
    print("Height Median CI = {} \nHeight Weight Correlation CI = {}".format(
        height_median_ci, height_weight_corr_ci))


def bootstrapping_regression():
    rsquared_boot, coefs_boot, sims = [], [], 1000
    reg_fit = sm.OLS(df['y'], df.iloc[:, 1:]).fit()

    # Run 1K iterations
    for i in range(sims):
        # First create a bootstrap sample with replacement with n=df.shape[0]
        bootstrap = df.sample(n=df.shape[0], replace=True)
        # Fit the regression and append the r square to rsquared_boot
        rsquared_boot.append(
            sm.OLS(bootstrap['y'], bootstrap.iloc[:, 1:]).fit().rsquared)

    # Calculate 95% CI on rsquared_boot
    r_sq_95_ci = np.percentile(rsquared_boot, [2.5, 97.5])
    print("R Squared 95% CI = {}".format(r_sq_95_ci))
