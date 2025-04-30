def lerarquivo(nomearquivo, M):
    with open(nomearquivo, 'r') as arquivo:
        linhas = [linha.strip().replace(' ', '') for linha in arquivo if linha.strip()]
    i = 0
    haltencontrado = False
    for linha in linhas:
        M[i] = linha
        if linha == "0111":
            haltencontrado = True
            i += 1
            break
        i += 1
    enderecodado = i
    for linha in linhas[i:]:
        M[enderecodado] = linha
        enderecodado += 1
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
def decodificador(M, saida):
    AC = 0
    PC = 0
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

        if operacao == "Add":
            AC += binparadecimal(M[PC])
        elif operacao == "Sub":
            AC -= binparadecimal(M[PC])
        elif operacao == "Addl":
            aux = binparadecimal(M[PC])
            AC += binparaint(M[aux])
        elif operacao == "Load":
            n = M[valor]
            AC = binparadecimal(n) if len(n) > 4 else 0
        elif operacao == "Store":
            M[valor] = format(AC, '016b')
            saida.append(f"Mem({valor})={AC}")
        elif operacao == "Storel":
            aux = binparadecimal(M[PC])
            M[aux] = format(AC, '016b')
            saida.append(f"Mem({aux})={AC}")
        elif operacao == "Input":
            AC = int(input(""))
        elif operacao == "Output":
            saida.append(f"Saida={AC}")
        elif operacao == "Jump" or operacao == "Jumpl":
            PC = valor
            incrementar_pc = (operacao != "Jumpl")
        elif operacao == "Jns":
            M[valor] = format(PC, '016b')
            PC = valor + 1
            incrementar_pc = False
        elif operacao == "LoadImmi":
            AC = valor
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
        saida.append(f"AC={AC}")
        if incrementar_pc:
            PC += 1
arquivotxt = 'Entrada.txt'
saida = []
M = ['0'] * (2**12)
lerarquivo(arquivotxt, M)
decodificador(M, saida)

with open('Saida.txt', 'w') as arquivo_saida:
    for linha in saida:
        arquivo_saida.write(linha + '\n')
