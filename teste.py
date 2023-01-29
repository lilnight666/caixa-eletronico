menu= '''
 [d] depositar
 [s]sacar
 [e]extrato
 [q]sair
'''

saldo=0
limite=500
extrato=''
numero_saques=0
LIMITE_SAQUE=3
while True:
      opcao=input(menu)
      
      if opcao== 'd':
            valor= float(input('informe o valor do deposito'))

            if valor >0:
                  saldo+= valor
                  extrato+= f'deposito R${valor:.2f}'

            else:
                  print('operação invalida digite um valor valido')

      elif opcao =='s':
            valor= float(input('informe o valor do saque '))

            excedeu_saldo=valor>saldo
            excedeu_limite= valor>limite
            exedeu_saques= numero_saques>= LIMITE_SAQUE

            if excedeu_saldo:
                  print('operação invalida por falta de saldo ')
            elif excedeu_limite:
                  print('operação invalida o valor do saque excedeu o limite')

            elif exedeu_saques:
                  print('voce atingiu o limite de saques')

            elif valor>0:
                  saldo-=valor
                  extrato+=f'saque: R${valor:.2f}'
                  numero_saques+=1
            else:
                  print('operação invalida o valor informado é invalido ')
      elif opcao=='e':
            print('não foram realizadas novas movimentações 'if not extrato else extrato)
            print(f'saldo: R${saldo:.2f}')

      elif opcao=='q':
            break
      else:
            print('operação invalida')