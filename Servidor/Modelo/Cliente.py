class Cliente(object):

    #costrutor da classe Pet
    def __init__(self, codigo=0, nome="", rg="", cpf="", dataNasc="", endereco="", num="", complemento="", bairro="", cep="", cidade="", uf="", telFixo="", telCel=""):
        self.__codigo = codigo
        self.__nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.__dataNasc = dataNasc
        self.__endereco = endereco
        self.__num = num
        self.__complemento = complemento
        self.__bairro = bairro
        self.__cep = cep
        self.__cidade = cidade
        self.__uf = uf
        self.__telFixo = telFixo
        self.__telCel = telCel
    
    #1-método get
    @property
    def codigo(self):
        return self.__codigo
    #método set
    @codigo.setter
    def codigo(self, novoCodigo):
        self.__codigo = novoCodigo


    #2-método get
    @property
    def nome(self):
        return self.__nome
    #método set
    @nome.setter
    def nome(self, novoNome):
        self.__nome = novoNome
    

    #3-método get
    @property
    def rg(self):
        return self.__rg
    #método set
    @rg.setter
    def rg(self, novoRg):
        self.__rg = novoRg

    
    #4-método get
    @property
    def cpf(self):
        return self.__cpf
    #método set
    @cpf.setter
    def cpf(self, novoCpf):
        self.__cpf = novoCpf

    
    #5-método get
    @property
    def dataNasc(self):
        return self.__dataNasc
    #método set
    @dataNasc.setter
    def dataNasc(self, novoDataNasc):
        self.__dataNasc = novoDataNasc
    

    #6-método get
    @property
    def endereco(self):
        return self.__endereco
    #método set
    @endereco.setter
    def endereco(self, novoEndereco):
        self.__endereco = novoEndereco
    

    #7-método get
    @property
    def num(self):
        return self.__num
    #método set
    @num.setter
    def num(self, novoNum):
        self.__num = novoNum


    #8-método get
    @property
    def complemento(self):
        return self.__complemento
    #método set
    @complemento.setter
    def complemento(self, novoComplemento):
        self.__complemento = novoComplemento


    #9-método get
    @property
    def bairro(self):
        return self.__bairro
    #método set
    @bairro.setter
    def bairro(self, novoBairro):
        self.__bairro = novoBairro


    #10-método get
    @property
    def cep(self):
        return self.__cep
    #método set
    @cep.setter
    def cep(self, novoCep):
        self.__cep = novoCep
    

    #11-método get
    @property
    def cidade(self):
        return self.__cidade
    #método set
    @cidade.setter
    def cidade(self, novoCidade):
        self.__cidade = novoCidade

    
    #12-método get
    @property
    def uf(self):
        return self.__uf
    #método set
    @uf.setter
    def uf(self, novoUf):
        self.__uf = novoUf
    

    #13-método get
    @property
    def telFixo(self):
        return self.__telFixo
    #método set
    @telFixo.setter
    def telFixo(self, novoTelFixo):
        self.__telFixo = novoTelFixo

    
    #14-método get
    @property
    def telCel(self):
        return self.__telCel
    #método set
    @telCel.setter
    def telCel(self, novoTelCel):
        self.__telCel = novoTelCel
    

    def __str__(self):
        return "Eu sou " + self.__nome + " e meu celular é " + self.__telCel