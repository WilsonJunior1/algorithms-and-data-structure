#Para revisar o conteúdo prático visto até agora, você agora pode resolver um exercício. 
#Logo em seguida você pode acessar a aula em vídeo com a solução

# Crie uma classe chamada aluno com os seguintes atributos:
# - Nome
# - Nota 1
# - Nota 2
# - Crie um construtor para a classe (__init__)


# Crie as seguintes funções (métodos):
# - Calcula média, retornando a média aritmética entre as notas
# - Mostra dados, que somente imprime o valor de todos os atributos
# - Resultado, que verifica se o aluno está aprovado ou reprovado 
#(se a média for maior ou igual a 6.0, o aluno está aprovado)


# Crie dois objetos (aluno1 e aluno2) e teste as funções

class Student():
    def __init__(self, name, grade_1, grade_2):
        self.name = name
        self.grade_1 = float(grade_1)
        self.grade_2 = float(grade_2)
    
    def average(self):
        average_grades = (self.grade_1 + self.grade_2) / 2
        return average_grades 
    def showData(self):
        print(f'Grade 1: {self.grade_1}\nGrade 2: {self.grade_2}')

    def result(self, average):
        if(float(average) >= 6.0):
            print(f"The student {self.name} is approved.\n")
        else:
            print(f"The student {self.name} is disapproved\n")

student_1 = Student("Will", 8, 6)
student_2 = Student("Guilherme", 4, 3)

print(student_1.average())
student_1.showData()
student_1.result(student_1.average())

print(student_2.average())
student_2.showData()
student_2.result(student_2.average())

