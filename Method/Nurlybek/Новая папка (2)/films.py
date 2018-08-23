from movie import*
import generator

#здесь создаем объекты класса Movie
m2=Movie("Deadpool","2016","Comedy","https://st.kp.yandex.net/images/film_big/462360.jpg", "https://www.youtube.com/watch?v=Xithigfg7dA")
m3=Movie("Ghostbusters",'2016',"Comedy","https://upload.wikimedia.org/wikipedia/en/d/d0/Ghostbusters_2016_film_poster.jpg","https://www.youtube.com/watch?v=w3ugHP-yZXw")
generator.open_movies_page([m2,m3])
