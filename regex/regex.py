import re

string = 'Hello my phone number is (61)9999-9999'
string2 = "The car license plate of the car i wrote down during the crash is FRT-1998"
email = "Plase contact me, my personal email is example@example.com"

print(re.search('/(/d{2}/)/d{4,5}-/d{4}', string))

