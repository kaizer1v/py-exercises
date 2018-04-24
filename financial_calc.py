balance = 4842
annualIterestRate = 0.2
monthlyPaymentRate = 0.04
total = 0.0
ub = balance
monthlyInterestRate = annualIterestRate / 12.0

for month in range(1, 13):
  monthlyPayment = ub * monthlyPaymentRate
  ub = ub - monthlyPayment
  interest = monthlyInterestRate * ub
  total += monthlyPayment
  ub = interest + ub

  #print 'Month: ', month
  #print 'Min month payment: ', round(monthlyPayment, 2)
  #print 'Rem Balance: ', round(ub, 2)

#print 'Total paid: ', round(total, 2)
#print 'Rem Balance: ', round(ub, 2)
