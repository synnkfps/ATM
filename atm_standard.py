bills = {100:0, 50:0, 20:0, 10:0, 5:0, 2:0}

def sacar(withdraw):
    money = bills.keys()
    
    for i in money:
        while withdraw >= i and not ((withdraw % i == 1 or withdraw % i == 3) and (withdraw % i/2) < (i)):
            bills[i] += 1;
            withdraw -= i;

try:
    withdrawValue = float(input("('q' quit 'quit' to quit)\nType an amount: "))
    result = 0;
        
    sacar(withdrawValue);

    for i in bills:
        if bills[i] != 0:
            print(f'Bills of ${i}: {bills[i]}')
        
        result += i*bills[i]
        
    print(f'Final result: {result}')
except:
    print("Type a valid amount (x.x.x or strings aren't supported)")
