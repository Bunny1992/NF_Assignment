import sys

def read_input(file):
    for line in file:
        yield line.rstrip()


def main():

    input = read_input(sys.stdin)
    for line in input:

        # Split the line by comma
        lineSplit = line.split(',')

        if len(lineSplit) == 3:

            movie = lineSplit[0]
            rating = lineSplit[2]
            date = lineSplit[3].replace('-', '')
            value = rating + '::' + date

            print(movie + "\t" + value)

if __name__ == "__main__":
    main()