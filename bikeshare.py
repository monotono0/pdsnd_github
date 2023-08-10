import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let\'s explore some US bikeshare data!")

    # User has to choose a city to filter by.
    # Loop until user enters a valid city abbreviation.
    while True:
        # Prompt user for city abbreviation and exit loop if it is a valid one.
        city = input('Please enter a city (Chicago, New York City or Washington): ').lower()
        if city in CITY_DATA:
            break
        # If the entered value is not valid, print an error message and continue loop.
        print('Invalid entry. Please type in the name of the given cities.')

    # User has to choose a month to filter by or all for no filter.
    # Define list of month
    month_list = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
    # Loop until user enters a valid month.
    while True:
        try:
            # Prompt user for month input and convert it to an integer.
            month = input('Choose the month, you want information about or choose "all": ').lower()
            # Check if input is in the valid range and exit loop if it is valid.
            if month in month_list:
                if month != 'all':
                    month = month_list.index(month)
                else: 
                    month = 0
                break
            else:
                # If the entered value is not in valid range, print an error message and continue loop.
                print('Invalid entry. Please type in january, february, march, april, may, june or all.')
        except ValueError:
            # If the entered value is not valid, print an error message and continue loop.
            print('Invalid value.')
            

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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


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

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
