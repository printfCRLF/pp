import numpy as np
import matplotlib.pyplot as plt


population = np.array(
    [104.96714153,   98.61735699,  106.47688538,  115.23029856,     97.65846625,   97.65863043,  115.79212816,  107.67434729,
     95.30525614,  105.42560044,   95.36582307,   95.34270246,     102.41962272,   80.86719755,   82.75082167,   94.37712471,
     89.8716888,  103.14247333,   90.91975924,   85.87696299,     114.65648769,   97.742237,  100.67528205,   85.75251814,
     94.55617275,  101.1092259,   88.49006423,  103.75698018,     93.9936131,   97.0830625,   93.98293388,  118.52278185,
     99.86502775,   89.42289071,  108.22544912,   87.7915635,     102.08863595,   80.40329876,   86.71813951,  101.96861236,
     107.3846658,  101.71368281,   98.84351718,   96.98896304,     85.2147801,   92.80155792,   95.39361229,  110.57122226,
     103.4361829,   82.36959845,  103.24083969,   96.1491772,     93.23078,  106.11676289,  110.30999522,  109.31280119,
     91.60782477,   96.90787624,  103.31263431,  109.75545127,     95.20825762,   98.14341023,   88.93665026,   88.03793376,
     108.12525822,  113.56240029,   99.27989878,  110.03532898,     103.61636025,   93.54880245,  103.61395606,  115.38036566,
     99.64173961,  115.64643656,   73.80254896,  108.21902504,     100.87047068,   97.0099265,  100.91760777,   80.12431085,
     97.80328112,  103.57112572,  114.77894045,   94.81729782,     91.91506397,   94.98242956,  109.15402118,  103.2875111,
     94.70239796,  105.13267433,  100.97077549,  109.68644991,     92.97946906,   96.72337853,   96.07891847,   85.36485052,
     102.96120277,  102.61055272,  100.05113457,   97.65412867,     85.84629258,   95.79354677,   96.57285483,   91.97722731,
     98.38714288,  104.04050857,  118.86185901,  101.74577813,     102.57550391,   99.25554084,   80.81228785,   99.73486125,
     100.6023021,  124.63242112,   98.07639035,  103.01547342,     99.6528823,   88.31321962,  111.42822815,  107.51933033,
     107.91031947,   90.90612545,  114.02794311,   85.98148937,     105.86857094,  121.90455626,   90.09463675,   94.3370227,
     100.99651365,   94.96524346,   84.49336569,  100.68562975,     89.37696286,  104.73592431,   90.80575766,  115.49934405,
     92.16746708,   96.77938484,  108.13517217,   87.69135684,     102.27459935,  113.07142754,   83.92516765,  101.84633859,
     102.59882794,  107.81822872,   87.63049289,   86.79543387,     105.21941566,  102.96984673,  102.5049285,  103.46448209,
     93.19975278,  102.32253697,  102.93072473,   92.85648582,     118.65774511,  104.73832921,   88.08696503,  106.56553609,
     90.2531833,  107.87084604,  111.58595579,   91.79317682,     109.63376129,  104.12780927,  108.2206016,  118.96792983,
     97.54611884,   92.46263836,   91.1048557,   91.84189715,     99.22898291,  103.41151975,  102.76690799,  108.27183249,
     100.13001892,  114.53534077,   97.35343167,  127.20169167,     106.25667348,   91.42842444,   89.29107502,  104.82472415,
     97.76537215,  107.14000494,  104.73237625,   99.27171087,     91.53206282,   84.85152775,   95.53485048,  108.56398794,
     102.14093744,   87.54261221,  101.73180926,  103.8531738,     91.16142564,  101.53725106,  100.58208718,   88.57029702,
     103.5778736,  105.60784526,  110.83051243,  110.53802052,     86.22330632,   90.6217496,  105.15035267,  105.13785951,
     105.15047686,  138.52731491,  105.70890511,  111.3556564,     109.54001763,  106.51391251,   96.84730755,  107.5896922,
     92.27174785,   97.63181393,   95.14636452,  100.81874139,     123.14658567,   81.32734807,  106.8626019,   83.87284129,
     95.28068134,  110.88950597,  100.64280019,   89.22255222,     92.84696291,  106.79597749,   92.69633368,  102.1645859,
     100.4557184,   93.48399652,  121.43944089,  106.33919022,     79.74857413,  101.86454315,   93.38213535,  108.52433335,
     92.07479262,   98.85263559,  105.04987279,  108.65755194,     87.99703593,   96.65498764,   95.25054689,   93.46670767,
     117.6545424,  104.04981711,   87.39116046,  109.17861947,     121.22156197,  110.32465261,   84.80630034,   95.15765927,
     112.66911149,   92.92330534,  104.43819428,  107.74634053,     90.73069528,   99.40474644,   67.5873266,   89.75612359,
     97.47431849,   87.52216818,  116.32411304,   85.69858622,     95.59955513,  101.30740577,  114.41273289,   85.64137849,
     111.63163752,  100.10233061,   90.18491349,  104.62103474,     101.99059696,   93.99783123,  100.69802085,   96.14686403,
     101.13517345,  106.62130675,  115.86016816,   87.62184501,     121.33033375,   80.479122,   98.48214905,  105.88317206,
     102.80991868,   93.7730048,   97.9187775,   95.06999065,     94.10635243,  108.49602097,  103.57015486,   93.07090405,
     108.99599875,  103.07299521,  108.12862119,  106.29628842,     91.71004989,   94.3981896,  107.47293605,  106.10370265,
     99.79098406,  101.17327383,  112.77664896,   94.08428611,     105.47097381,   97.97807348])


def sample_statistics_versus_population():
    # Compute the population statistics
    print("Population mean {:.1f}, stdev {:.2f}".format(
        population.mean(), population.std()))

    # Set random seed for reproducibility
    np.random.seed(42)

    # Construct a sample by randomly sampling 31 points from the population
    sample = np.random.choice(population, size=31)

    # Compare sample statistics to the population statistics
    print("    Sample mean {:.1f}, stdev {:.2f}".format(
        sample.mean(), sample.std()))


def variation_in_sample_statistics():
    # Initialize two arrays of zeros to be used as containers
    num_samples = 100
    num_pts = 1000
    means = np.zeros(num_samples)
    stdevs = np.zeros(num_samples)

    # For each iteration, compute and store the sample mean and sample stdev
    for ns in range(num_samples):
        sample = np.random.choice(population, num_pts)
        means[ns] = sample.mean()
        stdevs[ns] = sample.std()

    # Compute and print the mean() and std() for the sample statistic distributions
    print("Means:  center={:>6.2f}, spread={:>6.2f}".format(
        means.mean(), means.std()))
    print("Stdevs: center={:>6.2f}, spread={:>6.2f}".format(
        stdevs.mean(), stdevs.std()))


def get_sample_statistics(population, num_samples=100, num_pts=1000):
    means = np.zeros(num_samples)
    deviations = np.zeros(num_samples)
    for ns in range(num_samples):
        sample = np.random.choice(population, num_pts)
        means[ns] = sample.mean()
        deviations[ns] = sample.std()
    return means, deviations


def plot_hist(data, bins, data_name, color='blue'):
    font_options = {'family': 'Arial', 'size': 16}
    plt.rc('font', **font_options)
    fig, axis = plt.subplots(figsize=(8, 4))
    axis.hist(data, bins=bins, rwidth=0.9, color=color)
    title = 'Distribution of the {}: \ncenter={:0.2f}, spead={:0.2f}'.format(
        data_name, data.mean(), data.std())
    x_label = 'Values of {}'.format(data_name)
    y_label = 'Bin counts of {}'.format(data_name)
    axis.set_ylabel(y_label)
    axis.set_xlabel(x_label)
    axis.set_title(title)
    plt.show()
    return fig


def visualization_variation_of_a_statistic():
    # Generate sample distribution and associated statistics
    means, stdevs = get_sample_statistics(
        population, num_samples=100, num_pts=1000)

    # Define the binning for the histograms
    mean_bins = np.linspace(97.5, 102.5, 51)
    std_bins = np.linspace(7.5, 12.5, 51)

    # Plot the distribution of means, and the distribution of stdevs
    fig = plot_hist(data=means, bins=mean_bins,
                    data_name="Means", color='green')
    fig = plot_hist(data=stdevs, bins=std_bins,
                    data_name="Stdevs", color='red')


# sample_statistics_versus_population()
# variation_in_sample_statistics()
visualization_variation_of_a_statistic()
