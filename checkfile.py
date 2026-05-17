try:
    with open("balance.txt", "r") as file:
        balance = float(file.read())

except:
    balance = 0

    with open("balance.txt", "w") as file:
        file.write(str(balance))