import random

def pay(amount, denominations):
    coins = {d:0 for d in sorted(denominations, reverse=True)}
    for coin in coins:
        nr_coins, amount = divmod(amount, coin)
        coins[coin] = nr_coins
    return amount, coins

amount_to_pay = 1000 + random.randrange(2000)
denominations = [1, 2, 5, 10, 20, 50, 100, 200]
print(f'we have to pay: {amount_to_pay}')
print(f'with coins: {denominations}')
remaining, coins = pay(amount_to_pay, denominations)
print('coins:', coins)
print('remaining amount:', remaining)

coins_total = 0
print('\nchecking the result:')
print(f'COIN NR_COINS COIN_TOTAL')
for coin, count in coins.items():
    coin_total = coin * count
    print(f'{coin:4} {count:8} {coin_total:10}') 
    coins_total += coin_total
print(f'               --------- +')
print(f'coins_total:  {coins_total:10}')
print(f'remaining:    {remaining:10}')
print(f'               --------- +')
print(f'              {coins_total+remaining:10}')
