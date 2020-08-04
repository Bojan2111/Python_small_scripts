# Jean Meeus's Julian algorithm of calculating Orthodox Easter date based on Julian Calendar
# Gregorian Easter date Calculator
# Math formula by anonymous author
# Enter the year and see results!
# Likes, shares and comments are welcome! 

year = int(input("Enter year: "))
a = year % 4
b = year % 7
c = year % 19    
d = (19 * c + 15) % 30
e = (2 * a + 4 * b - d + 34) % 7    
month = (d + e + 114) // 31
day = ((d + e + 114) % 31) + 1
dayGreg = day + 13
monthGreg = month

if month == 3 and dayGreg > 31:
    monthGreg += 1
    dayGreg -= 31
elif month == 4 and dayGreg > 30:
    monthGreg += 1
    dayGreg -= 30
else:
    monthGreg = month
    dayGreg = dayGreg 

monthName = ""
if month == 3:
    monthName = "March"
elif month == 4:
    monthName = "April"
    
if monthGreg == 3:
    monthNameGreg = "March"
elif monthGreg == 4:
    monthNameGreg = "April"
else:
    monthNameGreg = "May"
resultEast = monthNameGreg + " " + str(dayGreg) + " " + str(year)
resultEastJul =  monthName + " " + str(day) + " " + str(year)

print("\nEastern Christians celebrate Easter on:\n" + resultEast + " in Gregorian Calendar or on:\n" + resultEastJul + " in Julian Calendar.")

ga = year % 19    
gb = year // 100    
gc = year % 100
gd = gb // 4    
ge = gb % 4
gf = (gb + 8) // 25
gg = (gb - gf + 1) // 3    
gh = (19 * ga + gb - gd - gg + 15) % 30
gi = gc // 4
gk = gc % 4
gl = (32 + 2 * ge + 2 * gi - gh - gk) % 7
gm = (ga + 11 * gh + 22 * gl) // 451    
gmonth = (gh + gl - 7 * gm + 114) // 31
gday = ((gh + gl - 7 * gm + 114) % 31) + 1    
gmonthName = ""
if gmonth == 3:
    gmonthName = "March"
else:
    gmonthName = "April"
easter = gmonthName + " " + str(gday) + " " + str(year)
print("\nWestern Christians celebrate Easter on:\n" + easter)

print("Press Enter to continue...")
input()