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


def compute(originalDate, dateNow):
    date1 = dateNow
    date2 = datetime.datetime(dateNow.year, originalDate.month, originalDate.day)
    deltaTime = date1 - date2
    days = int(deltaTime.total_seconds() / 60 / 60 / 24)
    return days

def printBirthday_information():
    if days < 0:
        print('Your Birthday is in {} days'.format(-days))
    elif days > 0:
        print('You had your Birthday already this year! It was {} days ago'.format(days))
    else:
        print('Happy Birthday')

def main():
    printHeader()
    bDay = getBirthday()
    now = datetime.datetime.dateNow()
    numberofDays = compute(birthday, dateNow)
    printBirthday_information()
    input('Press any key to Exit.')


main()
