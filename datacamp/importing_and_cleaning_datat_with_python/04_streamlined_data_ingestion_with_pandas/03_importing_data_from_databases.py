import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt 

engine = create_engine("sqlite:///data/data.db")

def load_entire_tables(): 
    print(engine.table_names())
    hpd_calls = pd.read_sql("SELECT * from hpd311calls", engine)
    print(hpd_calls.head())

    query = "SELECT * FROM weather"
    weather = pd.read_sql(query, engine)
    print(weather.head())

def selecting_columns_with_sql(): 
    query = """
        SELECT date, tmax, tmin
        FROM weather;
        """

    temperatures = pd.read_sql(query, engine)
    print(temperatures)

def selecting_rows(): 
    # Create query to get hpd311calls records about safety
    query = """
        SELECT *
        FROM hpd311calls
        WHERE complaint_type = 'SAFETY';
        """
    safety_calls = pd.read_sql(query, engine)
    call_counts = safety_calls.groupby('borough').unique_key.count()
    call_counts.plot.barh()
    plt.show()    

def filtering_on_multiple_conditions(): 
    # Create query for records with max temps <= 32 or snow >= 1
    query = """
        SELECT *
        FROM weather
        WHERE tmax <= 32 OR snow >= 1;
        """
    wintry_days = pd.read_sql(query, engine)
    print(wintry_days.describe())    

def getting_distinct_values(): 
    # Create query for unique combinations of borough and complaint_type
    query = """
        SELECT DISTINCT borough, complaint_type
        FROM hpd311calls;
        """
    issues_and_boros = pd.read_sql(query, engine)
    print(issues_and_boros)

def couting_in_groups(): 
    query = """
        SELECT complaint_type, COUNT(*)
        FROM hpd311calls
        GROUP BY complaint_type;
        """

    calls_by_issue = pd.read_sql(query, engine)
    calls_by_issue.plot.barh(x="complaint_type")
    plt.show()

def working_with_aggregate_functions(): 
    query = """
        SELECT month, MAX(tmax), MIN(tmin), SUM(prcp)
        FROM weather 
        GROUP BY month;
        """

    weather_by_month = pd.read_sql(query, engine)
    print(weather_by_month)

def joining_tables(): 
    query = """
        SELECT * 
        FROM hpd311calls
        JOIN weather 
        ON hpd311calls.created_date = weather.date;
        """
    calls_with_weather = pd.read_sql(query, engine)
    print(calls_with_weather.head())

def joining_tables_and_filtering(): 
    query = """
        SELECT hpd311calls.*, weather.prcp
        FROM hpd311calls
        JOIN weather
            ON hpd311calls.created_date = weather.date
        WHERE hpd311calls.complaint_type = 'WATER LEAK';"""
    leak_calls = pd.read_sql(query, engine)
    print(leak_calls.head())
    print(leak_calls.info())

def joinging_filtering_aggregating(): 
    # Query to get heat/hot water call counts by created_date
    query = """
        SELECT hpd311calls.created_date, 
            COUNT(*)
        FROM hpd311calls 
        WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER' 
        GROUP BY hpd311calls.created_date;
        """
    df = pd.read_sql(query, engine)
    print(df.head())

    query = """
    SELECT hpd311calls.created_date, 
        COUNT(*), 
        weather.tmax,
        weather.tmin
    FROM hpd311calls 
        JOIN weather
        on hpd311calls.created_date = weather.date
    WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER' 
    GROUP BY hpd311calls.created_date;
    """
    df = pd.read_sql(query, engine)
    print(df.head())

#load_entire_tables()
#selecting_columns_with_sql()
#selecting_rows()
#filtering_on_multiple_conditions()
#getting_distinct_values()
#couting_in_groups()
#working_with_aggregate_functions()
#joining_tables()
#joining_tables_and_filtering()
joinging_filtering_aggregating()
