"""Module supplying classes for manipulating dates and times"""
from datetime import datetime
from collections import defaultdict

def get_birthdays_per_week(users):
    """Function prints a list of colleagues' birthdays for the following 7 days"""
    today = datetime.today().date()
    list_of_birthday_colleagues = defaultdict(list)
    for user in users:
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year+1)
        else:
            birthday_this_year = birthday.replace(year=today.year)
        user["birthday"] = birthday_this_year
    sorted_list = sorted(users, key = lambda user: user["birthday"])
    for user in sorted_list:
        name = user["name"]
        next_birthday = user["birthday"]
        delta_days = (next_birthday - today).days
        str_next_birthday = str(next_birthday)
        if delta_days < 7:
            formatted = datetime.strptime(str_next_birthday, '%Y-%m-%d')
            day_of_the_week = datetime.strftime(formatted, "%A")
            if day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
                list_of_birthday_colleagues['Monday'].append(name)
            else:
                list_of_birthday_colleagues[day_of_the_week].append(name)
    for day, names in list_of_birthday_colleagues.items():
        print(f"{day}: {', '.join(names)}")
