from calc.calc import Calculator
from .locals import *
from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox
from typing import Iterable


class MyWidget(QMainWindow):

    start_lang: str

    def __init__(self) -> None:
        super().__init__()

        self.start_lang = 'eng'
        self.subwindow = None

        self.setWindowTitle('')
        self.resize(500, 400)

        self.graphical_env()


    def graphical_env(self) -> None:   # Функция, реализующая графическое окружение
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        verh_layout = QHBoxLayout()

        self.setCentralWidget(main_widget)
        main_widget.setLayout(main_layout)

        self.precision_input = QLineEdit()
        self.precision_input.setPlaceholderText("10") # дефолтное значение
        self.precision_input.setMaximumWidth(80)

        self.pow_label = QLabel("Root degree:")
        self.pow_input = QLineEdit()
        self.pow_input.setPlaceholderText("2") # дефолтное значение
        self.pow_input.setMaximumWidth(80)
        verh_layout.addWidget(self.pow_label)
        verh_layout.addWidget(self.pow_input)

        verh_layout.addStretch()

        self.help_button = QPushButton('Help')
        self.help_button.setStyleSheet('font-size: 13pt')
        self.help_button.setMaximumWidth(120)
        self.help_button.clicked.connect(self.create_subwindow)
        verh_layout.addWidget(self.help_button)

        main_layout.addLayout(verh_layout)
        
        self.input_label = QLabel()
        main_layout.addWidget(self.input_label)

        self.input_fielf = QLineEdit() # Поле ввода
        self.input_fielf.setMinimumHeight(50) # Минимальная высота окошка ввода
        self.input_fielf.setStyleSheet('font-size: 13pt') # Размер шрифта в плейсхолдере
        self.input_fielf.setPlaceholderText('Enter a number')
        main_layout.addWidget(self.input_fielf)

        self.calc_button = QPushButton("Push to calculate") # Кнопка рассчета (привязана к методу calculate)
        self.calc_button.setStyleSheet('font-size: 11pt')
        self.calc_button.setMinimumHeight(40)
        self.calc_button.clicked.connect(self.calculate)
        main_layout.addWidget(self.calc_button)

        self.output_label = QLabel("Result:") 
        self.output_label.setStyleSheet('font-size: 11pt')
        main_layout.addWidget(self.output_label)

        self.result_field = QTextEdit() # Поле для вывода результата
        self.result_field.setReadOnly(True)
        self.result_field.setStyleSheet('font-size: 12pt')
        main_layout.addWidget(self.result_field)

        niz_layout = QHBoxLayout()
        self.language_label = QLabel("Language:")
        self.precision_label = QLabel("Precision:")
        niz_layout.addWidget(self.language_label)

        self.lang_box = QComboBox() # Менюшка для выбора языка интерфейса (привязана к change_lang)
        self.lang_box.addItems([
            "English",
            "Русский",
            "Español",
            "中國人",
        ])

        self.lang_box.currentIndexChanged.connect(self.change_lang)
        niz_layout.addWidget(self.lang_box)

        niz_layout.addStretch()
        niz_layout.addWidget(self.precision_label)
        niz_layout.addWidget(self.precision_input)
        main_layout.addLayout(niz_layout)


    def calculate(self) -> None:    # Фуекция, вызывающая калькулятор (бэкенд)
        text = self.input_fielf.text()
        Pow = self.pow_input.text()

        if not text:
            self.result_field.setText(LOCALS[self.start_lang]['ResultFieldEx']) # заколхозил язык в аттрибут)
            return None
        if self.precision_input.text():
            if Pow:
                c = Calculator(text, Pow, self.precision_input.text())
            else:
                c = Calculator(text, precision=self.precision_input.text())
        else:
            if Pow:
                c = Calculator(text, Pow)
            else:
                c = Calculator(text)

        res = c.calculate()
        self.result_field.setText(self.format_out(res))



    def change_lang(self, ind: int) -> None: # функция для смены языка. Как заявлено - без перетрансляции (спасибо фреймворку)
        if ind == 0:
            self.start_lang = 'eng'

            self.input_label.setText(LOCALS['eng']['inputMessage']) # подтягиваем заранее подготовленный словарь с подписями
            self.calc_button.setText(LOCALS['eng']['StartButtonMessage'])
            self.output_label.setText(LOCALS['eng']['resultMessage'])
            self.language_label.setText(LOCALS['eng']['LangMenu'])
            self.precision_label.setText(LOCALS['eng']['Precision'])
            self.input_fielf.setPlaceholderText(LOCALS['eng']['Spaceholder'])
            self.pow_label.setText(LOCALS['eng']['Pow'])
            self.help_button.setText(LOCALS['eng']['Help'])
        elif ind == 1:
            self.start_lang = 'ru'

            self.input_label.setText(LOCALS['ru']['inputMessage'])
            self.calc_button.setText(LOCALS['ru']['StartButtonMessage'])
            self.output_label.setText(LOCALS['ru']['resultMessage'])
            self.language_label.setText(LOCALS['ru']['LangMenu'])
            self.input_fielf.setPlaceholderText(LOCALS['ru']['Spaceholder'])
            self.precision_label.setText(LOCALS['ru']['Precision'])
            self.pow_label.setText(LOCALS['ru']['Pow'])
            self.help_button.setText(LOCALS['ru']['Help'])
        elif ind == 2:
            self.start_lang = 'sp'

            self.input_label.setText(LOCALS['sp']['inputMessage'])
            self.calc_button.setText(LOCALS['sp']['StartButtonMessage'])
            self.output_label.setText(LOCALS['sp']['resultMessage'])
            self.language_label.setText(LOCALS['sp']['LangMenu'])
            self.input_fielf.setPlaceholderText(LOCALS['sp']['Spaceholder'])
            self.precision_label.setText(LOCALS['sp']['Precision'])
            self.pow_label.setText(LOCALS['sp']['Pow'])
            self.help_button.setText(LOCALS['sp']['Help'])
        elif ind == 3:
            self.start_lang = '中國人'

            self.input_label.setText(LOCALS['中國人']['inputMessage'])
            self.calc_button.setText(LOCALS['中國人']['StartButtonMessage'])
            self.output_label.setText(LOCALS['中國人']['resultMessage'])
            self.language_label.setText(LOCALS['中國人']['LangMenu'])
            self.input_fielf.setPlaceholderText(LOCALS['中國人']['Spaceholder'])
            self.precision_label.setText(LOCALS['中國人']['Precision'])
            self.pow_label.setText(LOCALS['中國人']['Pow'])
            self.help_button.setText(LOCALS['中國人']['Help'])

        else:
            raise ValueError("Invalid language index.")


    def create_subwindow(self) -> None:
        self.subwindow = SubWindow()
        self.subwindow.show()


    def format_out(self, res: Iterable) -> str: # колхоз для удобочитаемого вывода резов
        if type(res) == str:
            return res
        else:
            if len(res) != 0:
                if len(res) == 1:
                    return LOCALS[self.start_lang]['OneRoot'] + f': {res[0]}'
                elif len(res) == 2:
                    n1, n2 = str(res[0]).replace('j', 'i').strip('()'), str(res[1]).replace('j', 'i').strip('()')
                    return LOCALS[self.start_lang]['FRoot'] + n1 + '\n' + LOCALS[self.start_lang]['SecRoot'] + n2
                else:
                    counter = 0
                    out = ''
                    for root in res:
                        counter += 1
                        out += f'{LOCALS[self.start_lang]['OneRoot']} №{counter}: {root}\n'
                    return out
            else:
                return LOCALS[self.start_lang]['NoRoots']


class SubWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Help")
        self.resize(300, 200)

        layout = QVBoxLayout()
        sub_label = QLabel("\t\t\tThis is our technical support page.\nIf you need some help (e.g. language addition), you can contact us using this email:\n\n\t\t\tvasilina.polushvaiko@yandex.ru")
        sub_label.setStyleSheet('font-size: 17pt')
        layout.addWidget(sub_label)

        self.setLayout(layout)

        