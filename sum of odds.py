sum_of_odds = 0
for number in range(1, 101):
    if number % 2 != 0:
        sum_of_odds += number
        print(sum_of_odds)
        
