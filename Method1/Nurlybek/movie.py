import webbrowser
class Movie:
    #создайте фун init с атрибутами title, year ,genre, poster_url, trailer_url
    def __init__(self, title, year, genre, poster_url,trailer_url):
        self.title=title
        self.year=year
        self.genre=genre
        self.poster_url=poster_url
        self.trailer_url=trailer_url
    def print_movie(self):
        print(self.title, self.year, self.genre)

    def print_trailer(self):
        webbrowser.open(self.trailer_url)
