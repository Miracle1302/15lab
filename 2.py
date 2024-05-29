import pandas as pd


file_path = 'comptagevelo2013.csv'
df = pd.read_csv(file_path)


df['Date'] = pd.to_datetime(df['Date'])


df['Month'] = df['Date'].dt.month

# Сума кількості використання всіх велодоріжок у кожному рядку
df['Total'] = df.drop(columns=['Date', 'Month']).sum(axis=1)


monthly_totals = df.groupby('Month')['Total'].sum()

# Визначення місяця з найбільшою кількістю використань
most_popular_month = monthly_totals.idxmax()
most_popular_usage = monthly_totals[most_popular_month]

print(f"Найбільш популярний місяць: {most_popular_month} з {most_popular_usage} використаннями")

# Опціонально: виведення даних про використання для кожного місяця
print(monthly_totals)

