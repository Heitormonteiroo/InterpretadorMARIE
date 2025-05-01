# InterpretadorMARIE
Este projeto é um interpretador para a linguagem de máquina MARIE, que executa programas escritos no formato binário. O código implementa a execução de um programa simples, com a capacidade de ler instruções a partir de um arquivo de entrada, processá-las e gerar uma saída.

Estrutura do Código
O código está dividido em várias funções que trabalham em conjunto para decodificar e executar um programa em MARIE.

Funções principais
lerarquivo(nomearquivo, M):

Lê um arquivo binário de entrada (nomearquivo) e carrega as instruções na memória (M).

A leitura é feita linha por linha, removendo espaços e linhas vazias.

A execução começa após o comando "Halt" (instrução "0111").

Retorna o índice de onde os dados começam na memória.

binparaint(binario):

Converte uma string binária em um número inteiro.

binprastr(binario):

Converte uma string binária em uma string.

obteroperacao(binario):

Recebe uma string binária (primeiros 4 bits da instrução) e retorna a operação correspondente em formato textual (por exemplo, "Load", "Add", etc.).

binparadecimal(binstr):

Extrai os últimos 12 bits de uma string binária de 16 bits e converte para um número decimal.

decodificador(M, saida, dadoscomeco):

Função principal que executa o programa na memória.

Interpreta as instruções e executa operações como Load, Store, Add, Sub, etc.

Modifica o acumulador (AC) e o contador de programa (PC) conforme as instruções.

Adiciona a saída gerada a uma lista de saida que será posteriormente salva em um arquivo.

Caso a instrução "Halt" seja encontrada, a execução é interrompida.

Estrutura da Memória
A memória é modelada como uma lista de 4096 posições, com valores binários de 16 bits (representando as instruções e dados). A função lerarquivo carrega o arquivo de entrada nessa memória, e o interpretador manipula essa memória conforme as instruções.
