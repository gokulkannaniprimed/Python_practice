def leap_year(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        print(str(year) + ' leap year')
    else:
        print(str(year)+ ' not a leap year')
leap_year(2004)
leap_year(2000)
leap_year(100)