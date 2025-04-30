def lerarquivo(nomearquivo, M):
    with open(nomearquivo, 'r') as arquivo:
        i = 0
        for linha in arquivo:
            linhalimpa = linha.strip()
            linhalimpa = linhalimpa.replace(' ', '')
            if linhalimpa:
                M[i] = linhalimpa
            i += 1
def binparaint (binario):
        return int(binario, 2)
def binprastr (binario):
    return str(binario)
def add(valor,AC,M,saida):
    AC += M[valor]
    saida.append(f"AC={AC}")
    return AC
def sub(valor,AC):
    AC-=valor
    saida.append(f"AC={AC}")
    return AC
def addl(valor,AC,M,saida):
    aux = M[valor]
    AC+=M[aux]
    saida.append(f"AC={AC}")
    return AC
def load(valor,AC,M,saida):
    AC = M[valor]
    saida.append(f"AC={AC}")
    return AC

def obteroperacao (binario):
    if binario=="0000":
        return "Jns"
    elif binario=="0001":
        return "Load"
    elif binario=="0010":
        return "Store"
    elif binario=="0011":
        return "Add"
    elif binario=="0100":
        return "Sub"
    elif binario=="0101":
        return "Input"
    elif binario=="0110":
        return "Output"
    elif binario=="0111":
        return "Halt"
    elif binario=="1000":
        return "Skipcond"
    elif binario=="1001":
        return "Jump"
    elif binario=="1010":
        return "LoadImmi"
    elif binario=="1011":
        return "Addl"
    elif binario=="1100":
        return "Jumpl"
    elif binario=="1101":
        return "Loadl"
    elif binario=="1110":
        return "Storel"
    else:
        return "Error"


def decodificador(M,saida):
    AC=0
    PC=0
    tamanhodamemoria=len(M)
    while tamanhodamemoria>PC:
        strbin=(str(M[PC]))
        opbin=strbin[:4]
        restobin=None
        restobin=strbin[4:]
        operacao=obteroperacao(opbin)
        if restobin !="":
            valor=binparaint(restobin)
        incrementar_pc = True
        print(M)
        print(restobin)
        print(valor)
        if operacao=="Add":
            AC += binparaint(int(M[int(valor)]))
            saida.append(f"AC={AC}")
        elif operacao=="Sub":
            AC -= binparaint(int(M[int(valor)]))
            saida.append(f"AC={AC}")
        elif operacao=="Addl":
            aux = binparaint(int(M[valor]))
            AC += binparaint(M[aux])
            saida.append(f"AC={AC}")
        elif operacao=="Load":
            AC = binparaint(M[valor])
            saida.append(f"AC={AC}")
        elif operacao=="Halt":
            saida.append(f"Halt")
            break
        elif operacao=="Store":
            M[valor] = str(AC)
            saida.append(f"Mem({valor})={AC}")
        elif operacao=="Storel":
            aux = binparaint(M[valor])
            M[aux] = str(AC)
            saida.append(f"Mem({aux})={AC}")
        elif operacao=="Input":
            AC=int(input())
            saida.append(f"AC={AC}")
        elif operacao=="Output":
            saida.append(f"AC={AC}")
        elif operacao=="Jump":
            PC = valor
            incrementar_pc = False
            saida.append(f"PC={PC}")
        elif operacao=="Jumpl":
            PC = binparaint([valor])
            incrementar_pc = False
            saida.append(f"PC={PC}")
        elif operacao=="Jns":
            M[valor] = str(PC)
            incrementar_pc = False
            PC= valor + 1
            saida.append(f"M[{valor}]={M[valor]}")
        elif operacao=="LoadImmi":##clear
            if valor!="":
                AC = valor
            else:
                AC= 0
            saida.append(f"AC={AC}")
        elif operacao == "Skipcond":
            if valor == 0:
                if AC < 0:
                    PC += 1
            elif valor == 1024:
                if AC == 0:
                    PC += 1
            elif valor == 2048:
                if AC > 0:
                    PC += 1
            elif valor == 3072:
                if AC != 0:
                    PC += 1
            saida.append(f"PC={PC}")
        if incrementar_pc:
            PC += 1

arquivotxt='Entrada.txt'
saida=[]
M = ['0'] * (2**12)
lerarquivo(arquivotxt,M)
decodificador(M,saida)
with open('Saida.txt', 'w') as arquivo_saida:
    for linha in saida:
        arquivo_saida.write(linha + '\n')
