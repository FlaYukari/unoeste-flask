from Modelo.Cliente import Cliente
from Persistencia.ClienteBD import ClienteBD

meuCliente = Cliente(0, "Flávia", "000000", "0000002", "01/01/2010", "rua bahia", "001", "apto 1", "solo", "00000-000", "Campinas", "SP", "34444-33333", "99999-9999")

clienteBD = ClienteBD()
clienteBD.incluir(meuCliente)
print("O código gerado foi " + str(meuCliente.codigo))