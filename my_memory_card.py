#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QButtonGroup,
QHBoxLayout, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QGroupBox)
app=QApplication([])
btn_OK = QPushButton('Ответить')
main_win=QWidget()
main_win.setWindowTitle('')
lb_Question = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox =  QGroupBox('Результаты теста')
lb_Results = QLabel('Прав ты или нет?')
lb_Correct = QLabel('Ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Results, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_results():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

from random import shuffle, randint

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Results.setText(res)
    show_results()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
    print('add',window.score/window.total*100)

def next_questions():
    window.total += 1
    cur_question = randint(0,len(questions_list)-1)
    q = questions_list[cur_question]
    ask(q)
    
def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_questions()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')

window.total = 0
window.score = 0 

cur_question = -1
#btn_OK.clicked.connect(click_OK)


questions_list = []
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
questions_list.append(Question('Государственный язык Беларуси', 'Беларуский', 'Русский', 'Польский', 'Испанский'))

btn_OK.clicked.connect(click_OK)
next_questions()
window.show()
app.exec_()
