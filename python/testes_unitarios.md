# **Documentação Testes Unitários** 

---

# **Finalidade dos Testes**

Os testes unitários tem como finalidade a verificação do comportamento funcional da classe `Calculator`, para certificar que todas as operações matemáticas e interações com a interface gráfica (através de funções mockadas) estejam funcionando corretamente. Neste sentido, os testes em questão tem o objetivo de amparar as seguintes funcionalidades da classe `Calculator`:

● Avaliação de expressões matemáticas;

● Verificação de operadores válidos;

● Simulação de interações com a interface (UI) usando funções mockadas;

● Manipulação da expressão inserida (input, clear, backspace); e

● Comportamento em casos de erro (ex: divisão por zero).

---

# **Meios Utilizados**

Foram utilizados as ferramentas Python `unittest` e `unittest.mock` (para simular as funções de interface gráfica).

---

# **Configuração Inicial**

Cada teste cria instâncias mockadas de `update_display` e `clear_display`, que são inseridas na classe `Calculator`:

```python
self.mock_update = Mock()
self.mock_clear = Mock()
self.calc = Calculator(self.mock_update, self.mock_clear)
``` 

---

# **Principais Casos de Testes**

● `test_addition`, `test_subtraction` (Testam operações básicas de soma e subtração);

● `test_multiplication`, `test_division` (Comprovam multiplicação e divisão com resultados corretos);

● `test_division_by_zero` (Assegura que a divisão por zero retorna "Error" e ativa o estado de erro);

● `test_power` (sta a operação de potência com símbolo ^ interpretado como **); e

● `test_square_root` (	Avalia raiz quadrada com `isSquareRoot = True`).

---

# **Testes de Lógica de Entrada**

● `test_input_adds_to_expression` (Verifica se a expressão é atualizada com o caractere inserido);

● `test_input_equal_triggers_evaluation` (Avalia a expressão ao pressionar o botão = e verifica o resultado);

● `test_input_clears_expression` (Testa se o botão C limpa a expressão e chama o método de limpeza da UI);

● `test_backspace_removes_last_char` (Verifica se o último caractere da expressão é removido); e

● `test_can_add_decimal_only_once_per_number` (Certifica que apenas um ponto decimal pode ser inserido por número).

---

# **Testes de Validação de Expressão**

● `test_cannot_start_with_secondary_operator` (Impede que a expressão comece com operadores inválidos como *, / ou ^);

● `test_can_start_with_primary_operator_after_sqrt` (Permite iniciar com um operador primário (+, -) após √);

● `test_expression_ending_with_operator_is_not_evaluable` (Impede avaliação se a expressão terminar com um operador (ex: 5+));

● `test_expression_with_only_number_is_not_evaluable` (Uma expressão com apenas número não deve ser considerada "avaliável"); e

● `test_valid_expression_can_be_evaluated` (Confirma que uma expressão completa (como 2+3) pode ser avaliada).

---

# **Resultados e Conclusão**

● **Todos os 18 testes foram realizados com sucesso**

```
Ran 18 tests in 0.014s
OK
```

● O módulo Calculator está corretamente isolado e testado, além disso, destaca-se que o Mocking foi essencial para validar a integração indireta com a interface gráfica. Isto posto, o código segue boas práticas como Inversão de Dependência, TDD e cobertura de erros.


