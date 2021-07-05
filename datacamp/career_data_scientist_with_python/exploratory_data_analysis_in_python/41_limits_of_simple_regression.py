from scipy.stats import linregress
import statsmodels.formula.api as smf
from data import load_brfss_data


def using_stats_model_for_linear_regression_for_two_variables(brfss):
    # Run regression with linregress
    subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])
    xs = subset['INCOME2']
    ys = subset['_VEGESU1']
    res = linregress(xs, ys)
    print(res)

    # Run regression with StatsModels
    results = smf.ols('INCOME2 ~ _VEGESU1', data=subset).fit()
    print(results.params)


brfss = load_brfss_data()
using_stats_model_for_linear_regression_for_two_variables(brfss)
