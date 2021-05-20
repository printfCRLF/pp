import numpy as np
import matplotlib.pyplot as plt
import util
import seaborn as sns


x = np.array([3.20141089,  3.57332076,  4.2284669,  4.27233051,  4.49370529,
              4.5713193,  4.74611933,  4.9143694,  5.06416613,  5.12046366,  5.1332596,
              5.1382451,  5.19463348,  5.30012277,  5.32111385,  5.361098,  5.3622485,
              5.42139975,  5.55601804,  5.56564872,  5.57108737,  5.60910021,  5.74438063,
              5.82636432,  5.85993128,  5.90529103,  5.98816951,  6.00284592,  6.2829785,
              6.28362732,  6.33858905,  6.3861864,  6.41291216,  6.57380586,  6.68822271,
              6.73736858,  6.9071052,  6.92746243,  6.97873601,  6.99734545,  7.0040539,
              7.17582904,       7.26593626,  7.49073203,  7.49138963,  7.65143654,  8.18678609,
              8.20593008,  8.23814334,  8.39236527, ])

y = np.array([146.48264883,  167.75876162,  229.73232314,  205.23686657,  224.99693822,
              239.79378267,  246.65838372,  264.14477475,  268.91257002,  267.25180588,
              248.54953839,  265.25831322,  263.03153004,  251.08035094,  280.93733241,
              276.53088378,  268.59007072,  268.62252076,  265.21874,  280.37743899,
              283.47297931,  271.72788298,  299.42217399,  279.79758387,  270.70401032,
              306.18168601,  295.17313188,  298.81898515,  305.35499931,  297.3187572,
              330.10944498,  312.07619563,  338.08560914,  337.16702908,  331.10617501,
              325.46645358,  337.66440893,  333.64162871,  370.85149057,  351.59390525,
              362.27985309,  345.48425572,  365.1976818,  386.90415177,  371.05186831,
              393.39852867,  397.95134137,  395.98005292,  415.89087335,  415.63691073, ])


def mean_deviation_standard_deviation():
    # Compute the deviations by subtracting the mean offset
    dx = x - np.mean(x)
    dy = y - np.mean(y)

    # Normalize the data by dividing the deviations by the standard deviation
    zx = dx / np.std(x)
    zy = dy / np.std(y)

    # Plot comparisons of the raw data and the normalized data
    fig = plot_cdfs(dx, dy, zx, zy)


def plot_cdfs(dx, dy, zx, zy):
    """
    Cumulative distribution function
    """
    array_index = list(range(len(x)))
    fig, axes = plt.subplots(nrows=2, ncols=1)
    axes[0].plot(array_index, dx, color="blue")
    axes[0].plot(array_index, dy, color="red")
    axes[0].set_ylabel("Deviations of X and Y")
    axes[1].plot(array_index, zx, color="blue")
    axes[1].plot(array_index, zy, color="red")
    axes[1].set_ylabel("Normalized Deviations of X and Y")
    axes[1].set_xlabel("Array Index")
    plt.show()


def plot_normalized_deviations(zx, zy, correlation):
    fig, axis = plt.subplots()
    lines = axis.plot(zx * zy, color="purple")
    axis.axhline(0, color="black", linestyle="--")
    axis.set_ylabel("Product of Normalized Deviations")
    axis.set_xlabel("Array Index")
    axis.set_title(
        "Correlation = np.mean(zx*zy) = {:0.2f}".format(correlation))
    plt.show()
    return fig


def covariance_vs_correlation():
    # Compute the covariance from the deviations.
    dx = x - np.mean(x)
    dy = y - np.mean(y)
    covariance = np.mean(dx * dy)
    print("Covariance: ", covariance)

    # Compute the correlation from the normalized deviations.
    zx = dx / np.std(x)
    zy = dy / np.std(y)
    correlation = np.mean(zx * zy)
    print("Correlation: ", correlation)

    # Plot the normalized deviations for visual inspection.
    fig = plot_normalized_deviations(zx, zy, correlation)


def correlation(x, y):
    x_dev = x - np.mean(x)
    y_dev = y - np.mean(y)
    x_norm = x_dev / np.std(x)
    y_norm = y_dev / np.std(y)
    return np.mean(x_norm * y_norm)


def correlation_strength():
    data_sets = {
        "A": {
            "correlation": np.nan,
            "x": np.array([2.55041235, 2.60839969, 2.79619981, 2.84385271, 3.15184751, 3.21906477,
                           3.23462037, 3.33976744, 3.47394544, 3.56125803, 3.67786134,
                           3.7339611, 3.86496991, 4.10019474, 4.24786673, 4.24920164,
                           4.29714059, 4.31952159, 4.41315702, 4.41783781, 4.42072788,
                           4.42420154, 4.62362038, 4.63538281, 4.70730828, 4.7073288,
                           4.71777962, 4.82716962, 4.85543965, 4.98312847, 5.08441026,
                           5.13865324, 5.21421035, 5.24607654, 5.26107949, 5.30245284,
                           5.39280917, 5.42952286, 5.46962252, 5.62089269, 5.67820005,
                           5.80961067, 5.92308322, 5.95929341, 6.02818114, 6.32140278,
                           6.83206096, 6.90378732, 6.97401602, 7.31534773, ]),
            "y": np.array([5.18184568, 5.12052882, 5.42316911, 5.84062449, 6.5614449, 6.67094956,
                           6.25943637, 6.60223178, 7.03070673, 7.36640234, 7.23592912, 7.42150745,
                           7.45335607, 7.90133782, 8.69886493, 8.83746328, 8.57627865, 8.88992641, 8.91672304,
                           8.67439568, 8.93180467, 9.23291221, 9.23828425, 9.66192654, 8.75968029,
                           9.62013323, 9.45732102, 9.57958741, 9.73381949, 9.46936471, 10.11390254,
                           10.36658462, 10.79789421, 10.36258554, 10.32003559, 10.47946642, 11.01446886,
                           10.9412335, 10.80680499, 11.37010224, 11.3806695, 11.86138259, 11.67065318,
                           11.83667129, 11.95833524, 12.27692683, 13.73815199, 13.87283846, 13.9493104,
                           14.57204868, ]),
        },
        "B": {
            "correlation": np.nan,
            "x": np.array([2.19664381,  2.406278,  2.47343147,  2.72871597,  3.06636806,
                           3.51128038,  3.87855402,  4.09926408,  4.18003832,  4.20434562,
                           4.29194259,  4.41336839,  4.50269971,  4.58240329,  4.59650649,
                           4.60918513,  4.74669209,  4.77111432,  4.82900646,  4.84738553,
                           5.00264796,  5.01962047,  5.02286149,  5.04517742,  5.09524948,
                           5.15589119,  5.24177672,  5.26908573,  5.30974025,  5.36136493,
                           5.42179707,  5.50681676,  5.58929395,  5.69179864,  5.84444261,
                           5.94426748,  6.05209339,  6.07448552,  6.07964661,  6.10895368,
                           6.19165516,  6.23993253,  6.30742282,  6.30947322,  6.32371148,
                           6.43754466,  6.64768944,  6.65144774,  6.79088371,  7.98870064, ]),
            "y": np.array([7.75732279,   -0.97068431,   -0.66103018,   5.05375913,   3.93976632,
                           6.44408273,   9.17318937,   8.05647607,   10.62302986,   14.59132646,
                           4.68693984,   8.54535728,   10.23727485,   8.33081153,   13.32821592,
                           -0.38344428,   17.61579867,   4.97170349,   10.50554646,   12.51365356,
                           6.86355506,   11.88747988,   12.86263588,   12.18438671,   6.48548172,
                           18.34315419,   11.39140361,   5.92753502,   13.14739828,   10.8807806,
                           12.70116343,   3.24043311,   16.46301037,   11.99411949,   12.34700338,
                           10.16815219,   15.17366173,   16.0886504,   13.24263662,   17.78585212,
                           12.70267957,   10.88000673,   8.5034434,   10.28007359,   15.91379868,
                           12.5473011,   11.91631483,   15.41604806,   9.30581229,   13.92987605,
                           ]),
        },
        "C": {
            "correlation": np.nan,
            "x": np.array([1.50176362,  1.96665095,  2.78558362,  2.84041313,  3.11713161,
                           3.21414912,  3.43264917,  3.64296175,  3.83020766,  3.90057957,
                           3.9165745,  3.92280638,  3.99329185,  4.12515346,  4.15139231,
                           4.2013725,  4.20281062,  4.27674969,  4.44502255,  4.45706091,
                           4.46385921,  4.51137526,  4.68047579,  4.7829554,  4.8249141,
                           4.88161379,  4.98521188,  5.00355739,  5.35372312,  5.35453415,
                           5.42323631,  5.482733,  5.5161402,  5.71725733,  5.86027839,
                           5.92171072,  6.13388149,  6.15932804,  6.22342001,  6.24668181,
                           6.25506737,  6.46978631,  6.58242032,  6.86341504,  6.86423703,
                           7.06429567,  7.73348261,  7.7574126,  7.79767917,  7.99045658,
                           ]),
            "y": np.array([-17.70183793,  -12.68730947,  33.47056284,  -7.0881775,  6.7091949,
                           23.53735376,  21.11660059,  35.3641024,  31.59072152,  24.91144186,
                           -4.53019043,  20.56341545,  13.01493562,  -12.96994045,  30.97956936,
                           21.31852956,  9.13346253,  4.82402639,  -10.28277321,  12.10650699,
                           16.42274434,  -4.27572923,  27.95621636,  -7.98933795,  -24.3197774,
                           26.39886103,  3.51656715,  7.99064142,  -2.69282132,  -14.98633586,
                           30.93027062,  -0.05643774,  37.60752021,  24.35144564,  6.68442643,
                           -5.53101698,  0.5483712,  -7.08171402,  45.84065377,  15.1244233,
                           30.91342343,  -7.33806017,  16.06140272,  32.57262109,  8.36830187,
                           30.62642269,  -1.88612137,  -6.30071951,  21.66576814,  9.91409021, ]),
        },
    }

    # Compute and store the correlation for each data set in the list.
    for name, data in data_sets.items():
        data["correlation"] = correlation(data["x"], data["y"])
        print("data set {} has correlation {:.2f}".format(
            name, data["correlation"]))

        # Assign the data set with the best correlation.
        best_data = data_sets["A"]


sns.set()
# mean_deviation_standard_deviation()
covariance_vs_correlation()
# correlation_strength()