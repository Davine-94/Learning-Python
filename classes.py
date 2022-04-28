class Movie():
    def __init__(self,title,year,imdb_Score,have_seen):
        self.title = title
        self.year = year
        self.imdb_Score = imdb_Score
        self.have_seen = have_seen
    def nice_print(self):
        print("Title:", self.title)
        print("Year of Production:", self.year)
        print("IMDB Score:", self.imdb_Score)
        print("I have seen it:", self.have_seen)

film_1 = Movie("Fault in our stars", 2014, 9, True)
film_2 = Movie("Me before you", 2016, 9.2, True)

film_1.nice_print()

# print(film_1.year, film_2.title)
        
        
#classes are blueprints
# objects are the actual things you built
# variables = attributes
# functions = methods

        