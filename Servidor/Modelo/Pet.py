class Pet(object):

    #costrutor da classe Pet
    def __init__(self, codigo=0, nome="", especie="", raca="", cor="", dataNasc="", numMricrochip="", rga=""):
        self.__codigo = codigo
        self.__nome = nome
        self.__especie = especie
        self.__raca = raca
        self.__cor = cor
        self.__dataNasc = dataNasc
        self.__numMicrochip = numMricrochip
        self.__rga = rga
    
    #método get
    @property
    def codigo(self):
        return self.__codigo
    #método set
    @codigo.setter
    def codigo(self, novoCodigo):
        self.__codigo = novoCodigo


    #método get
    @property
    def nome(self):
        return self.__nome
    #método set
    @nome.setter
    def nome(self, novoNome):
        self.__nome = novoNome
    

    #método get
    @property
    def especie(self):
        return self.__especie
    #método set
    @especie.setter
    def especie(self, novoEspecie):
        self.__especie = novoEspecie

    
    #método get
    @property
    def raca(self):
        return self.__raca
    #método set
    @raca.setter
    def raca(self, novoRaca):
        self.__raca = novoRaca


    #método get
    @property
    def cor(self):
        return self.__cor
    #método set
    @cor.setter
    def cor(self, novoCor):
        self.__cor = novoCor

    
    #método get
    @property
    def dataNasc(self):
        return self.__dataNasc
    #método set
    @dataNasc.setter
    def dataNasc(self, novoDataNasc):
        self.__dataNasc = novoDataNasc
    

    #método get
    @property
    def numMicrochip(self):
        return self.__numMicrochip
    #método set
    @numMicrochip.setter
    def numMicrochip(self, novoNumMicrochip):
        self.__numMicrochip = novoNumMicrochip


    #método get
    @property
    def rga(self):
        return self.__rga
    #método set
    @rga.setter
    def rga(self, novoRga):
        self.__rga = novoRga

    
    def __str__(self):
        return "Eu sou Pet " + self.__nome + " e sou da raça " + self.__raca