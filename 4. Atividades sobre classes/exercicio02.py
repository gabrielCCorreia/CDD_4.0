class ContaBancaria:
    def __init__(self, numero_conta, tipo_conta, saldo, status_conta, nome_cliente):
        self.numero_conta = numero_conta
        self.tipo_conta = tipo_conta
        self.saldo = saldo
        self.status_conta = status_conta
        self.nome_cliente = nome_cliente

    def depositar(self, deposito):
        if self.status_conta:
            if deposito > 0:
                self.saldo += deposito
                print(f"Depósito de R$ {deposito} realizado com sucesso.")
            elif deposito == 0:
                print(f"Erro: Digite um valor maior do que zero para depositar.")
            else:
                print(f"Erro: Não é possível realizar um depósito de valor negativo.")
        else:
            print(f"Erro: Sua conta está desativada.")

    def sacar(self, saque):
        if self.status_conta:
            if saque > 0:
                if saque <= self.saldo:
                    self.saldo -= saque
                    print(f"Saque de R$ {saque} realizado com sucesso.")
                else:
                    print(f"Erro: Valor a sacar é maior do que o saldo disponível.")
            elif saque == 0:
                print(f"Erro: Digite um valor maior do que zero para sacar.")
            else:
                print(f"Erro: Não é possível realizar um saque de valor negativo.")
        else:
            print(f"Erro: Sua conta está desativada.")

    def verificar_saldo(self):
        if self.status_conta:
            print(f"Saldo disponível: R$ {self.saldo}")
        else:
            print(f"Erro: Sua conta está desativada.")

    def ativar(self):
        if not self.status_conta:
            self.status_conta = True
            print(f"Sua conta foi ativada.")
        else:
            print(f"Sua conta já está ativa.")

    def desativar(self):
        if self.saldo == 0:
            self.status_conta = False
            print(f"Sua conta foi desativada.")
        elif not self.status_conta:
            print(f"Sua conta já está desativada.")
        elif self.saldo < 0:
            print(f"Erro: Seu saldo está negativo (é necessário zerar o saldo).")
        else:
            print(f"Erro: Saldo disponível na conta (é necessário zerar o saldo).")


p1 = ContaBancaria("1234-5678-9012-3456", "Conta Poupança", 0.0, True, "Gabriel C. C. Santos")
