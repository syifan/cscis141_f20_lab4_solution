from datetime import date
from copy import deepcopy

def weekday(month, day, year):
    '''
    Given a date as month (string), day (int), and year (int), return the weekday.
    '''
    pass

def is_leap_year(year):
    '''
    Return True if year is a leap year; False otherwise.
    '''
    pass

def day_of_the_year(month, day, year):
    '''
    Given a date as month (string), day (int), and year (int), return the day of the year.
    '''
    pass

#-----------------------------------------------------------
# Pytest test code: execute with "pytest change.py".

def test_is_leap_year():
    '''
    Some inadequate testing.
    '''
    assert is_leap_year(2020)
    assert not is_leap_year(1999)

def test_weekday():
    '''
    More inadequate testing.  Test against the datetime module.
    '''
    DAYS = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
    NONLEAP = {'Jan':31, 'Feb':28, 'Mar':31, 'Apr':30, 'May':31, 'Jun':30,
              'Jul':31, 'Aug':31, 'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31}
    LEAP = deepcopy(NONLEAP)
    LEAP['Feb'] = 29

    for year in [1900, 1999]:
        if is_leap_year(year):
            months = LEAP
        else:
            months = NONLEAP
        m = 1  # The datetime module expects the month as a number.
        for month in months:
            for day in range(1, 28):
                assert weekday(month, day, year) == DAYS[date(year, m, day).weekday()]
            m += 1

def test_day_of_year():
    '''
    More inadequate testing.  Test against the datetime module.
    '''
    DAYS = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
    NONLEAP = {'Jan':31, 'Feb':28, 'Mar':31, 'Apr':30, 'May':31, 'Jun':30,
              'Jul':31, 'Aug':31, 'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31}
    LEAP = deepcopy(NONLEAP)
    LEAP['Feb'] = 29

    for year in [1900, 1999]:
        if is_leap_year(year):
            months = LEAP
        else:
            months = NONLEAP
        m = 1
        for month in months:
            for day in range(1, 28):
                assert day_of_year(month, day, year) == date(year, m, day).toordinal() - date(year, 1, 1).toordinal() + 1
            m += 1

#---------------------------------------------------------------------------
# Purely python (not pytest) test code: execute with "python change.py".

# The following if statement insures the code does not execute when imported into other test code.
if (__name__ == '__main__'):
    DAYS = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
    NONLEAP = {'Jan':31, 'Feb':28, 'Mar':31, 'Apr':30, 'May':31, 'Jun':30,
              'Jul':31, 'Aug':31, 'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31}
    LEAP = deepcopy(NONLEAP)
    LEAP['Feb'] = 29

    for year in [1900, 1999]:
        if is_leap_year(year):
            months = LEAP
        else:
            months = NONLEAP
        m = 1
        for month in months:
            for day in range(1, 28):
                assert weekday(month, day, year) == DAYS[date(year, m, day).weekday()]
            m += 1

    for year in [1900, 1999]:
        if is_leap_year(year):
            months = LEAP
        else:
            months = NONLEAP
        m = 1
        for month in months:
            for day in range(1, 28):
                assert day_of_year(month, day, year) == date(year, m, day).toordinal() - date(year, 1, 1).toordinal() + 1
            m += 1
