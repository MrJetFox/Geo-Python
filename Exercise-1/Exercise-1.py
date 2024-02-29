import random  # Решил сделать любовь к мороженному и сну волей случая

def sr(a, b):
    a = (a + b) / 2
    return a

first_name = input("Моё имя: ")
last_name = input("Моя фамилия: ")
my_name = first_name + " " + last_name

ice_cream_rating = random.randint(0, 10)
sleep_rating = random.randint(0, 10)
happiness_rating = sr(ice_cream_rating, sleep_rating)
print(F"Меня зовут {first_name}, и я ставлю мороженому {ice_cream_rating} баллов из 10!")
print(F"Я {my_name}, и мой рейтинг удовольствия от сна — {sleep_rating} из 10!")
print(F"Исходя из вышеперечисленных факторов, мой рейтинг счастья составляет {happiness_rating} из 10, или {happiness_rating * 10}%!")
