import os


def service_six():
	cls()
	while 1:
		b = input('Введите имя сервиса: ')
		f=os.popen("systemctl disable " + b)
		rd=f.read()
		f.close()
		q=os.popen("systemctl is-enabled " + b)
		rq=q.read()
		q.close()
		print(rd)
		print(rq)
		print('0. Выход')
		b = input("Введите:")
		if b == '0':
			break

		cls()

def service_five():
	cls()
	while 1:
		b = input('Введите имя сервиса: ')
		f=os.popen("systemctl enable " + b)
		rd=f.read()
		f.close()
		q=os.popen("systemctl is-enabled " + b)
		rq=q.read()
		q.close()
		print(rd)
		print(rq)
		print('0. Выход')
		b = input("Введите:")
		if b == '0':
			break

		cls()

def service_four():
	cls()
	while 1:
		b = input('Введите имя сервиса: ')
		f=os.popen("systemctl restart " + b)
		rd=f.read()
		f.close()
		q=os.popen("systemctl status " + b)
		rq=q.read()
		q.close()
		print(rd)
		print(rq)
		print('0. Выход')
		b = input("Введите:")
		if b == '0':
			break

		cls()

def service_three():
	cls()
	while 1:
		b = input('Введите имя сервиса: ')
		f=os.popen("systemctl stop " + b)
		rd=f.read()
		f.close()
		q=os.popen("systemctl status " + b)
		rq=q.read()
		q.close()
		print(rd)
		print(rq)
		print('0. Выход')
		b = input("Введите:")
		if b == '0':
			break

		cls()

def service_two():
	cls()
	while 1:
		b = input('Введите имя сервиса: ')
		f=os.popen("systemctl start " + b)
		rd=f.read()
		f.close()
		q=os.popen("systemctl status " + b)
		rq=q.read()
		q.close()
		print(rd)
		print(rq)
		print('0. Выход')
		b = input("Введите:")
		if b == '0':
			break

		cls()

def service_one():
	cls()
	f=os.popen("systemctl list-unit-files --type service")
	rd=f.read()
	f.close()
	while 1:
		print(rd)
		print('0. Выход')
		v = input("Введите:")
		if v == '0':
			break

		cls()


#Меню №4
def service():
	cls()
	f=os.popen("")
	rd=f.read()
	f.close()
	while 1:
		
		cls()
		print(c)
		v = input("Введите:")
		if v == '1':
			service_one()
		elif v == '2':
			service_two()
		elif v == '3':
			service_three()	
		elif v == '4':
			service_four()
		elif v == '5':
			service_five()
		elif v == '6':
			service_six()
		elif v == '0':
			break

		cls()

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

def ip_network():
	cls()
	while 1:
		b = input('Введите ip: ')
		c = input('Введите маску: ')
		d = input('Введите имя интерфейса: ')
		f=os.popen("ip addr add " + b + "/" + c + " dev " + d)
		rd=f.read()
		f.close()
		q=os.popen("systemctl restart network ")
		rq=q.read()
		q.close()
		print(rd)
		print(rq)
		print('0. Выход')
		b = input("Введите:")
		if b == '0':
			break

		cls()

def network_interface():
	cls()
	f=os.popen("ls | grep /etc/sysconfig/network-scripts/ifcfg-")
	rd=f.read()
	f.close()
	while 1:
		print(rd)
		print('0. Выход')
		v = input("Введите:")
		if v == '0':
			break

		cls()


def start_firewalld():
	cls()
	f=os.popen("systemctl start firewalld")
	rd=f.read()
	f.close()
	while 1:
		print(rd)
		print('0. Выход')
		v = input("Введите:")
		if v == '0':
			break

		cls()

def stop_firewalld():
	cls()
	f=os.popen("systemctl stop firewalld")
	rd=f.read()
	f.close()
	while 1:
		print(rd)
		print('0. Выход')
		v = input("Введите:")
		if v == '0':
			break

		cls()

def network1():
	cls()
	f=os.popen("ip a")
	rd=f.read()
	f.close()
	while 1:
		print(rd)
		print('0. Выход')
		v = input("Введите:")
		if v == '0':
			break

		cls()
#Меню №2
def network():
	cls()
	f=os.popen("")
	rd=f.read()
	f.close()
	while 1:
		
		cls()
		print(b)
		v = input("Введите:")
		if v == '1':
			network1()
		elif v == '2':
			network_interface()
		elif v == '3':
			ip_network()	
		elif v == '4':
			start_firewalld()
		elif v == '5':
			stop_firewalld()
		elif v == '0':
			break

		cls()

def users_4():
	cls()
	while 1:
		b = input("Введите имя пользователя: ")
		f=os.popen("sudo userdel -r " + b)
		rd=f.read()
		f.close()
		print(rd)
		print('0. Выход')
		b = input("Введите:")
		if b == '0':
			break

		cls()

def users_3():
	cls()
	while 1:
		b = input("Введите имя пользователя: ")
		f=os.popen("sudo passwd " + b)
		rd=f.read()
		f.close()
		print(rd)
		print('0. Выход')
		b = input("Введите:")
		if b == '0':
			break

		cls()

def users_2():
	cls()
	while 1:
		b = input("Введите имя пользователя: ")
		f=os.popen("sudo adduser " + b)
		rd=f.read()
		f.close()
		print(rd)
		print('0. Выход')
		b = input("Введите:")
		if b == '0':
			break

		cls()

def users_1():
	cls()
	f=os.popen("less /etc/passwd")
	rd=f.read()
	f.close()
	while 1:
		print(rd)
		print('0. Выход')
		v = input("Введите:")
		if v == '0':
			break

		cls()

#Меню №1
def users():
	cls()
	f=os.popen("")
	rd=f.read()
	f.close()
	while 1:
		
		cls()
		print(d)
		v = input("Введите:")
		if v == '1':
			users_1()
		elif v == '2':
			users_2()
		elif v == '3':
			users_3()	
		elif v == '4':
			users_4()
		elif v == '0':
			break

		cls()

# now, to clear the screen
def hosts():
	cls()
	f = open('/etc/hostname')
	f=f.read()
	while 1:
		print(f)
		print('0. Выход')
		v = input("Введите:")
		if v == '0':
			break

		cls()	

cls()
a = ''' 
1. Пользователи
2. Настроить сеть
3. Имя машины
4. Сервисы
0. Выход
'''
b = '''
1. Просмотр сетевой службы
2. Вывод сетевых интерфейсов
3. Задать IP адрес для сетевого интерфейса
4. Включение фаервола
5. Отключение фаервола
0. Выход
'''
c = '''
1. Вывод сервисов
2. Запуск сервиса
3. Остановка сервиса
4. Перезапуск сервиса
5. Включение автозапуска сервиса
6. Отключение автозапуска сервиса
0. Выход
'''
d = '''
1. Вывод всех пользователей
2. Создание имени пользователя
3. Создание пароля пользователя
4. Удаление пользователя
0. Выход
'''
while 1:

	cls()
	print(a)
	v = input("Введите:")
	if v == '1':
		users()
	elif v == '3':
		hosts()
	elif v == '2':
		network()
	elif v == '4':
		service()
	elif v == '0':
		break

cls()