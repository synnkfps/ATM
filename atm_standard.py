bills = {100:0, 50:0, 20:0, 10:0, 5:0, 2:0}

def withdraw(value):
    money = bills.keys()
    
    for i in money:
        while value >= i and not ((value % i == 1 or value % i == 3) and (value % i/2) < (i)):
            bills[i] += 1;
            withdraw -= i;

try:
    withdrawValue = float(input("('q' quit 'quit' to quit)\nType an amount: "))
    result = 0;
        
    withdraw(withdrawValue);

    for i in bills:
        if bills[i] != 0:
            print(f'Bills of ${i}: {bills[i]}')
        
        result += i*bills[i]
        
    print(f'Final result: {result}')
except:
    print("Type a valid amount (x.x.x or strings aren't supported)")
