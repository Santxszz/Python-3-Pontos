import os

os.system('cls')

membros = []
total_lavado = []
cargos = []

situacao = ''

meta_batida = []
meta_nbatida = []

contador_cumprido = 0
contador_não_cumprido = 0

print('# --- [ Menu ] --- #')
print('[1] Iniciar ')
print('[0] Sair')
print('# --- [ ---- ] --- #')

opção = int(input('# Opção: '))

if opção == 1:
    os.system('cls')
    print('# --- [ ---- ] --- #')
    qtd_membros = int(input('# Total de Membros: '))
    lucro = int(input('# Lucro: '))
    os.system('cls')
    for i in range(qtd_membros):
        membros.append(input('# Nome: '))
        total_lavado.append(float(input('# Total Lavado: ')))
        cargos.append(input('# Cargo: '))
        os.system('cls')

    for valor in range(len(membros)):
        if cargos[valor] == 'Gaijin' and total_lavado[valor] < 7000000:
            situacao = 'Meta Não Cumprida'
            contador_não_cumprido += 1
            meta_nbatida.append(membros[valor])

        elif cargos[valor] == 'Gaijin' and total_lavado[valor] >= 7000000:
            situacao = 'Meta Cumprida'
            contador_cumprido += 1
            meta_batida.append(membros[valor])
        
        if cargos[valor] == 'Shatei' and total_lavado[valor] < 6000000:
            situacao = 'Meta Não Cumprida'
            contador_não_cumprido += 1
            meta_nbatida.append(membros[valor])
        
        elif cargos[valor] == 'Shatei' and total_lavado[valor] >= 6000000:
            situacao = 'Meta Cumprida'
            contador_cumprido += 1
            meta_batida.append(membros[valor])
        
        if cargos[valor] == 'Kyodai' and total_lavado[valor] < 5500000:
            situacao = 'Meta Não Cumprida'
            contador_não_cumprido += 1
            meta_nbatida.append(membros[valor])
        
        elif cargos[valor] == 'Kyodai' and total_lavado[valor] >= 5500000:
            situacao = 'Meta Cumprida'
            contador_cumprido += 1
            meta_batida.append(membros[valor])

        if cargos[valor] == 'Kaikei' and total_lavado[valor] < 5000000:
            situacao = 'Meta Não Cumprida'
            contador_não_cumprido += 1
            meta_nbatida.append(membros[valor])        
        elif cargos[valor] == 'Kaikei' and total_lavado[valor] >= 5000000:
            situacao = 'Meta Cumprida'
            contador_cumprido += 1
            meta_batida.append(membros[valor])
        
        if cargos[valor] == 'Shingin' and total_lavado[valor] < 4500000:
            situacao = 'Meta Não Cumprida'
            contador_não_cumprido += 1
            meta_nbatida.append(membros[valor])

        elif cargos[valor] == 'Shingin' and total_lavado[valor] >= 4500000:
            situacao = 'Meta Cumprida'
            contador_cumprido += 1
            meta_batida.append(membros[valor])
        

        porcentagem_gerentes = (40 / 100) * lucro
        porcentagem_membros = (60 / 100) * lucro

        if contador_cumprido == 0:
            contador_cumprido = 0

        if contador_cumprido != 0:
            valor_membros = (porcentagem_membros / contador_cumprido)
        else:
            valor_membros = 0

        valor_gerentes = porcentagem_gerentes / 3



        print('# [ {0} ] - [ R$ {1} ] - [ {2} ]'.format(membros[valor], total_lavado[valor], situacao))
print('')
print('# [ Cumpriram: {0} ] - [ Não Cumpriram: {1} ]'.format(contador_cumprido, contador_não_cumprido))
print('')
print('\033[1;92m# [ Membros Cumpridos: {} ]\033[0;0m'.format(meta_batida))
print('\033[1;31m# [ Membros Não Cumpridos: {} ]\033[0;0m'.format(meta_nbatida))
print('')
print('# [ Lucro Gerência: R$ {} ]'.format(porcentagem_gerentes))
print('# [ Lucro Membros: R$ {} ]'.format(porcentagem_membros))
print('')
print('# [ Salário Membros: R$ {} ]'.format(valor_membros))
print('# [ Salário Gerentes: R$ {} ]'.format(valor_gerentes))


if opção == 0:
    exit()

