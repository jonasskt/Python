class Aplicar:

  def __init__(self, nome, idade, valor, cpf):
    self.nome = nome
    self.idade = idade
    self.cpf = cpf
    self.valor = valor
    self.historico = [valor]
    self.historico_entradas = []
    self.historico_saidas = []

  def transacao(self, valor):
    self.historico.append(valor)


  def depositar(self, valor_aplicado):
    self.historico_entradas.append(valor_aplicado)
    self.valor += valor_aplicado 
    print(f"Você depositou: R$ {valor_aplicado}")
    return


  def saque(self, valor_saque):
    self.historico_saidas.append(valor_saque)
    self.transacao(self.valor)
    self.valor -= valor_saque
    print(f"Você sacou R${valor_saque}")
    print(f"Saldo atual: R${self.valor}")
    return self.historico_saidas
     
  

  def extrato(self):
    print(f"Saídas: {self.historico_saidas}")
    print(f"Entradas: {self.historico_entradas}")
    for valor in self.historico:
      print(f'Saldo disponível: R${valor}')
    
  def transferir(self, valor_enviar, destino):
    self.saque(valor_enviar)
    destino.depositar(valor_enviar)
    print(f"Você transferiu R${valor_enviar}")
    print(f"Seu saldo é de R${self.valor}")

  def entradas(self):
    print(f"Entradas: R${self.valor}")
    
    


