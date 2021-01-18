from itertools import groupby
from operator import itemgetter
import sys


# Iterator function that returns and separates
# each line by a given separator
def read_mapper(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)


# Import the movie titles file from distributed cache,
# and load it into a python dict so each movie year can
# be accessed by a MovieID key
def movies(file_name):

    movies_data = {}
    f = open(file_name)

    for line in f:
        mov, year, name = line.rstrip().split(',', 2)
        movies_data[mov] = year + ',' + name

    f.close()
    return movies_data


def main():

    mapper = read_mapper(sys.stdin)
    movie_names = movies('movie_titles.txt')

    for line in mapper:

        ##groupby MovieId
        for movie, group in groupby(mapper, itemgetter(0)):
            try:

                # Ratings is the accumulated total of all the ratings per movie
                # Count is the total number of ratings per movie
                # First is the date of the earliest rating
                # Last is the date of the latest rating
                ratings = 0
                count = 0
                first = 0
                last = 0

                # Iterate through each user rating in a movie grouping
                for movie, value in group:

                    # Accumulate ratings and count
                    rating, date = value.split(',', 1)
                    ratings += int(rating)
                    count += 1

                    # Check the date against first and last
                    dateInt = int(date)
                    if first == 0:
                        first = dateInt
                        last = dateInt

                    elif (first > dateInt):
                        first = dateInt

                    elif (last < dateInt):
                        last = dateInt

                year, name = movie_names[movie].split(',', 1)

                avg = float(ratings) / count

                value = '%d,%d,%s,%d,%f,%s' % (first, last, year, count, avg, name)

                print('%s\t%s' % (movie, value))

            except ValueError:
                pass


if __name__ == "__main__":
    main()