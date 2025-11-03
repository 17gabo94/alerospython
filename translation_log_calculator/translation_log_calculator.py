def execute():
    transaction_log = ["DEPOSIT,100", "WITHDRAW, 20", "DEPOSIT,50", "WITHDRAW,75"]
    calculate_final_balance(transaction_log)

def calculate_final_balance(transaction_log):
    index = 0
    totalBalance = 0
    while(index < len(transaction_log)):
        transaction = transaction_log[index]
        transactionType = transaction.split(",")[0]
        amount = int(transaction.split(",")[1])
        if(transactionType == "DEPOSIT"):
            totalBalance += amount
        else:
            totalBalance -= amount

        index += 1

    print("Final balance: ", totalBalance)
