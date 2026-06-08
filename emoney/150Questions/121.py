# # 121. Best Time to Buy and Sell Stock


# may 29


prices = [7,1,5,3,6,4]
# smallest day to buy and everyday lets see if i can see. keep track of lowest

lowest = 0
maxProfit = 0


for x in range(0, len(prices)):
    if prices[lowest] > prices[x]:
        prices[lowest] = prices[x]
    
    profit = prices[x]- prices[lowest]
    if profit > maxProfit:
        maxProfit = profit







# prices = [7,1,5,3,6,4]

# '''
# approach #1: Brute force

# compare all of the combinations in the array and whichever combo (after sub)
# gives the highest answer is our answer

# two numbers that produce the highest -> not two pointers since two pointers does not including looking at all possible combos!!

# '''

# largest = 0
# for x in range(0, len(prices)):
#     for y in range(1, len(prices)-1):
#         profit1 = prices[x] - prices[y]
#         proit2 =  prices[y] - prices[x]
#         print(profit1)
#         print(proit2)
#         # if abs(profit) > largest:
#         #     largest = profit

# print(largest)

# largest = 0
# arr = [7,6,4,3,1]
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if i < j:
#             profit = arr[j] - arr[i]
#         else:
#             profit = arr[i] - arr[j]
        
#         if profit > largest:
#             largest = profit

# print(largest)


# def maxProfit(prices):
#     largest = 0
#     for i in range(len(prices)):
#         for j in range(i+1, len(arr)):
#             if i < j:
#                 profit = prices[j] - prices[i]
#             else:
#                 profit = prices[i] - prices[j]
            
#             if profit > largest:
#                 largest = profit
#     return largest

# arr = [7,6,4,3,1]
# cheapest = arr[0]
# largestProfit = 0

# for x in range(0, len(arr)):
#     if arr[x] < cheapest:
#         cheapest = arr[x]
    
#     profit = arr[x] - cheapest
#     if profit > largestProfit:
#         largestProfit = profit
    

# print(cheapest)
# print(largestProfit)
# # cheapest price seen so fat









def maxProfit(prices):
    cheapest = prices[0]
    largestProfit = 0

    for x in range(0, len(prices)):
        if prices[x] < cheapest:
            cheapest = prices[x]
        
        profit = prices[x] - cheapest
        if profit > largestProfit:
            largestProfit = profit
    
    return prices


print()





