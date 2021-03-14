-- Create a temp table of Canadians
CREATE TEMP TABLE canadians AS
    SELECT *
    FROM athletes_recent
    WHERE country_code = 'CAN'
    AND season = 'Winter'; -- The table has both summer and winter athletes

-- Find the most popular sport
SELECT sport
  , COUNT(DISTINCT athlete_id) as no_athletes
FROM canadians
GROUP BY sport 
ORDER BY no_athletes DESC;

-- Create temp countries table
CREATE TEMP TABLE countries AS
    SELECT DISTINCT o.region, a.country_code, o.country
    FROM athletes a
    INNER JOIN oregions o
      ON a.country_code = o.olympic_cc;
      
ANALYZE countries; -- Collect the statistics

-- Count the entries
SELECT count(*) FROM countries;