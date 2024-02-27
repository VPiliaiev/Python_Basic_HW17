# Ввести з клавіатури 4 рядки та зберегти їх у 4 різні змінні.
# Створити файл і записати в нього перші 2 рядки та закрити файл.
# Потім відкрити файл на редагування і дозаписати 2 рядки, що залишилися.
# У підсумку файл має бути 4 рядки, кожен з яких повинен починатися з нового рядка.


line1 = input('Введіть перший рядок: ')
line2 = input('Введіть другий рядок: ')
line3 = input('Введіть третій рядок: ')
line4 = input('Введіть четвертий рядок: ')

with open('i.txt', 'w') as file:
    file.write(line1 + '\n')
    file.write(line2 + '\n')
with open('i.txt', 'a') as file:
    file.write(line3 + '\n')
    file.write(line4 + '\n')


# Hello World
# World Hello
# Python World
# World Python





