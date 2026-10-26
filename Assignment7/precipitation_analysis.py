
import os

MIN_PRECIPITATION = 0.0
MAX_PRECIPITATION = 366.0
OUTPUT_FILE = 'precipitation.txt'


def main():

    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    precipitation = [0.0] * 12

    for i in range(len(months)):
        precipitation[i] = get_precipitation(months[i])

    analyze_precipitation(precipitation, months)

    path = write_precipitation_file(months, precipitation)
    if path is not None:
        print(f'Data saved to {path}')


def get_precipitation(month):
    while True:
        try:
            rainfall = float(input(f'Enter the rainfall for {month}: '))

            if MIN_PRECIPITATION <= rainfall <= MAX_PRECIPITATION:
                return rainfall
            else:
                print(f'Invalid input. Please enter a value between '
                      f'{MIN_PRECIPITATION} and {MAX_PRECIPITATION}.')

        except ValueError:
            print('Invalid input. Please enter a number.')


def analyze_precipitation(precipitation, months):
    total = sum(precipitation)
    average = total / len(precipitation)

    highest = max(precipitation)
    lowest = min(precipitation)

    highest_index = precipitation.index(highest)
    lowest_index = precipitation.index(lowest)

    print(f'Total rainfall: {total:.2f}')
    print(f'Average rainfall: {average:.2f}')
    print(f'Highest rainfall: {months[highest_index]}'
          f' {highest:.1f}')
    print(f'Lowest rainfall: {months[lowest_index]}'
          f' {lowest:.1f}')


def write_precipitation_file(months, precipitation, filename=OUTPUT_FILE):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    try:
        with open(path, 'w') as output_file:
            for i in range(len(months)):
                output_file.write(f'{months[i]},{precipitation[i]}\n')

    except OSError as error:
        print(f"Could not save the data to '{path}': {error}")
        return None

    return path


if __name__ == '__main__':
    main()
