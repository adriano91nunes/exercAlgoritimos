class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potenciaDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potenciaDaFonte

    def get_potenciaDaFonte(self):
        return self._potenciaDaFonte

    def set_potenciaDaFonte(self, potencia):
        self._potenciaDaFonte = potencia

    def getInformacoes(self):
        info_base = super().getInformacoes()
        return f"{info_base}, Potência da Fonte: {self._potenciaDaFonte}W"

    def cadastrar(self):
        print("Desktop cadastrado com sucesso!")
