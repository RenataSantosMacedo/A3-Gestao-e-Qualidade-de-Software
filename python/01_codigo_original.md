 # **Análise do Código Original - Calculadora**

---

## **Introdução**

O código `my_first_calculator.py` é uma calculadora simples que realiza operações básicas de **adição, subtração, multiplicação e divisão** com números inteiros de 0 a 50.  
O código apresenta diversos problemas de **Clean Code**, incluindo repetição excessiva, falta de modularização, ausência de tratamento de exceções, uso de variáveis com nomes não descritivos e acoplamento elevado.  

---

## **Problemas e Soluções**

---

### **1. REPETIÇÃO EXCESSIVA (DRY Violado)**

**Conceito:**  
O princípio **DRY** (Don't Repeat Yourself) é uma boa prática de programação que diz que **não devemos repetir código**. Repetições no código dificultam a manutenção e aumentam o risco de erros. Quando há muita repetição, o código se torna mais difícil de entender e alterar.

**Problema:**  
No código original, a estrutura `if` foi repetida várias vezes para cada combinação possível de operação e números, resultando em código redundante.

```python
if num1 == 0 and operador == '+' and num2 == 0:
    print("0 + 0 = 0")
if num1 == 1 and operador == '+' and num2 == 1:
    print("1 + 1 = 2")
```

**Solução:**
Criamos uma função centralizada que realiza as operações matemáticas de forma simplificada e sem repetição. A lógica de cada operação é feita em um único lugar, o que melhora a legibilidade e facilita manutenções futuras.

```python
def calcular(operador, num1, num2):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        return num1 / num2 if num2 != 0 else "Erro: Divisão por zero"

print(calcular('+', 1, 1))
print(calcular('*', 2, 3))
```

---

### **2. FALTA DE MODULARIZAÇÃO**

**Conceito:**
Modularização refere-se ao processo de dividir o código em blocos menores e independentes, chamados de funções ou métodos, que realizam tarefas específicas. Isso facilita a leitura, manutenção e reutilização do código.

**Problema:**
Todo o código estava em um único bloco, sem funções, o que dificultava a leitura e a reutilização.

```python
print('Welcome to this calculator!')
num1 = int(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
num2 = int(input('Please choose your second number: '))
```

**Solução:**
Organizamos o código em funções, para que cada parte da lógica tivesse uma responsabilidade específica, facilitando a manutenção e a expansão do código.

```python
def exibir_mensagem_inicial():
    print("Bem-vindo à calculadora!")

def obter_entrada():
    num1 = int(input('Digite o primeiro número: '))
    operador = input('Escolha a operação (+, -, *, /): ')
    num2 = int(input('Digite o segundo número: '))
    return num1, operador, num2

exibir_mensagem_inicial()
numero1, operacao, numero2 = obter_entrada()
```

---

### **3. AUSÊNCIA DE TRATAMENTO DE EXCEÇÕES**

**Conceito:**
O tratamento de exceções é uma prática que permite que o código lide com erros (exceções) de forma controlada, evitando que o programa trave ou falhe inesperadamente.

**Problema:**
O código não possuía nenhum mecanismo para lidar com entradas inválidas (como quando o usuário não digita um número) ou com erros de execução, como a tentativa de divisão por zero.

```python
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
```

**Solução:**
Adicionamos tratamento de exceções com try e except para garantir que o código só continue a execução se os valores fornecidos forem válidos, e que erros sejam tratados de maneira apropriada.

```python
def obter_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: Digite um número válido.")

num1 = obter_numero('Digite o primeiro número: ')
num2 = obter_numero('Digite o segundo número: ')
```

---

### **4. USO DE NOMES NÃO DESCRITIVOS**

**Conceito:**
Nomes descritivos ajudam a entender facilmente o propósito de variáveis e funções. Quando os nomes são vagos ou genéricos, o código se torna mais difícil de ler e manter.

**Problema:**
Variáveis como sign e num1 não eram claras o suficiente sobre o seu propósito.

```python
sign = input('What do you want to do? +, -, /, or *: ')
```

**Solução:**
Renomeamos as variáveis para nomes mais descritivos e consistentes, facilitando o entendimento de seu propósito.

```python
operador = input('Escolha a operação (+, -, *, /): ')
```

---

### **5. AUSÊNCIA DE COMENTÁRIOS CLAROS E SIGNIFICATIVOS**

**Conceito:**
Comentários são importantes para explicar o propósito do código ou de uma função específica, especialmente quando o código não é imediatamente óbvio.

**Problema:**
O código original possuía apenas um comentário genérico que não esclarecia a intenção do código.

```python
# TODO: Make it work for all floating point numbers too
```

**Solução:**
Adicionamos comentários claros e significativos, explicando a lógica por trás das funções e processos mais complexos, sem sobrecarregar o código com explicações desnecessárias.

```python
# Função para executar as operações básicas
def calcular(operador, num1, num2):
    try:
        if operador == '+':
            return num1 + num2
        elif operador == '-':
            return num1 - num2
        elif operador == '*':
            return num1 * num2
        elif operador == '/':
            return num1 / num2 if num2 != 0 else "Erro: Divisão por zero"
    except Exception as e:
        return f"Erro ao calcular: {e}"
```

---

### **6. ACOPLAMENTO ELEVADO**

**Conceito:**
Acoplamento refere-se ao grau em que diferentes partes do código dependem umas das outras. Acoplamento elevado torna o código difícil de testar e modificar. Idealmente, as partes do código devem ser independentes.

**Problema:**
A lógica das operações estava misturada com a entrada e saída de dados, o que tornava a modificação e o teste do código mais difíceis.

```python
print('Welcome to this calculator!')
num1 = int(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
num2 = int(input('Please choose your second number: '))
```

**Solução:**
Separando a lógica das operações e a interação com o usuário em funções distintas, conseguimos reduzir o acoplamento, tornando o código mais modular e facilitando a manutenção.

```python
def executar_calculo(num1, operador, num2):
    resultado = calcular(operador, num1, num2)
    print(f"O resultado de {num1} {operador} {num2} é {resultado}")
```

