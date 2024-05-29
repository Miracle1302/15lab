import pandas as pd

# Створення словника
temperature_data = {
    "Month": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "Kyiv": [-3.5, -2.0, 4.0, 12.0, 18.0, 21.0, 22.5, 21.5, 16.0, 9.5, 3.5, -1.0],
    "Lviv": [-4.0, -3.0, 3.0, 10.5, 16.0, 19.5, 21.0, 20.0, 14.5, 8.0, 2.0, -2.5]
}

# Перетворення словника у датафрейм
df = pd.DataFrame(temperature_data)

# Вивід датафрейму на екран
print(df)

# Обрахування середньої температури за рік тільки для числових стовпців
average_temp = df[["Kyiv", "Lviv"]].mean()

# Вивід результатів на екран
print("\nAverage Yearly Temperature:")
print(average_temp)



