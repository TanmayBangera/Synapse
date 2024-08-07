request_spending = {
    "Mahek": {
        "balance": 3000.00, 
        "transactions": [
            {"amount": -9000.00, "category": "Creatives"},
            {"amount": 7000.00, "category": "Sponsor"},
            {"amount": -2000.00, "category": "Prize-Money"} 
        ]
    },
    "Arham": {
        "balance": 5000.00, 
        "transactions": [
            {"amount": 8000.00, "category": "Stalls"},
            {"amount": 7500.00, "category": "Seminars"} 
        ]
    },
    "Unnati": {
        "balance": 3500.00, 
        "transactions": [
            {"amount": -5000.00, "category": "Attraction"},
            {"amount": 2500.00, "category": "Promo"},
            {"amount": -900.00, "category": "Lighting"},
            {"amount": -3000.00, "category": "Games"}
        ]
    },
    "Gaurang": {
        "balance": 2000.00, 
        "transactions": [
            {"amount": -1500.00, "category": "Website"},
            {"amount": -1000.00, "category": "C2C"},
            {"amount": -500.00, "category": "Posters"} 
        ]
    },

}


def total_spending(request_spending, account_id: str, category: str):
    acc = request_spending[account_id]
    passBook = acc["transactions"]
    for i in range(len(passBook)):
        if (passBook[i]["category"] == category):
            spent = passBook[i]["amount"]
        else:
            continue
    if (spent > 0):
        print(f"Money received by {account_id} in {category} is {spent}")
    else:
        print(f"Money spent by {account_id} in {category} is {(spent) * -1}")
    

def account_balance(request_spending, account_id: str):
    acc = request_spending[account_id]
    trans = 0
    passBook = acc["transactions"]
    for i in range(len(passBook)):
        trans += passBook[i]["amount"]
    totalBalance = acc["balance"] + trans
    print(f"Balance in {account_id}'s account is {totalBalance}")
    return totalBalance


def money_owed(request_spending, account_id: str):
    moneyOwed = account_balance(request_spending, account_id)
    if moneyOwed < 0:
        print(f"Money owed to {account_id} is {(moneyOwed) * -1}")
    else:
        print(f"{account_id} owes us {moneyOwed}")


