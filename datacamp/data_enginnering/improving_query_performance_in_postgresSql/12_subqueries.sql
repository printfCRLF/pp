-- filtering to freezing with a subquery 
-- Countries cold enough for snow year-round
SELECT country_code
  , country
  , COUNT (DISTINCT athlete_id) AS winter_athletes -- Athletes can compete in multiple events 
FROM athletes
WHERE country_code IN (SELECT olympic_cc FROM oclimate  WHERE temp_annual < 0)
AND season = 'Winter'
GROUP BY country_code, country;



-- where winter is white 
WITH south_cte AS -- CTE
(
  SELECT region
    , ROUND(AVG(temp_06),2) AS avg_winter_temp
    , ROUND(AVG(precip_06),2) AS avg_winter_precip
  FROM oclimate
  WHERE region IN ('Africa','South America','Australia and Oceania')
  GROUP BY region
)

SELECT south.region, south.avg_winter_temp, south.avg_winter_precip
  , COUNT(DISTINCT ath.athlete_id)
FROM south_cte as south
INNER JOIN athletes_recent ath
  ON south.region = ath.region
  AND ath.season = 'Winter'
GROUP BY south.region, south.avg_winter_temp, south.avg_winter_precip
ORDER BY south.avg_winter_temp;


-- Climate by country with Olympian athletes 
SELECT country
  , temp_06
  , precip_06
FROM climate
WHERE region = 'Africa'
AND olympic_cc IN (SELECT country_code FROM athletes_wint)
ORDER BY temp_06;

-- 
WITH countries_cte AS -- CTE
(
    SELECT olympic_cc
      , country
      , temp_06
      , precip_06
    FROM climate
    WHERE region = 'Africa'
)

SELECT DISTINCT cte.country
  , cte.temp_06
  , cte.precip_06
FROM athletes_wint AS wint
INNER JOIN countries_cte AS cte
  ON wint.country_code = cte.olympic_cc
ORDER BY temp_06;
