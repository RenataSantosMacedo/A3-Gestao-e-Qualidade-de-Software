 # **Análise do Código Original - Calculadora**

---

## **Introdução**

O código `my_first_calculator.py` é uma calculadora simples que realiza operações básicas de **adição, subtração, multiplicação e divisão** com números inteiros de 0 a 50.  
O código apresenta diversos problemas de **Clean Code**, incluindo repetição excessiva, falta de modularização, ausência de tratamento de exceções, uso de variáveis com nomes não descritivos e acoplamento elevado.  

---

## **Problemas e Soluções**

---

### **1. REPETIÇÃO EXCESSIVA (DRY Violado)**

O código repete a estrutura `if` para cada combinação possível de operação e números, resultando em centenas de linhas de código redundante.

**Problema:**

```python
if num1 == 0 and operador == '+' and num2 == 0:
    print("0 + 0 = 0")
if num1 == 1 and operador == '+' and num2 == 1:
    print("1 + 1 = 2")
```

**Solução:**

Utilizar uma função que execute a operação de forma centralizada, reduzindo a repetição.

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

Todo o código está em um único bloco, sem funções ou estrutura clara, dificultando a leitura e a reutilização do código.

**Problema:**

```python
print('Welcome to this calculator!')
num1 = int(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
num2 = int(input('Please choose your second number: '))
```

**Solução:**

Separar a lógica em funções específicas para facilitar a manutenção.

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

O código não trata exceções para entradas inválidas ou divisões por zero, o que pode gerar erros em tempo de execução.

**Problema:**

```python
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
```

**Solução:**

Implementar tratamento de exceções com try e except.

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

Variáveis como `sign` e `num1` não são descritivas e não seguem as boas práticas de Clean Code.

**Problema:**

```python
sign = input('What do you want to do? +, -, /, or *: ')
```

**Solução:**

Usar nomes mais claros e consistentes.

```python
operador = input('Escolha a operação (+, -, *, /): ')
```

---

### **5. AUSÊNCIA DE COMENTÁRIOS CLAROS E SIGNIFICATIVOS**

O código possui apenas um comentário genérico e sem contexto útil.

**Problema:**

```python
# TODO: Make it work for all floating point numbers too
```

**Solução:**

Adicionar comentários apenas onde necessário, explicando a intenção do código.

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

O código mistura a lógica das operações com a entrada e saída de dados, dificultando a reutilização.

**Problema:**

```python
print('Welcome to this calculator!')
num1 = int(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
num2 = int(input('Please choose your second number: '))
```

**Solução:**

Separar a lógica das operações e a interação com o usuário em funções distintas.

```python
def executar_calculo(num1, operador, num2):
    resultado = calcular(operador, num1, num2)
    print(f"O resultado de {num1} {operador} {num2} é {resultado}")
```

