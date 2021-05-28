import scipy.stats as st
import numpy as np


def power_analysis():
    # Initialize effect_size, control_mean, control_sd
    effect_size, sample_size, control_mean, control_sd = 0.05, 50, 1, 0.5

    # Simulate control_time_spent and treatment_time_spent, assuming equal variance
    control_time_spent = np.random.normal(
        loc=control_mean, scale=control_sd, size=sample_size)
    treatment_time_spent = np.random.normal(
        loc=control_mean*(1+effect_size), scale=control_sd, size=sample_size)

    # Run the t-test and get the p_value
    t_stat, p_value = st.ttest_ind(treatment_time_spent, control_time_spent)
    stat_sig = p_value < 0.05
    print("P-value: {}, Statistically Significant? {}".format(p_value, stat_sig))


def power_analysis_2():
    effect_size, sample_size, control_mean, control_sd = 0.05, 50, 1, 0.5
    sims = 1000

    # Keep incrementing sample size by 10 till we reach required power
    while 1:
        control_time_spent = np.random.normal(
            loc=control_mean, scale=control_sd, size=(sample_size, sims))
        treatment_time_spent = np.random.normal(
            loc=control_mean*(1+effect_size), scale=control_sd, size=(sample_size, sims))
        t, p = st.ttest_ind(treatment_time_spent, control_time_spent)

        # Power is the fraction of times in the simulation when the p-value was less than 0.05
        power = (p < 0.05).sum()/sims
        if power >= 0.8:
            break
        else:
            sample_size += 10
    print("For 80% power, sample size required = {}".format(sample_size))


# power_analysis_1()
power_analysis_2()
