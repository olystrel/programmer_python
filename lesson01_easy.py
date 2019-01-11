_author_='Olga_Strelenko'

#Задача1

number = int(input(' Введите число '))
for i in str(number):
    	print(i)

#Задача2

answer_user= input('Введите данные ' )
answer_user1= input('Введите данные1 ')
answer_change = ''
answer_change = answer_user
answer_user=answer_user1
answer_user1= answer_change
print(answer_user, answer_user1)


#Задача3
age=int(input('Введите свой возраст '))
if age >= 18:
    print('Доступ разрешен')

else:
    print('Извините, пользование данным ресурсом только с 18 лет')

