def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
def main():
    try:
        original_price = float(input("Enter the original price of the item: "))
        discount_percentage = float(input("Enter the discount percentage: "))

        final_price = calculate_discount(original_price, discount_percentage)
        print(f"The final price after discount is: {final_price}")

        if final_price == original_price:
            print("No discount applied. The original price is: ${original_price: .2f}")
        else: 
            print(f"The final price after applying the discount is: ${final_price: .f}")
            
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()