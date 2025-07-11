stock_prices = {"AAPL": 180, "TSLA": 250}
stock = input("Enter stock symbol (AAPL or TSLA): ").upper()
qty = int(input("Enter quantity: "))
if stock in stock_prices:
    total = stock_prices[stock] * qty
    print(f"Total investment in {stock}: ${total}")
else:
    print("Stock not found.")
save = input("Save result to file? (y/n): ").lower()
if save == "y":
    with open("portfolio.txt", "w") as f:
        f.write(f"{stock},{qty},{stock_prices.get(stock, 0)},{total}\n")
    print("Saved to portfolio.txt")
