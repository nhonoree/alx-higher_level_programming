-- Title: Rotten tomatoes
-- Script to list all shows by their rating from `hbtn_0d_tvshows_rate`
-- Each record displays: tv_shows.title - rating sum
-- Results are sorted in descending order by the rating

SELECT tv_shows.title, SUM(rating) AS rating 
FROM tv_shows 
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.tv_show_id 
GROUP BY tv_shows.title 
ORDER BY rating DESC;
