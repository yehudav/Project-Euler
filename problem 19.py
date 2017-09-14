

monthes = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]

current_year = 1900

sundays = 0

first_of_month = 1          # 0 = sunday.... 6 = saturday

while current_year < 2001:
    if current_year % 4 == 0 and current_year != 1900:
        monthes[1] = 1
    else:
        monthes[1] = 0

    for m in monthes:
        first_of_month = (first_of_month + m ) % 7

        if not first_of_month:
            sundays += 1

    current_year += 1

print(sundays - 2)



