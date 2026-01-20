brand = 'Ford'
models = ['maverick', 'escape', 'explorer', 'bronco', 'f-150']
models.append('Mustang')
colors = ['Red', 'Grey', 'Silver', 'Black', 'Blue']
colors[4] = 'Tan'
year = 2026
MSRP_Maverick = 30000
MSRP_Escape = 31000
MSRP_Explorer = 35000
MSRP_Bronco = 39000
MSRP_F150 = 40000
fouryr = 48
fiveyr = 60
sixyr = 72
guest_name = 'Bob'
print(f'Welcome to our dealership, {guest_name}')
print('Welcome to Trojan Trades Dealership!')
models = [m.title() for m in models]
models.sort()
print(models)
months = input("Enter the number of months for your payment:")
monthly_payment = MSRP_Maverick / int(months)
print(f'You would pay ${monthly_payment} every month for {months} months.')
print(f'For 5 months it would be ${MSRP_Maverick / 5} every month for 5 months.')