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
        M[dadosi] = linha
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
    AC = 0  # Acumulador
    PC = 0  # Contador de programa
    tamanhodamemoria = len(M)
    while PC < tamanhodamemoria:
        strbin = M[PC]
        if len(strbin) < 4:
            PC += 1
            continue

        opbin = strbin[:4]
        restobin = strbin[4:] if len(strbin) > 4 else ""
        operacao = obteroperacao(opbin)
        valor = binparaint(restobin) if restobin != "" else 0
        incrementar_pc = True

        # Processamento das instruções
        if operacao == "Add":
            AC += binparadecimal(M[PC])
            saida.append(f"AC={AC}")
        elif operacao == "Sub":
            AC -= binparadecimal(M[PC])
            saida.append(f"AC={AC}")
        elif operacao == "Addl":
            aux = binparadecimal(M[PC])
            AC += binparaint(M[aux])
            saida.append(f"AC={AC}")
        elif operacao == "Load":
            n = M[valor]
            AC = binparadecimal(n) if len(n) > 4 else 0
            saida.append(f"AC={AC}")
        elif operacao == "Store":
            M[valor] = format(AC, '016b')
            saida.append(f"Mem({valor})={AC}")
        elif operacao == "Storel":
            aux = binparadecimal(M[PC])
            M[aux] = format(AC, '016b')
            saida.append(f"Mem({aux})={AC}")
        elif operacao == "Input":
            AC = int(input("Digite um número: "))
        elif operacao == "Output":
            saida.append(f"Output={AC}")
        elif operacao == "Jump" or operacao == "Jumpl":
            PC = valor
            incrementar_pc = (operacao != "Jumpl")
            saida.append(f"PC={PC}")
        elif operacao == "Jns":
            M[valor] = format(PC, '016b')
            PC = valor + 1
            incrementar_pc = False
            saida.append(f"PC={PC}")
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
        elif operacao == "Halt":
            saida.append("Halt")
            break
        if incrementar_pc:
            PC += 1
arquivotxt = 'Entrada.txt'
saida = []
M = ['0'] * (2**12)
dadoscomeco=lerarquivo(arquivotxt, M)
decodificador(M, saida,dadoscomeco)

with open('Saida.txt', 'w') as arquivo_saida:
    for linha in saida:
        arquivo_saida.write(linha + '\n')