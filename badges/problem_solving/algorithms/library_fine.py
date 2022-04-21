def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def days_in_month(month , year):
    if month in {1 , 3 , 5 , 7 , 8 , 10 , 12}:
        return 31
    if month == 2:
        if leap_year(year):
            return 29
        return 28
    return 30


def libraryFine(d1 , m1 , y1 , d2 , m2 , y2):
    fine = 0
    if y1 == y2:
        if m1 == m2 and d1 > d2:
            late = d1 - d2
            fine = late * 15

        elif m1 > m2:
            late = m1 - m2
            fine = late * 500
    elif y1 < y2:
        fine = 0

    else:
        fine = 10000
    return fine


if __name__ == "__main__":
    result = libraryFine(14 , 7 , 2018 , 5 , 7 , 2018)
    print(result)
