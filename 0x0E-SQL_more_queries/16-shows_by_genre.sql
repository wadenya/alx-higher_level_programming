-- lists all shows, and all genres linked to that show, 
-- from the database hbtn_0d_tvshows
SELECT t.`title`, gn.`name`
FROM `tv_shows` AS t
LEFT JOIN `tv_show_genres` AS s
ON t.`id` = s.`show_id`
LEFT JOIN `tv_genres` AS gn
ON s.`genre_id` = gn.`id`
ORDER BY t.`title`, gn.`name`;
