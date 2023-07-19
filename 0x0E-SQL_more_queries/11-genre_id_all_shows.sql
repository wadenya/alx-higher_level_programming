-- script that lists all shows contained in the database hbtn_0d_tvshows.
--  record should display: tv_shows.title - tv_show_genres.genre_id
SELECT t.`title`, sg.`genre_id`
	FROM `tv_shows` AS t
	LEFT JOIN `tv_show_genres` AS sg
	ON t.`id` = sg.`show_id`
	ORDER BY t.`title`, sg.`genre_id`;
