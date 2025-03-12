
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTextEdit, QHBoxLayout, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont
from lexer import analizador_lexico
from syntax import analizador_sintactico
from semantic import analizador_semantico

class ExpressionAnalyzer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Analizador de Expresiones")
        self.setGeometry(100, 100, 800, 600)

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.setStyleSheet("background-color: #f8f9fa; font-family: Arial, sans-serif; font-size: 18px;")

        self.grammar_label = QLabel("<b>Gramática:</b><br>EXP -> EXP + TERM | EXP - TERM | TERM<br>TERM -> TERM * FACTOR | TERM / FACTOR | FACTOR<br>FACTOR -> EXP | NUMBER", self)
        self.grammar_label.setStyleSheet("color: #343a40; font-size: 18px;")
        self.grammar_label.setFont(QFont('Arial', 12))

        self.label = QLabel("Ingresa la expresión:", self)
        self.label.setStyleSheet("color: #343a40; font-size: 18px;")
        self.label.setFont(QFont('Arial', 14))

        self.input = QLineEdit(self)
        self.input.setPlaceholderText("Expresion")
        self.input.setStyleSheet("""
            font-size: 16px;
            padding: 10px;
            border: 2px solid #6c757d;
            border-radius: 8px;
            background-color: #e9ecef;
            color: #343a40;
        """)
        self.input.setFont(QFont('Arial', 14))

        # enter
        self.input.returnPressed.connect(self.start_analysis)

        self.button = QPushButton("Analizar", self)
        self.button.setStyleSheet("""
            background-color: #6c757d;
            color: #ffffff;
            padding: 10px;
            border-radius: 8px;
            font-size: 16px;
        """)
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: #ffffff;
                padding: 10px;
                border-radius: 8px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #5a6268;  /* Un poco más oscuro cuando pasa el mouse */
            }
            QPushButton:pressed {
                background-color: #495057;  /* Aún más oscuro cuando se hace clic */
            }
        """)
        self.button.clicked.connect(self.start_analysis)

        self.reset_button = QPushButton("Resetear", self)
        self.reset_button.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: #ffffff;
                padding: 10px;
                border-radius: 8px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #5a6268;  /* Un poco más oscuro cuando pasa el mouse */
            }
            QPushButton:pressed {
                background-color: #495057;  /* Aún más oscuro cuando se hace clic */
            }
        """)
        self.reset_button.clicked.connect(self.reset_fields)

        self.result = QTextEdit(self)
        self.result.setReadOnly(True)
        self.result.setStyleSheet("""
            font-size: 20px;
            padding: 10px;
            border: 2px solid #6c757d;
            border-radius: 8px;
            background-color: #e9ecef;
            color: #343a40;
        """)
        self.result.setFont(QFont('Arial', 14))

        main_layout = QVBoxLayout()
        input_layout = QHBoxLayout()
        button_layout = QHBoxLayout()

        main_layout.addWidget(self.grammar_label)  # Colocado en la parte superior
        input_layout.addWidget(self.label)
        input_layout.addWidget(self.input)

        button_layout.addWidget(self.button)
        button_layout.addWidget(self.reset_button)

        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.result)

        self.setLayout(main_layout)

#  -------------------- analizer starter --------------------
    def start_analysis(self):
        expr = self.input.text() # read the expresion
        if not expr:
            self.result.setText("Por favor, ingresa una expresión.")
            return

        self.result.clear()
        self.show_lexical_analysis(expr)

    def show_lexical_analysis(self, expr):
        self.result.append("Análisis Léxico...")
        QTimer.singleShot(1500, lambda: self.check_lexical_analysis(expr))

    def check_lexical_analysis(self, expr):
        lexical_result = analizador_lexico(expr)
        if "Error léxico" in lexical_result:
            self.result.append(f"<span style='color: #dc3545;'>{lexical_result} ❌</span>")
        else:
            self.result.append("<span style='color: #28a745;'>Análisis Léxico... Correcto. ✅</span>")
            self.show_syntactic_analysis(expr)

    def show_syntactic_analysis(self, expr):
        self.result.append("Análisis Sintáctico...")
        QTimer.singleShot(1500, lambda: self.check_syntactic_analysis(expr))

    def check_syntactic_analysis(self, expr):
        syntactic_result = analizador_sintactico(expr)
        if "Error sintáctico" in syntactic_result:
            self.result.append(f"<span style='color: #dc3545;'>{syntactic_result} ❌</span>")
        else:
            self.result.append("<span style='color: #28a745;'>Análisis Sintáctico... Correcto. ✅</span>")
            self.show_semantic_analysis(expr)

    def show_semantic_analysis(self, expr):
        self.result.append("Análisis Semántico...")
        QTimer.singleShot(1500, lambda: self.check_semantic_analysis(expr))

    def check_semantic_analysis(self, expr):
        try:
            result = analizador_semantico(expr)
            self.result.append("<span style='color: #28a745;'>Análisis Semántico... Correcto. ✅</span>")
            self.result.append(f"<p style='color: #343a40; font-size: 24px; font-weight: bold;'>Resultado de la expresión: {result}</p>")
        except Exception as e:
            self.result.append(f"<span style='color: #dc3545;'> {str(e)} ❌</span>")

    def reset_fields(self):
        self.input.clear()
        self.result.clear()

# main
def main():
    app = QApplication(sys.argv)
    window = ExpressionAnalyzer()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
