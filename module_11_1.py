import requests
import pandas as pd
import numpy as np

# 1. Библиотека requests
print("=== Библиотека requests ===")
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
if response.status_code == 200:
    # Вывести первые 5 постов из ответа
    posts = response.json()[:5]
    for post in posts:
        print(f"Post ID: {post['id']}, Title: {post['title']}")
else:
    print("Не удалось получить данные")

# 2. Библиотека pandas
print("\n=== Библиотека pandas ===")
# Создадим небольшой DataFrame с данными
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 27, 22, 32],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
print("Исходные данные:")
print(df)

# Выполним несколько операций
print("\nАнализ данных:")
print("Средний возраст:", df['Age'].mean())
print("Группировка по городу:")
print(df.groupby('City').size())

# 3. Библиотека numpy
print("\n=== Библиотека numpy ===")
# Создадим массив
array = np.array([1, 2, 3, 4, 5])
print("Исходный массив:", array)

# Операции с массивом
print("Увеличение массива на 10:", array + 10)
print("Квадрат элементов массива:", np.square(array))
print("Среднее значение массива:", np.mean(array))
