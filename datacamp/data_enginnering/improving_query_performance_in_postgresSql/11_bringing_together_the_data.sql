-- Athlete count by country and region
SELECT reg.region
  , reg.country
  , COUNT(DISTINCT ath.athlete_id) AS no_athletes -- Athletes can compete in multiple events
FROM athletes ath
INNER JOIN oregions reg
  ON reg.olympic_cc = ath.country_code
GROUP BY reg.region, reg.country
ORDER BY no_athletes;


-- use regions and athletes and a LEFT JOIN to keep all the regions 
SELECT reg.region, reg.country
  , COUNT(DISTINCT ath.athlete_id) AS no_athletes
FROM regions reg
LEFT JOIN athletes ath
  ON reg.olympic_cc = ath.country_code
GROUP BY reg.region, reg.country
ORDER BY no_athletes DESC;

-- use RIGHT JOIN to keep all the regions 
SELECT reg.region, reg.country
  , COUNT(DISTINCT ath.athlete_id) AS no_athletes
FROM athletes ath
RIGHT JOIN regions reg
  ON ath.country_code = reg.olympic_cc
GROUP BY reg.region, reg.country
ORDER BY no_athletes DESC;


-- user INNER JOIN to find ONLY the countries with competing athletes
SELECT reg.region, reg.country
  , COUNT(DISTINCT ath.athlete_id) AS no_athletes
FROM athletes ath
INNER JOIN regions reg
  ON ath.country_code = reg.olympic_cc
GROUP BY reg.region, reg.country
ORDER BY no_athletes DESC;


