class Pessoa :
    nome = None
    telefone = None
    email = None
    endereco = None

    def __init__(self, nome, telefone, email, endereco) :
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def info(self):
        print(self.nome)
        print(self.telefone)
        print(self.email)
        print(self.endereco)

###############################################################

class Aluno(Pessoa):
    curso = None
    
    def __init__(self, nome, telefone, email, endereco, curso) :
        super().__init__(nome, telefone, email, endereco)
        self.curso = curso
    
    def setCurso(self, curso):
        self.curso = curso

    def info(self):
        super().info()
        print(self.curso)  
     
################################################################

p1 = Pessoa('João', '88888', 'joao@gmail.com', 'rua A')
p1.info()

a1 = Aluno('Maria', '00000099','mari@gmail.com', 'rua B', 'Informática')
a1.info()