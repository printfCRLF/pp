from sqlalchemy import create_engine
import pandas as pd

def create_a_database_engine(): 
    engine = create_engine('sqlite:///data/Chinook.sqlite')
    table_names = engine.table_names()
    print(table_names)

    con = engine.connect()
    rs = con.execute('select * from Album')
    df = pd.DataFrame(rs.fetchall())   
    print(df.head())

    rs = con.execute('SELECT LastName, Title FROM Employee')
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()
    print(len(df))
    print(df.head())
    con.close()

def filtering_and_querying(): 
    engine = create_engine('sqlite:///data/Chinook.sqlite')
    table_names = engine.table_names()
    print(table_names)

    with engine.connect() as con: 
        rs = con.execute('SELECT * From Employee WHERE EmployeeId >= 6')
        df = pd.DataFrame(rs.fetchall())
        df.columns = rs.keys()

    print(df.head())

def querying_with_pandas():
    engine = create_engine("sqlite:///data/Chinook.sqlite")
    df = pd.read_sql_query("SELECT * from Employee WHERE EmployeeId >= 6 ORDER BY BirthDate", engine)
    print(df.head())

def complex_query_inner_join(): 
    engine = create_engine("sqlite:///data/Chinook.sqlite")
    df1 = pd.read_sql_query("SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID", engine)
    print(df1.head())
    df2= pd.read_sql_query("SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000", engine)
    print(df2.head())

#create_a_database_engine()
#filtering_and_querying()
#querying_with_pandas()
complex_query_inner_join()