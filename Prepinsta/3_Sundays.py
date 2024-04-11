'''
Jack is always excited about sunday. It is favourite day, when he gets to play all day. And goes to cycling with his friends. 

So every time when the months starts he counts the number of sundays he will get to enjoy. Considering the month can start with any day, be it Sunday, Monday…. Or so on.

Count the number of Sunday jack will get within n number of days.

 Example 1:

Input 

mon-> input String denoting the start of the month.

13  -> input integer denoting the number of days from the start of the month.

Output :

2    -> number of days within 13 days.

Explanation:

The month start with mon(Monday). So the upcoming sunday will arrive in next 6 days. And then next Sunday in next 7 days and so on.

Now total number of days are 13. It means 6 days to first sunday and then remaining 7 days will end up in another sunday. Total 2 sundays may fall within 13 days.
'''
def countSundays(day, n):

    days = {
        "mon"   : 1, 
        "tue"   : 2, 
        "wed"   : 3, 
        "thurs" : 4, 
        "fri"   : 5, 
        "sat"   : 6, 
        "sun"   : 7
    }

    n += 1

    diff = days['sun'] - days[day]

    count = 0

    for i in range(diff+1, n+1, 7):
        count += 1
      # print(i)
    return count

# Try to solve it using modulos operator

# def countSundays(day, n):






day, n = 'mon', 13
print(countSundays(day, n))