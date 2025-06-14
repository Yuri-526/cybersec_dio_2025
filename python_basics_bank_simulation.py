#!/usr/bin/python3

"""
CONTEXT:
--------
I began a new cybersecurity course on DIO platform and, as the first track, we
are learning python, of course (again, from the scratch). So, as a basic
practical exercise, this script must simulate three ATM machine functions,
namely check balance, deposit and withdraw.

As a starting point, the platform released a code template [1]
(Yeah, I know... please don't hate me.)

 
REFERENCES:
------------
[1] https://github.com/digitalinnovationone/trilha-python-dio/blob/main/00%20-%20Fundamentos/desafio.py
[2] https://github.com/digitalinnovationone/trilha-python-dio/tree/main

"""

class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.status = []
        self.contador_saque = 0
        self.LIMITE_SAQUE = 1000
        self.MAX_SAQUES = 5

    def depositar(self, quantidade):

        if quantidade <= 0:
            return False, "Quantia inválida. O valor a ser depositado precisa ser positivo."

        self.saldo += quantidade
        self.status.append(f"Depósito: +R${quantidade:.2F}")
        return True, f"Depositado R${quantidade:.2F}"

    def sacar(self, quantidade):
        
        if quantidade <= 0:
            return False, "Quantia inválida. O valor a ser sacado precisa ser positivo."
        if quantidade > self.saldo:
            return False, "Fundos insuficientes."
        if quantidade > self.LIMITE_SAQUE:
            return False, f"O limite máximo de saque de R${self.LIMITE_SAQUE:.2F} foi excedido."
        if self.contador_saque >= self.MAX_SAQUES:
            return False, "Número máximo de saques alcançados hoje."

        self.saldo -= quantidade
        self.contador_saque += 1
        self.status.append(f"Saque: -R${quantidade:.2F}")
        return True, f"Saque de R${quantidade:.2F} realiazado."

    def ver_extrato(self):
        header = "=============== STATUS DA CONTA ===============" 
        op = "\n".join(self.status) if self.status else "Nenhuma operação realizada."
        footer = f"\n\nSaldo atual: R$ {self.saldo:.2F}\n" + "=" * len(header)
        return f"{header}\n{op}{footer}"

def main():
    conta = ContaBancaria()

    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    while True:
        opcao = input(menu).strip().lower()

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: R$"))
                sucesso, msg = conta.depositar(valor)
                print(msg)
            except ValueError:
                print("Entrada inválida. Por favor informe um valor numérico.")

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: R$"))
                sucesso, msg = conta.sacar(valor)
                print(msg)
            except ValueError:
                print("Entrada inválida. Por favor informe um valor numérico.")

        elif opcao == "e":
            print(conta.ver_extrato())

        elif opcao == "q":
            print("Obrigado por usar nossos serviços. Volte sempre!")
            break

        else:
            print("Opção inválida. Por favor tente novamente.")

if __name__ == "__main__":
    main()
