def lerarquivo(nomearquivo, M):
    with open(nomearquivo, 'r') as arquivo:
        linhas = [linha.strip().replace(' ', '') for linha in arquivo if linha.strip()]
    i = 0
    for linha in linhas:
        M[i] = linha
        if linha == "0111":
            i += 1
            break
        i += 1
    dadosi = i
    dadoscomeco=i
    for linha in linhas[i:]:
        M[dadosi] = binparadecimal(linha)
        dadosi += 1
    return dadoscomeco
def binparaint(binario):
    return int(binario, 2)
def binprastr(binario):
    return str(binario)
def obteroperacao(binario):
    if binario == "0000":
        return "Jns"
    elif binario == "0001":
        return "Load"
    elif binario == "0010":
        return "Store"
    elif binario == "0011":
        return "Add"
    elif binario == "0100":
        return "Sub"
    elif binario == "0101":
        return "Input"
    elif binario == "0110":
        return "Output"
    elif binario == "0111":
        return "Halt"
    elif binario == "1000":
        return "Skipcond"
    elif binario == "1001":
        return "Jump"
    elif binario == "1010":
        return "LoadImmi"
    elif binario == "1011":
        return "Addl"
    elif binario == "1100":
        return "Jumpl"
    elif binario == "1101":
        return "Loadl"
    elif binario == "1110":
        return "Storel"
    else:
        return "Error"
def binparadecimal(binstr):
    return int(binstr[4:], 2)
def decodificador(M, saida, dadoscomeco):
    AC = 0
    PC = 0
    tamanhodamemoria = len(M)
    dadoscomeco = dadoscomeco-1
    while PC < tamanhodamemoria:
        strbin = (str(M[PC]))
        opbin = strbin[:4]
        restobin = None
        restobin = strbin[4:]
        operacao = obteroperacao(opbin)
        print(operacao)
        if restobin != "":
            valor = binparaint(restobin)
        incrementar_pc = True
        if operacao == "Add":
            AC += int(M[valor+dadoscomeco])
            saida.append(f"AC={AC}")
        elif operacao == "Sub":
            AC -= int(M[valor+dadoscomeco])
            saida.append(f"AC={AC}")
        elif operacao == "Addl":
            aux = (M[valor+dadoscomeco])
            AC += M[aux]
            saida.append(f"AC={AC}")
        elif operacao == "Load":
            n = M[valor+dadoscomeco]
            AC = n
            saida.append(f"AC={AC}")
        elif operacao == "Store":
            M[valor+dadoscomeco] = str(AC)
            saida.append(f"Mem({valor})={AC}")
        elif operacao == "Storel":
            aux = binparadecimal(M[PC])
            M[aux] = format(AC, '016b')
            saida.append(f"Mem({aux})={AC}")
        elif operacao == "Input":
            AC = int(input("Digite um número: "))
        elif operacao == "Output":
            saida.append(f"Output={AC}")
        elif operacao == "Jump":
            PC = valor
            saida.append(f"PC={PC}")
        elif operacao == "Jumpl":
            aux = (M[valor + dadoscomeco])
            PC += M[aux]
            incrementar_pc = False
            saida.append(f"PC={PC}")
        elif operacao == "Jns":
            M[valor+dadoscomeco] = str(valor)
            incrementar_pc = False
            PC = valor + 1
            saida.append(f"M[{valor}]={M[valor]}")
        elif operacao == "LoadImmi":
            AC = valor
            saida.append(f"AC={AC}")
        elif operacao == "Skipcond":
            if valor == 0 and AC < 0:
                PC += 1
            elif valor == 1024 and AC == 0:
                PC += 1
            elif valor == 2048 and AC > 0:
                PC += 1
            elif valor == 3072 and AC != 0:
                PC += 1
            saida.append(f"PC={PC}")
        elif operacao == "Halt":
            saida.append("Halt")
            break
        if incrementar_pc:
            PC += 1
        print(saida)
arquivotxt = 'Entrada.txt'
saida = []
M = ['0'] * (2**12)
dadoscomeco=lerarquivo(arquivotxt, M)
print(M)
decodificador(M, saida,dadoscomeco)
with open('Saida.txt', 'w') as arquivo_saida:
    for linha in saida:
        arquivo_saida.write(linha + '\n')