def Main():
    currentSharesOwned = 40
    targetPrice = float(input("What is the target price to sell shares at?: $"))
    currentPrice = float(input("What is the current price per share: $"))

    while currentPrice < targetPrice:
        currentPrice = currentPrice + 10.00

    print("Current value per share is " + str(currentPrice))
    print("Shares can be sold now")

Main()