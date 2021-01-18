from itertools import groupby
from operator import itemgetter
import sys
import pandas as pd


# Iterator function that returns and separates
# each line by a given separator
def read_mapper(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main():

    mapper = read_mapper(sys.stdin)
    colnames = ["movie_id", "Year", "movie_name"]
    movie_data = pd.read_csv("movie_titles.csv", encoding='latin-1', names=colnames, header=None)
    movie_data["mov"] = movie_data['Year'].astype(str) + "," + movie_data['movie_name']

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
                    rating, date = value.split('::', 1)
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

                year, name = movie_data["mov"].split(',', 1)

                avg = float(ratings) / count

                value = '%d,%d,%s,%d,%f,%s' % (first, last, year, count, avg, name)

                print('%s\t%s' % (movie, value))

            except ValueError:
                pass


if __name__ == "__main__":
    main()
