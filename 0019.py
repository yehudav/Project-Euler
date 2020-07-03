def current_february_days(year):# todo refactor
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return 1
    return 0


def sundays_on_first(starting_year, jan_1, ending_year):
    months = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
    current_year = starting_year
    first_day_of_month = jan_1
    sundays = 0

    while current_year <= ending_year:
        months[1] = current_february_days(current_year)

        for m in months:
            first_day_of_month = (first_day_of_month + m) % 7

            if first_day_of_month == 0:
                sundays += 1

        current_year += 1

    return sundays


print(sundays_on_first(1900, 1, 2000) - sundays_on_first(1900, 1, 1900))
