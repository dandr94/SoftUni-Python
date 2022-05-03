deposit_sum = float(input())
deposit_limit = int(input())
yearly_interest = float(input())


interest = deposit_sum * yearly_interest / 100
interest_for_one_month = interest / 12
sum = deposit_sum + (deposit_limit * interest_for_one_month)
print(sum)