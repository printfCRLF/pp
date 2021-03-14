-- creating and querying a view 
-- Create a view for reviews with a score above 9
CREATE VIEW high_scores AS
SELECT * FROM REVIEWS
WHERE score > 9;

-- Count the number of self-released works in high_scores
SELECT COUNT(*) FROM high_scores
INNER JOIN labels ON high_scores.reviewid = labels.reviewid
WHERE label = 'self-released';

-- creating a view from other views
-- Create a view with the top artists in 2017
CREATE VIEW top_artists_2017 AS
-- with only one column holding the artist field
SELECT artist_title.artist FROM top_15_2017
INNER JOIN artist_title
ON top_15_2017.reviewid = artist_title.reviewid;

-- Output the new view
SELECT * FROM top_artists_2017;

-- Granting and revoking access
-- Revoke everyone's update and insert privileges
REVOKE UPDATE, INSERT ON long_reviews FROM PUBLIC; 

-- Grant the editor update and insert privileges 
GRANT UPDATE, INSERT ON long_reviews TO editor; 

-- redefining a view 
-- Redefine the artist_title view to have a label column
CREATE OR REPLACE VIEW artist_title AS
SELECT reviews.reviewid, reviews.title, artists.artist, labels.label
FROM reviews
INNER JOIN artists
ON artists.reviewid = reviews.reviewid
INNER JOIN labels
ON labels.reviewid = reviews.reviewid;

SELECT * FROM artist_title;

--  creating and refreshing a materialized view 
-- Create a materialized view called genre_count 
CREATE MATERIALIZED VIEW genre_count AS
SELECT genre, COUNT(*) 
FROM genres
GROUP BY genre;

INSERT INTO genres
VALUES (50000, 'classical');

-- Refresh genre_count
REFRESH MATERIALIZED VIEW genre_count;

SELECT * FROM genre_count;