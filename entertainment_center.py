import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", 
						"A story of a boy and toy", 
						"https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Toy_Story_logo.svg/300px-Toy_Story_logo.svg.png", 
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.Movie("Avatar", 
					 "A marine on an alien planet",
					 "data:image/jpeg;base64,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",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)
#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock", 
							 "Using rock music to learn", 
							 "http://ia.media-imdb.com/images/M/MV5BMjEwOTMzNjYzMl5BMl5BanBnXkFtZTcwNjczMTQyMQ@@._V1_SX640_SY720_.jpg", 
							 "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

special_forces = media.Movie("Special Forces", 
							 "Saving Hostage", 
							 "http://ia.media-imdb.com/images/M/MV5BMTY4NTA5NjA1Ml5BMl5BanBnXkFtZTcwMDM3NDA1OA@@._V1_SX214_AL_.jpg", 
							 "https://www.youtube.com/watch?v=uIx00INSlyQ")

the_beauty_inside = media.Movie("The Beauty Inside", 
								"Romance", 
								"http://www.soompi.com/wp-content/uploads/2015/07/TheBeautyInside.jpg", 
								"https://www.youtube.com/watch?v=3XcK4Elpn0s")

the_throne = media.Movie("The Throne", 
						 "Korean histoy: King", 
						 "http://asianwiki.com/images/3/38/The_Throne-tp.jpg", 
						 "https://www.youtube.com/watch?v=c_DPNR2301o")

movies = [toy_story, avatar, school_of_rock, special_forces, the_beauty_inside, the_throne]
fresh_tomatoes.open_movies_page(movies)