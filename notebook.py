class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempoDeBateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria

    def get_tempoDeBateria(self):
        return self.__tempoDeBateria

    def set_tempoDeBateria(self, tempo):
        self.__tempoDeBateria = tempo

    def getInformacoes(self):
        info_base = super().getInformacoes()
        return f"{info_base}, Tempo de Bateria: {self.__tempoDeBateria}h"

    def cadastrar(self):
        print("Notebook cadastrado com sucesso!")
