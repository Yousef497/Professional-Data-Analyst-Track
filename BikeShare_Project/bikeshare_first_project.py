import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please Choose a city from (Chicago, New York City or Washington): ').title()
    while city.title() not in CITY_DATA.keys():
        print('\nPlease enter a valid choice.\n')
        city = input('Please Choose a city from (Chicago, New York City or Washington): ').title()

    print()

    # get user input for month (all, january, february, ... , june)
    month = input('Please choose a month from (January to June) and if you choose not to filter by month enter (all): ').title()
    while month.title() not in ['All', 'January', 'February', 'March', 'April', 'May', 'June']:
        print('\nPlease enter a valid choice.\n')
        month = input('Please choose a month from (January to June) and if you choose not to filter by month enter (all): ').title()

    print()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please choose a day to filter and if you choose not to filter by day enter (all): ').title()
    while day.title() not in ['All', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        print('\nPlease enter a valid choice.\n')
        day = input('Please choose a day to filter and if you choose not to filter by day enter (all): ').title()

    print()

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
    #Open CSV File acording to user choice
    df = pd.read_csv(CITY_DATA[city])

    #Convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month and day to filter data
    df['Month'] = df['Start Time'].dt.month_name()
    df['Week Day'] = df['Start Time'].dt.day_name()
    df['Start Hour'] = df['Start Time'].dt.hour

    #Apply filters
    #Month filtering
    if month != 'All':
        df = df[df['Month'] == month]

    #Day Filtering
    if day != 'All':
        df = df[df['Week Day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['Month'].mode()[0]
    print('Most Common Month: {}'.format(common_month))

    # display the most common day of week
    common_day = df['Week Day'].mode()[0]
    print('Most Common Day of Week: {}'.format(common_day))

    # display the most common start hour
    common_hour = df['Start Hour'].mode()[0]
    print('Most Common Start Hour: {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most Common Start Station: {}'.format(common_start))

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most Common End Station: {}'.format(common_end))

    # display most frequent combination of start station and end station trip
    route = df.groupby(['Start Station', 'End Station'])
    common_route = route.size().sort_values(ascending = False).head(1)
    print('Most Common Route:\n')
    print(common_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total Travel Time: {:.2f}'.format(total_time))

    # display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('Average Travel Time: {:.2f}'.format(avg_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    users_type = df['User Type'].value_counts()
    print('User Types:')
    print(users_type)
    print()

    # Display counts of gender
    if 'Gender' in df.columns:
        users_gender = df['Gender'].value_counts()
        print('Users Gender:')
        print(users_gender)
        print()
    else:
        print('Sorry Washington data does not include Customers Gender Data.')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Birth Year stats:')
        #Earliest
        early = df['Birth Year'].min()
        print('Earliest Birth year: {}'.format(int(early)))

        #Recent
        recent = df['Birth Year'].max()
        print('Most Recent Birth Year: {}'.format(int(recent)))

        #Most Common Year
        common_year = df['Birth Year'].mode()[0]
        print('Most Common Birth Year: {}'.format(int(common_year)))

    else:
        print('Sorry Washington data does not include Customers Birth Data.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:(start_loc + 5)])
        start_loc += 5
        view_data = input("\nDo you wish to continue?: ").lower()



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
