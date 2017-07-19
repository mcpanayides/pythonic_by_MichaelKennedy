import datetime

def printHeader():
    print('=============================================')
    print('               Birthday App')
    print('=============================================')
    print()


def getBirthday():
    year = int(input('What year where you born in? '))
    month = int(input('What month where you born in? '))
    day = int(input('What day where you born in? '))
    birthday = datetime.datetime(year, month, day)
    return birthday


def compute(original_date, now):
    date1 = now
    date2 = datetime.datetime(now.year, original_date.month, original_date.day)
    deltaTime = date1 - date2
    days = int(deltaTime.total_seconds() / 60 / 60 / 24)
    return days

def printBirthday_information(days):
    if days < 0:
        print('Your Birthday is in {} days'.format(-days))
    elif days > 0:
        print('You had your Birthday already this year! It was {} days ago'.format(days))
    else:
        print('Happy Birthday')

def main():
    printHeader()
    bDay = getBirthday()
    now = datetime.datetime.now()
    numberofDays = compute(bDay, now)
    printBirthday_information(numberofDays)
    input('Press any key to Exit.')


main()
