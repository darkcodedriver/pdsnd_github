""" Python Code to analyze Bikeshare Data of thre different major cities in the US depending on multiple user inputs"""


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['January', 'February', 'March', 'April', 'May', 'June']
Weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
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
    #Handling Value Errors of user input
    while True:
        try:
            city = str(input('Please choose a city: Chicago, New York City, Washington: ')).lower()

        except ValueError:
            continue
        if city in CITY_DATA:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input('Please choose a Month: All, January, February, ... , June ')).title()
        except ValueError:
            continue
        if month in months:
            break
        elif month == 'All':
            break
    print(month)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day =  str(input('Please choose a day of the week: All, Monday, Tuesday,..: ')).title()
        except ValueError:
            continue
        if day.title() in Weekdays:
            break
        elif day == 'All':
            break
    print(day)

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'All':
        month=months.index(month)+1
        print(month)
        df=df[df['month']==month]

    if day != 'All':
        df = df[df['day_of_week']==day]

   # print(df)
    return df


def time_stats(df,city,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_most = df['month'].mode()[0]
    month_most_name = months[df['month'].mode()[0]-1]
    if month == 'All':
        print('The most common month of bikeshare usage in {} is: {}'.format(city.title(),month_most_name))
    # TO DO: display the most common day of week
    if day == 'All':
        day_most = df['day_of_week'].mode()[0]
        print('Most common day of bike share usage in {} during month <{}> is: {}.'.format(city,month,day_most))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour #convert start time to hour and create new column hour
    hour_most = df['hour'].mode()[0]
    print('The most common start hour of bike share usage in {} during month <{}> on day <{}> is: {}.'.format(city,month,day,hour_most))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df,city,month,day):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_most = df['Start Station'].mode()[0]
    print('The most common start station is: {}.'.format(start_station_most))
    # TO DO: display most commonly used end station
    end_station_most = df['End Station'].mode()[0]
    print('The most common end station is: {}.'.format(end_station_most))

    # TO DO: display most frequent combination of start station and end station trip
    #station_combo_most = df.groupby(['Start Station'])['Start Station','End Station'].mode()[0]
    df['start end']=df['Start Station'].map(str)+'  -->  '+df['End Station'].map(str)
    popular = df['start end'].mode()[0]
    print('The most popular combination of stations in {} during month <{}> on day <{}> is: {}'.format(city,month,day,popular))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: ',total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is: ',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    df = df.dropna(axis = 0)
#    df.to_csv('test2')
    if city != 'washington':
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        print('Earliest Year of Birth: ',int(df['Birth Year'].min()))
        print('Most recent Year of Birth: ',int(df['Birth Year'].max()))
        print('Most common Year of Birth: ',int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_raw(df):
    """ function showing raw data to user if requested"""
    valid=['Yes','yes','y','ye','YE','Ye','YES'] # valid input for yes
    invalid=['No','NO','no','n']# valid input for no
    start=0
    end=5
    continue_count=0

    while True:
        try:

            if start>0:
                decision = str(input('Do you want to see 5 more rows of the raw data? Type [Yes] or [No]: '))
            else:
                decision = str(input('Do you want to see the raw data? Type [Yes] or [No]: '))
        except ValueError:
            continue
        if decision in valid:

            if end>df.shape[0]:
                print(df.iloc[start:end,:])
                break
            else:
                print(df.iloc[start:end,:])
                start,end = start+5,end+5
                continue
        elif decision in invalid:
            break
        else:
            continue_count+=1
            if continue_count==5:
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,city,month,day)
        station_stats(df,city,month,day)
        trip_duration_stats(df)
        user_stats(df,city)
        show_raw(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    #city, month, day = get_filters()
    #df=load_data(city, month, day)
    #time_stats(df)
    #station_stats(df)
    #trip_duration_stats(df)
    #user_stats(df)
