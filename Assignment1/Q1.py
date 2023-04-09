# Q1.) Write a Python program that takes a list of daily stock prices as input, and returns the best 
# days to buy and sell stocks in order to maximize profit. The list contains the stock prices for 
# each day, starting from the first day. 
# For example, the list (100, 180, 260, 310, 40, 535, 695) represents the stock prices for 7 days, 
# where the price on the first day is 100, the second day is 180, and so on. 
# The program should find the best days to buy and sell stocks such that the profit obtained is 
# maximum. For instance, in the given list of stock prices, the best days to buy and sell stocks 
# would be: 
# Buy stock on the 1st day (price=100) 
# Sell stock on the 4th day (price=310)
# Buy stock on the 5th day (price=40) 
# Sell stock on the 7th day (price=695) 
# The program should output these buy and sell days as a tuple or list of integers. give me 
# solution of this program



def stockBuySell(price, n):
	
	# Prices must be given for at
	# least two days
	if (n == 1):
		return
	
	# Traverse through given price array
	i = 0
	while (i < (n - 1)):
		
		# Find Local Minima
		# Note that the limit is (n-2) as
		# we are comparing present element
		# to the next element
		while ((i < (n - 1)) and
				(price[i + 1] <= price[i])):
			i += 1
		
		# If we reached the end, break
		# as no further solution possible
		if (i == n - 1):
			break
		
		# Store the index of minima
		buy = i
		i += 1
		
		# Find Local Maxima
		# Note that the limit is (n-1) as we are
		# comparing to previous element
		while ((i < n) and
			(price[i] >= price[i - 1])):
			i += 1
			
		# Store the index of maxima
		sell = i - 1
		
		print("Buy on day: ",buy," ",
				"Sell on day: ",sell)
		
# Driver code

# Stock prices on consecutive days
price = [100, 180, 260,
		310, 40, 535, 695]
n = len(price)

# Function call
stockBuySell(price, n)
