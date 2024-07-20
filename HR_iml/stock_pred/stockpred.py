import sys

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    
    if not input_lines:
        print("No input provided.")
        return
    
    # Read the first line for the initial parameters
    first_line = input_lines[0].split()
    try:
        m = float(first_line[0])
        k = int(first_line[1])
        d = int(first_line[2])
    except ValueError:
        print("Error parsing the initial line.")
        return
    
    transactions = []
    
    for line in input_lines[1:k+1]:
        parts = line.split()
        
        if len(parts) < 7:
            print(f"Error: Not enough data on line: {line}")
            continue
        
        name = parts[0]
        try:
            owned = int(parts[1])
            prices = list(map(float, parts[2:]))
        except ValueError:
            print(f"Error parsing values on line: {line}")
            continue
        
        current_price = prices[-1]
        previous_price = prices[-2]
        
        # Simple strategy for buying or selling
        if current_price > previous_price and m >= current_price:
            shares_to_buy = int(m // current_price)
            transactions.append(f"{name} BUY {shares_to_buy}")
            m -= shares_to_buy * current_price
        elif current_price < previous_price and owned > 0:
            transactions.append(f"{name} SELL {owned}")
    
    # Print the number of transactions
    print(len(transactions))
    
    # Print each transaction
    for transaction in transactions:
        print(transaction)

if __name__ == "__main__":
    main()
