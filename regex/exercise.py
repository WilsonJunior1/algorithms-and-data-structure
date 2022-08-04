#Make expressões regulares para extrair as seguintes informações do texto abaixo (use a função findall):
#- Números
#- CEPs
#- URLs

import re

text = ''' 
Although google.com is the most used search engine at the moment, 
it is a fact that it is not perfect and there are alternatives that 
can hit where it fails, some examples are:
    bing.com
    duckduckgo.com
    yahoo.com


It is estimated that our galaxy, the Milky Way, has 200 to 400 billion stars. 
Galaxies have on average hundreds of billions of stars. 
And estimates also point to hundreds of billions of galaxies in the Universe. 
This would result in the existence of more than 10 sextillion stars.

In the case of CEP 13165-000, for example, we can see that the code refers to
a location in the interior of São Paulo, since its first digit starts with the 
number 1. If we analyze each of the other digits according to the criteria 
established, we will come to the conclusion that the CEP refers to the city 
of Engenheiro Coelho. The last three digits of the code refer to the 
individual identification of locations, places, special codes and postal units.

CEP 40315-086 is also valid, as is:
39400-338

'''

cep = '\d{5}-\d{3}'
url = '\w+\.\w+'
numbers = '\d+'

print(re.findall(cep, text))
print(re.findall(url, text))
print(re.findall(numbers, text))
