"""
Python
23628번 악마의 연차계산기
Implementation
"""
date1 = list(map(int, input().split()))
date2 = list(map(int, input().split()))

year = date2[0] - date1[0]
month = (year * 12) + date2[1] - date1[1]
date = month * 30 + (date2[2] - date1[2])
year = date // 360

month_vacation = min(36, date // 30)
year_vacation = year * 15

if year % 2 == 0:
    n = (year - 1) // 2
    year_vacation += (n * (n + 1))
else:
    n = (year - 1) // 2
    year_vacation += (n * (n + 1)) - n

print(year_vacation, month_vacation)
print(f"{date:d}days")
