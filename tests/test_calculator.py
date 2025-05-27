# Testes unitários para a classe Calculator
# Utiliza mocks para simular a interface do usuário e verificar o comportamento da calculadora

# Importa as bibliotecas necessárias
import unittest
from unittest.mock import Mock
from core.calculator import Calculator

class TestCalculatorWithMocks(unittest.TestCase):

    def setUp(self):
        # Cria funções mockadas para simular a UI
        self.mock_update = Mock()
        self.mock_clear = Mock()
        self.calc = Calculator(self.mock_update, self.mock_clear)

    def test_addition(self):
        # Testa a soma
        self.calc.expression = "10+5"
        result = self.calc.evaluate_expression()
        self.assertEqual(result, "15")  # Espera-se 15 como resultado

    def test_subtraction(self):
        # Testa a subtração
        self.calc.expression = "10-5"
        result = self.calc.evaluate_expression()
        self.assertEqual(result, "5")

    def test_multiplication(self):
        # Testa a multiplicação
        self.calc.expression = "4*3"
        result = self.calc.evaluate_expression()
        self.assertEqual(result, "12")

    def test_division(self):
        # Testa a divisão 
        self.calc.expression = "12/4"
        result = self.calc.evaluate_expression()
        self.assertEqual(result, "3.0")  # float esperado

    def test_division_by_zero(self):
        # Testa divisão por zero e deve acionar erro
        self.calc.expression = "5/0"
        self.calc.input('=')  # Ao pressionar '=', deve avaliar a expressão
        self.assertTrue(self.calc.onError)  # Deve estar em estado de erro
        self.mock_update.assert_called_with("Error")  # Display deve mostrar "Error"

    def test_power(self):
        # Testa operador de potência usando símbolo ^ que vira **
        self.calc.expression = "2^3"
        result = self.calc.evaluate_expression()
        self.assertEqual(result, "8")

    def test_square_root(self):
        # Testa raiz quadrada
        self.calc.expression = "9"
        self.calc.isSquareRoot = True
        result = self.calc.evaluate_expression()
        self.assertEqual(result, "3.0")

    def test_clear_expression_resets_state(self):
        # Testa se clear zera expressão e chama a função de limpar
        self.calc.expression = "99+1"
        self.calc.clear_expression()
        self.assertEqual(self.calc.expression, "")
        self.mock_clear.assert_called_once()

    def test_input_adds_to_expression(self):
        # Testa se input normal atualiza expressão e chama update da UI
        self.calc.input('7')
        self.assertEqual(self.calc.expression, "7")
        self.mock_update.assert_called_with("7")

    def test_input_equal_triggers_evaluation(self):
        # Testa se '=' avalia a expressão e atualiza a UI
        self.calc.expression = "6*6"
        self.calc.input('=')
        self.assertEqual(self.calc.expression, "36")
        self.mock_update.assert_called_with("36")

    def test_input_clears_expression(self):
        # Testa input 'C', que limpa expressão e chama a UI
        self.calc.expression = "7+3"
        self.calc.input('C')
        self.assertEqual(self.calc.expression, "")
        self.mock_clear.assert_called_once()

    def test_backspace_removes_last_char(self):
        # Testa se backspace apaga último caractere corretamente
        self.calc.expression = "123"
        self.calc.backspace()
        self.assertEqual(self.calc.expression, "12")
        self.mock_update.assert_called_with("12")

    def test_can_add_decimal_only_once_per_number(self):
        # Testa se segundo ponto decimal é ignorado na mesma parte do número
        self.calc.input('1')
        self.calc.input('.')
        self.calc.input('5')
        self.calc.input('.')
        self.assertEqual(self.calc.expression, "1.5")  # Segundo '.' é ignorado

    def test_cannot_start_with_secondary_operator(self):
        # Testa se operador como '*' não pode iniciar expressão
        can_add = self.calc.canAddThisInput('*')
        self.assertFalse(can_add)

    def test_can_start_with_primary_operator_after_sqrt(self):
        # Testa se pode adicionar '+' depois de '√' como primeiro caractere
        self.calc.expression = "√9"
        can_add = self.calc.canAddThisInput('+')
        self.assertTrue(can_add)

    def test_expression_ending_with_operator_is_not_evaluable(self):
        # Testa se expressão terminando com operador não pode ser avaliada
        self.calc.expression = "7+"
        self.assertFalse(self.calc.can_evaluate())

    def test_expression_with_only_number_is_not_evaluable(self):
        # Testa se expressão sem operadores não é avaliada
        self.calc.expression = "7"
        self.assertFalse(self.calc.can_evaluate())

    def test_valid_expression_can_be_evaluated(self):
        # Testa se expressão correta é considerada válida para avaliação
        self.calc.expression = "8+2"
        self.assertTrue(self.calc.can_evaluate())

if __name__ == "__main__":
    unittest.main()

# Este código é um exemplo de testes unitários para a classe Calculator.
# Ele utiliza mocks para simular a interface do usuário e verificar o comportamento da calculadora sem depender de uma UI real.
# Os testes cobrem operações básicas, tratamento de erros e manipulação de expressões.