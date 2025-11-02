def execute():
    number = int(input("Enter a number: "))
    digits = [int(c) for c in str(number)]
    countDigits = 0
    total = 0
    
    while(countDigits < len(digits)):
        total += digits[countDigits]
        countDigits += 1
    
    print("Total is: ", total)