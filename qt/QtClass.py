from calc.calc import Calculator
from .locals import *
from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox


class MyWidget(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle('')
        self.resize(500, 400)

        self.graphical_env()


    def graphical_env(self) -> None:   # Функция, реализующая графическое окружение
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        self.setCentralWidget(main_widget)
        main_widget.setLayout(main_layout)

        self.input_label = QLabel()
        main_layout.addWidget(self.input_label)

        self.input_fielf = QLineEdit() # Поле ввода
        self.input_fielf.setPlaceholderText('Enter a number')
        main_layout.addWidget(self.input_fielf)

        self.calc_button = QPushButton("Push to calculate") # Кнопка рассчета (привязана к методу calculate)
        self.calc_button.clicked.connect(self.calculate)
        main_layout.addWidget(self.calc_button)

        self.output_label = QLabel("Result:") 
        main_layout.addWidget(self.output_label)

        self.result_field = QTextEdit() # Поле для вывода результата
        self.result_field.setReadOnly(True)
        main_layout.addWidget(self.result_field)

        niz_layout = QHBoxLayout()
        self.language_label = QLabel("Language:")
        niz_layout.addWidget(self.language_label)

        self.lang_box = QComboBox() # Менюшка для выбора языка интерфейса (привязана к change_lang)
        self.lang_box.addItems([
            "English",
            "Русский",
            "Español"
        ])

        self.lang_box.currentIndexChanged.connect(self.change_lang)

        niz_layout.addStretch()
        niz_layout.addWidget(self.lang_box)
        main_layout.addLayout(niz_layout)


    def calculate(self) -> None:    # Фуекция, вызывающая калькулятор (бэкенд)
        text = self.input_fielf.text()

        if not text:
            self.result_field.setText("Please enter a number.")
            return None
        c = Calculator(text)
        res = c.calculate()
        self.result_field.setText(self.format_out(res, c.status))



    def change_lang(self, ind: int) -> None: # функция для смены языка. Как заявлено - без перетрансляции (спасибо фреймворку)
        if ind == 0:
            self.input_label.setText(LOCALS['eng']['inputMessage']) # подтягиваем заранее подготовленный словарь с подписями
            self.calc_button.setText(LOCALS['eng']['StartButtonMessage'])
            self.output_label.setText(LOCALS['eng']['resultMessage'])
            self.language_label.setText(LOCALS['eng']['LangMenu'])
        elif ind == 1:
            self.input_label.setText(LOCALS['ru']['inputMessage'])
            self.calc_button.setText(LOCALS['ru']['StartButtonMessage'])
            self.output_label.setText(LOCALS['ru']['resultMessage'])
            self.language_label.setText(LOCALS['ru']['LangMenu'])
        elif ind == 2:
            self.input_label.setText(LOCALS['sp']['inputMessage'])
            self.calc_button.setText(LOCALS['sp']['StartButtonMessage'])
            self.output_label.setText(LOCALS['sp']['resultMessage'])
            self.language_label.setText(LOCALS['sp']['LangMenu'])
        else:
            raise ValueError("Invalid language index.")


    def format_out(self, res, num_type: str) -> str: # колхоз для удобочитаемого вывода резов
        if len(res) != 0:
            if num_type == 'complex' or num_type == 'negative':
                n1, n2 = str(res[0])[1:-1], str(res[1])[1:-1]
                return f"{n1}\n{n2}"
            else:
                return f"{res[0]}\n{res[1]}"
        else:
            return "No roots found!"
