age = int(input('please input your age: '))
experience = int(input('please input your expirience: '))
height = float(input('please input your height: '))
isHired = age >= 18 and experience >= 2 and height >= 175
print('you are hired: ' + str (isHired))