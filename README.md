# Interpretador MARIE

Este projeto é um interpretador para a linguagem de máquina MARIE, que executa programas escritos no formato binário. O código implementa a execução de um programa simples, com a capacidade de ler instruções a partir de um arquivo de entrada, processá-las e gerar uma saída.

## Estrutura do Código

O código está dividido em várias funções que trabalham em conjunto para decodificar e executar um programa em MARIE.

### Funções principais

1. **`lerarquivo(nomearquivo, M)`**:
   - Lê um arquivo binário de entrada (`nomearquivo`) e carrega as instruções na memória (`M`).
   - A leitura é feita linha por linha, removendo espaços e linhas vazias.
   - A execução começa após o comando "Halt" (instrução "0111").
   - Retorna o índice de onde os dados começam na memória.

2. **`binparaint(binario)`**:
   - Converte uma string binária em um número inteiro.

3. **`binprastr(binario)`**:
   - Converte uma string binária em uma string.

4. **`obteroperacao(binario)`**:
   - Recebe uma string binária (primeiros 4 bits da instrução) e retorna a operação correspondente em formato textual (por exemplo, "Load", "Add", etc.).

5. **`binparadecimal(binstr)`**:
   - Extrai os últimos 12 bits de uma string binária de 16 bits e converte para um número decimal.

6. **`decodificador(M, saida, dadoscomeco)`**:
   - Função principal que executa o programa na memória.
   - Interpreta as instruções e executa operações como Load, Store, Add, Sub, etc.
   - Modifica o acumulador (`AC`) e o contador de programa (`PC`) conforme as instruções.
   - Adiciona a saída gerada a uma lista de `saida` que será posteriormente salva em um arquivo.
   - Caso a instrução "Halt" seja encontrada, a execução é interrompida.

### Estrutura da Memória

A memória é modelada como uma lista de 4096 posições, com valores binários de 16 bits (representando as instruções e dados). A função `lerarquivo` carrega o arquivo de entrada nessa memória, e o interpretador manipula essa memória conforme as instruções.

### Arquivo de Entrada

O arquivo de entrada deve ser um arquivo de texto com cada linha representando uma instrução ou dado. As instruções são de 16 bits, e os dados são armazenados após a instrução "Halt" (com código `0111`).

**Exemplo de entrada**:

0001 000000000010 0011 000000000011 0010 000000000100 0111 0000000000000010 0000000000000011 0000000000000000

Cada instrução é composta por 16 bits, com os primeiros 4 bits representando a operação, e os 12 bits restantes representando o operando (endereço ou valor imediato).

### Arquivo de Saída

A saída do interpretador é salva em um arquivo chamado `Saida.txt`. Cada linha contém o resultado de uma operação executada. **Exemplo de saída**:

AC=10 AC=5 Mem(2)=10 AC=15 Mem(3)=5 ... Halt

### Como Usar

1. Prepare um arquivo de entrada com instruções e dados no formato binário.
2. Salve o arquivo como `Entrada.txt` no mesmo diretório do script.
3. Execute o script Python.
4. O interpretador irá processar o arquivo de entrada e gerar uma saída no arquivo `Saida.txt`.

### Requisitos

- Python 3.x
- O arquivo de entrada deve estar no formato correto (instruções binárias de 16 bits).

### 2. Criar o arquivo `Entrada.txt`

Este arquivo deve conter:

- Instruções MARIE em binário (uma por linha).
- A instrução `0111` (Halt) indicando o fim do código.
- Após o `0111`, coloque os dados (em binário) que serão utilizados pela memória.

#### Exemplo de conteúdo:

0010000000000100 0011000000000101 0100000000000110 0111 0000000000000011 0000000000000010 0000000000000001

### 3. Executar o programa

Abra o terminal e rode o interpretador com o comando:

```bash
python interpretador.py

Após a execução, o arquivo Saida.txt será criado com a saída do programa. Exemplo:

AC=3
AC=5
AC=2
Halt
