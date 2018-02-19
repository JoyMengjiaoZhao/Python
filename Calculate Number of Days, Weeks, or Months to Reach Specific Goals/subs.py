import datetime
import math

goal_subs=100000
current_subs=85000
subs_to_go=goal_subs-current_subs

avg_subs_day=200
days_to_go=math.ceil(subs_to_go/avg_subs_day)
#Return the ceiling of x, the smallest integer greater
# than or equal to x. If x is not a float,
# delegates to x.__ceil__(), which should return an Integral value.
print(days_to_go)
today=datetime.date.today()

print(today+datetime.timedelta(days=days_to_go))

