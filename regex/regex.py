import re 

phone = 'Hello my phone number is (61)9959-9999'
license_plate = "The car license plate of the car i wrote down during the crash is FRT-1998"
email =  "Plase contact me, my personal email is jubileu@gmail.com"


print(re.search('\(\d{2}\)\d{4,5}-\d{4}', phone))
print(re.search('[A-Za-z]{3}-\d{4}', license_plate))
print(re.search('\w+@\w+\.com', email))

# Match Function

phone2 =  '(61)9959-9999 is my phone number' 
print(re.match('\(\d{2}\)\d{4,5}-\d{4}', phone2))

# FindAll Function

phone3 = 'My actual phone number is (99)9999-9999. The phone number (61)0000-0000 is old.'

email2 = ''' 
    Name: test1
    email: test@test.com
    Name: test2
    email test2@test.com
    Name: test3
    email: test3@test.com.br 
'''

print(re.findall('\(\d{2}\)\d{4,5}-\d{4}', phone3))
print(re.findall('\w+@\w+\.\w*', email2))

