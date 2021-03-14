SELECT reg.region, COUNT(DISTINCT dem.olympic_cc)
FROM regions reg -- Olympics region data
LEFT JOIN demographics dem -- World Bank population data
  ON dem.olympic_cc = reg.olympic_cc
GROUP BY reg.region;

-- count and count distinct 
SELECT country_code
  , COUNT(DISTINCT athlete_id) as medals_count
FROM athletes_recent
WHERE medal IS NOT NULL
AND year = 2016
GROUP BY country_code
ORDER BY medals_count DESC;

-- OR versus IN with athletes
SELECT *
FROM athletes_wint 
WHERE age in (11,12);

-- where to place a region filter 
SELECT dem.olympic_cc, reg.country, dem.gdp, dem.population
FROM demographics dem
LEFT JOIN oregions reg
  ON dem.olympic_cc = reg.olympic_cc
  AND reg.region = 'Africa'
WHERE dem.year = 2014
AND dem.gdp IS NOT NULL
ORDER BY dem.gdp DESC; 
-- 189 

SELECT dem.olympic_cc, reg.country, dem.gdp, dem.population
FROM demographics dem
LEFT JOIN oregions reg
  ON dem.olympic_cc = reg.olympic_cc
WHERE dem.year = 2014
AND reg.region = 'Africa'
AND dem.gdp IS NOT NULL
ORDER BY dem.gdp DESC;
-- 51


SELECT dem.olympic_cc, reg.country, dem.gdp, dem.population
FROM demographics dem
INNER JOIN oregions reg
  ON dem.olympic_cc = reg.olympic_cc
  AND reg.region = 'Africa'
WHERE dem.year = 2014
AND dem.gdp IS NOT NULL
ORDER BY dem.gdp DESC;
-- 51

-- filtering in join, where and select 
SELECT DISTINCT ath.name, dem.country, dem.gdp
FROM athletes_wint ath
INNER JOIN odemographics dem
  ON ath.country_code = dem.olympic_cc 
WHERE ath.year = 2014
ORDER BY dem.gdp DESC;

-- number of cometing athletes 
-- Number of competing athletes
WITH athletes as (
  SELECT country_code, year, COUNT(athlete_id) AS no_athletes
  FROM athletes
  GROUP BY country_code, year
)

SELECT demos.country, ath.year, ath.no_athletes
    , demos.gdp_rank
    , demos.population_rank
FROM athletes ath
INNER JOIN demographics_rank demos  
  ON ath.country_code = demos.olympic_cc -- Country
  AND ath.year = demos.year -- Year
ORDER BY ath.no_athletes DESC;

-- South Africa Trends 
-- South African athletes by year
WITH athletes_cte as 
(
    SELECT year
      , season
      , COUNT(DISTINCT athlete_id) AS no_athletes
    FROM athletes
    WHERE country_code = 'RSA' -- South Africa filter
    GROUP BY year, season
)

SELECT ath.year
  , ath.season
  , ath.no_athletes
  , demos.gdp_rounded
  , demos.gdp_rank
  , demos.population_rounded
  , demos.population_rank
FROM athletes_cte ath
INNER JOIN demographics_rank demos
  ON ath.year = demos.year
  AND demos.olympic_cc = 'RSA' -- Filter to South Africa
ORDER BY ath.season, ath.year;

