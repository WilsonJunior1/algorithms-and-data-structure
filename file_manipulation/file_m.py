with open ("./file_example.txt") as text:
  file = text.readlines()
  print(file)

with open('file_create_with_python.txt', 'w') as text2:
  text2.write("Hello! I'm a line wrote with python.")