from faker import Faker

fake = Faker()

with open('test_file.csv', 'r+') as f:
    print('Date,Name,Favorite Color', file=f)
    for x in range(10):
        print(f'{fake.date_this_month()},{fake.first_name()}.{fake.last_name()},{fake.color_name()}', file=f)