 # import Decimal
 # capital = decimal.Decimal('1000.00')
capital = 1000
rendimiento = 0.05  

for n in range(1,11):
    dinero_total = capital*(1 + rendimiento)**n
    print(f'{n:<4}{dinero_total:<10.2f}')
    
    


