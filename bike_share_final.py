import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june','july','augest','september','october','november','december','all']

DAYS = ['monday','tuesday','thursday','wednesday','friday','saturday','sunday','all']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('\nWould you like to see data for Chicago, New York City, or Washington?\n')
    citys = ['chicago','new york city','washington']
    city = input().lower()
    while city not in citys:
        print('\nThis is not a valid city! Please try again!\n')
        city = input().lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    print("\nWhich month? 'January','February','March','April','May','June' or 'all'")

    month = input().lower()
    if month != 'all':
        while month not in MONTHS:
            print('\nThis is not a valid month name! Pleas input again!\n')
            month = input().lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print("\nWhich day? 'Monday','Tuesday','Thursday','Wednesday','Friday','Saturday','Sunday' or 'all'")

    day = input().lower()
    if day != 'all':
        while day.lower() not in DAYS:
            print('\nThis is not a valid day name! Pleas input again!\n')
            day = input().lower()
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

   # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','augest','september','october','november','december']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == DAYS.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]


    print('The most popular month: ',popular_month)
    print('The most popular day: ',popular_day)
    print('The most popular hour: ',popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    start_time = time.time()
    print('\nCalculating The Most Popular Stations and Trip...\n')


    # TO DO: display most commonly used start station
    popular_start_station = df["Start Station"].mode()[0]

    # TO DO: display most commonly used end station
    popular_end_station = df["End Station"].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + df['End Station']
    popular_trip = df['trip'].mode()[0]

    print("Most Popular Start Station : ",popular_start_station)
    print("Most Popular End Station : ",popular_end_station)
    print("Most Popular Trip : ",popular_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()

    print('Total Duration: ',total_travel_time)

    print('Avg Duration:' ,mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nCounts of user types:\n')
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if "Gender" in  df.keys():
        user_gender = df["Gender"].value_counts()
        print(user_gender)
    else:
        print("There is no Gender data!")

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.keys():
        earliest_year = df['Birth Year'].min()
        lasted_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]


        print('the earliest year of birth: ', earliest_year)
        print('the recent year of birth: ' ,lasted_year)
        print('the most common year of birth: ', most_common_year)
    else:
        print("There is no Birth Year data!")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

#Chicago, January, all
#Chicago, February, Monday
#New York City, March, Tuesday
#New York City, April, Wednesday
#Washington, May, Saturday
#Washington, June, Friday
