i = 3
password = 'abc123456'

while i > 0:
	i = i - 1
	password_type = input('請輸入密碼: ')
	if password != password_type:
		print('密碼錯誤!你還有', i ,'次機會!')
	else:
		print('密碼正確!')
		break 
		
