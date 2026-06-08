# Classe mãe
class Funcionario:
    def _init_(self, nome, salario):
        self.__nome = nome
        self.set_salario(salario)

    def get_nome(self):
        return self.__nome

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        if salario < 0:
            raise ValueError("Salário não pode ser negativo.")
        self.__salario = salario

    def calcular_salario(self):
        return self.__salario


# Classe filha CLT
class CLT(Funcionario):
    def _init_(self, nome, salario):
        super()._init_(nome, salario)

    def calcular_salario(self):
        return self.get_salario()


# Classe filha Vendedor
class Vendedor(Funcionario):
    def _init_(self, nome, salario, comissao):
        super()._init_(nome, salario)
        self.__comissao = comissao

    def calcular_salario(self):
        return self.get_salario() + self.__comissao


# Classe filha Gerente
class Gerente(Funcionario):
    def _init_(self, nome, salario, bonus):
        super()._init_(nome, salario)
        self.__bonus = bonus

    def calcular_salario(self):
        return self.get_salario() + self.__bonus


# Programa principal
funcionarios = [
    CLT("João", 2500),
    Vendedor("Maria", 2000, 500),
    Gerente("Carlos", 4000, 1500)
]

for funcionario in funcionarios:
    print(
        f"Nome: {funcionario.get_nome()} | "
        f"Salário: R$ {funcionario.calcular_salario():.2f}"
    )