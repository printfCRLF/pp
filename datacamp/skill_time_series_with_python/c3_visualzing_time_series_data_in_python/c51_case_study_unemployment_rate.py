import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


def explore_jobs_dataset():
    # Read in jobs file
    jobs = pd.read_csv("data/ch5_employment.csv")
    # Print first five lines of your DataFrame
    print(jobs.head(5))
    # Check the type of each column in your DataFrame
    print(jobs.dtypes)
    # Convert datestamp column to a datetime object
    jobs["datestamp"] = pd.to_datetime(jobs["datestamp"])
    # Set the datestamp columns as the index of your DataFrame
    jobs = jobs.set_index('datestamp')
    # Check the number of missing values in each column
    print(jobs.isnull().sum())

    return jobs


def describe_time_series_with_boxplots(jobs):
    # Generate a boxplot
    jobs.boxplot(fontsize=6, vert=False)
    plt.show()
    # Generate numerical summaries
    print(jobs.describe())
    # Print the name of the time series with the highest mean
    print("Agriculture")
    # Print the name of the time series with the highest variability
    print("Construction")


def plot_all_the_time_series_in_your_dataset(jobs):
    # A subset of the jobs DataFrame
    jobs_subset = jobs[['Finance', 'Information',
                        'Manufacturing', 'Construction']]
    # Print the first 5 rows of jobs_subset
    print(jobs_subset.head())

    # Create a facetted graph with 2 rows and 2 columns
    axes = jobs_subset.plot(subplots=True, layout=(2, 2),
                            sharex=False, sharey=False,
                            linewidth=0.7, fontsize=3, legend=False)
    plt.show()


def annotate_significant_events_in_time_series_data(jobs):
    # Plot all time series in the jobs DataFrame
    ax = jobs.plot(colormap="Spectral", fontsize=6, linewidth=0.8)

    # Set labels and legend
    ax.set_xlabel('Date', fontsize=10)
    ax.set_ylabel('Unemployment Rate', fontsize=10)
    ax.set_title('Unemployment rate of U.S. workers by industry', fontsize=10)
    ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

    # Annotate your plots with vertical lines
    ax.axvline(x="2001-07-01", color='blue', linestyle='--', linewidth=0.8)
    ax.axvline(x="2008-09-01", color='blue', linestyle='--', linewidth=0.8)

    # Show plot
    plt.show()


def plot_monthly_trend(jobs):
    # Extract the month from the index of jobs
    index_month = jobs.index.month

    # Compute the mean unemployment rate for each month
    jobs_by_month = jobs.groupby(index_month).mean()

    # Plot the mean unemployment rate for each month
    ax = jobs_by_month.plot(fontsize=6, linewidth=1)

    # Set axis labels and legend
    ax.set_xlabel('Month', fontsize=10)
    ax.set_ylabel('Mean unemployment rate', fontsize=10)
    ax.legend(bbox_to_anchor=(0.8, 0.6), fontsize=10)
    plt.show()


def plot_yearly_trend(jobs):
    # Extract of the year in each date indices of the jobs DataFrame
    index_year = jobs.index.year

    # Compute the mean unemployment rate for each year
    jobs_by_year = jobs.groupby(index_year).mean()

    # Plot the mean unemployment rate for each year
    ax = jobs_by_year.plot(fontsize=6, linewidth=1)

    # Set axis labels and legend
    ax.set_xlabel('Year', fontsize=10)
    ax.set_ylabel('Mean unemployment rate', fontsize=10)
    ax.legend(bbox_to_anchor=(0.1, 0.5), fontsize=10)
    plt.show()


def decompose_your_dataset(jobs):
    # Initialize dictionary
    jobs_decomp = {}
    # Get the names of each time series in the DataFrame
    jobs_names = jobs.columns
    # Run time series decomposition on each time series of the DataFrame
    for ts in jobs_names:
        ts_decomposition = sm.tsa.seasonal_decompose(jobs[ts])
        jobs_decomp[ts] = ts_decomposition

    # Extract the seasonal values for the decomposition of each time series
    jobs_seasonal = {}
    for ts in jobs_names:
        jobs_seasonal[ts] = jobs_decomp[ts].seasonal

    # Create a DataFrame from the jobs_seasonal dictionary
    seasonality_df = pd.DataFrame.from_dict(jobs_seasonal)
    # Remove the label for the index
    seasonality_df.index.name = None
    # Create a faceted plot of the seasonality_df DataFrame
    seasonality_df.plot(subplots=True, layout=(4, 4), sharey=False,
                        fontsize=2, linewidth=0.3, legend=False)
    # Show plot
    plt.show()

    return seasonality_df


def correlation_between_multiple_time_series(seasonality_df):
    # Get correlation matrix of the seasonality_df DataFrame
    seasonality_corr = seasonality_df.corr(method="spearman")

    # Customize the clustermap of the seasonality_corr correlation matrix
    fig = sns.clustermap(seasonality_corr, annot=True, annot_kws={
                         "size": 4}, linewidths=.4, figsize=(15, 10))
    plt.setp(fig.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)
    plt.setp(fig.ax_heatmap.xaxis.get_majorticklabels(), rotation=90)
    plt.show()

    # Print the correlation between the seasonalities of the Government and Education & Health industries
    print(0.89)


if __name__ == "__main__":
    sns.set()
    jobs = explore_jobs_dataset()
    # describe_time_series_with_boxplots(jobs)
    # plot_all_the_time_series_in_your_dataset(jobs)
    # annotate_significant_events_in_time_series_data(jobs)
    # plot_monthly_trend(jobs)
    # plot_yearly_trend(jobs)
    seasonality_df = decompose_your_dataset(jobs)
    correlation_between_multiple_time_series(seasonality_df)
