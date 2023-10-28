class ContaBancaria:
    def __init__(self, nome_cliente, numero_conta, tipo_conta):
        self.nome_cliente = nome_cliente
        self.numero_conta = numero_conta
        self.tipo_conta = tipo_conta
        self.saldo = 0.0
        self.limite = 1000
        self.limite_disponivel = self.limite
        self.status_conta = False

    def depositar(self, deposito):
        if self.status_conta:
            if deposito > 0:
                if self.limite_disponivel < self.limite:
                    self.limite_disponivel += deposito
                    if not self.limite_disponivel <= self.limite:
                        self.saldo += (self.limite_disponivel - self.limite)
                        self.limite_disponivel -= (self.limite_disponivel - self.limite)
                    print(f"Depósito de R$ {deposito:.2f} realizado com sucesso.")
                else:
                    self.saldo += deposito
                    print(f"Depósito de R$ {deposito:.2f} realizado com sucesso.")
            else:
                print("Erro: O valor do depósito deve ser maior que zero.")
        else:
            print("Erro: Sua conta está desativada.")

    def sacar(self, saque):
        if self.status_conta:
            if saque > 0:
                if saque <= self.saldo + self.limite_disponivel:
                    if saque > self.saldo:
                        escolha = input("Saldo indisponível. Gostaria de utilizar o limite (s/n)? ")
                        while escolha not in "ssSSnnNN":
                            escolha = input("Resposta inválida. Digite novamente (s/n): ")
                        if escolha in "sS":
                            self.limite_disponivel -= (saque - self.saldo)
                            self.saldo = 0
                            print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
                        else:
                            print(f"Erro: Valor a sacar é maior do que o saldo disponível.")
                    else:
                        self.saldo -= saque
                elif self.saldo == 0:
                    print(f"Erro: Seu saldo está zerado, e o saque ultrapassa o limite da conta disponível.")
                else:
                    print(f"Erro: Saque ultrapassa o saldo e o limite da conta.")
            else:
                print("Erro: O valor do saque deve ser maior que zero.")
        else:
            print("Erro: Sua conta está desativada.")

    def verificar_saldo_e_limite(self):
        if self.status_conta:
            print(f"* Saldo disponível: R$ {self.saldo:.2f}\n"
                  f"* Limite disponível: R$ {self.limite_disponivel:.2f}")
        else:
            print("Erro: Sua conta está desativada.")

    def ativar(self):
        if not self.status_conta:
            self.status_conta = True
            print("Sua conta foi ativada.")
        else:
            print("Sua conta já está ativada.")

    def desativar(self):
        if self.saldo == 0:
            self.status_conta = False
            print("Sua conta foi desativada.")
        elif not self.status_conta:
            print("Sua conta já está desativada.")
        else:
            print("Erro: Seu saldo não está zerado.")


p1 = ContaBancaria("Gabriel C. C. Santos", "1234-5678-9012-3456", "Conta Poupança")

p1.ativar()
p1.sacar(10)
p1.verificar_saldo_e_limite()
p1.depositar(20)
p1.verificar_saldo_e_limite()
