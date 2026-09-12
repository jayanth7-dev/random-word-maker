from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout
)
from random import choice


# Main App Objects and Settings
app = QApplication([])

main_window = QWidget()
main_window.setWindowTitle("Random Word Maker")
main_window.resize(600, 300)


# Create all App Objects
title = QLabel("Random Keywords")

text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")


button1 = QPushButton("Click Me")
button2 = QPushButton("Click Me")
button3 = QPushButton("Click Me")


# Words
my_words = [
    "Galaxy",
    "Thunder",
    "Apple",
    "Mountain",
    "Dragon",
    "Ocean",
    "Shadow",
    "Rocket",
    "Forest",
    "Diamond",
    "Coffee",
    "Tiger",
    "Rainbow",
    "Volcano",
    "Mystery",
    "Lantern",
    "Penguin",
    "Castle",
    "Desert",
    "Robot",
    "Moon",
    "Wizard",
    "Firefly",
    "River",
    "Storm",
    "Butterfly",
    "Crystal",
    "Pirate",
    "Sunset",
    "Compass"
]


# Layouts
master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()


row1.addWidget(title, alignment=Qt.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)


master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)


# Functions
def random_word(label):
    label.setText(choice(my_words))


# Events
button1.clicked.connect(lambda: random_word(text1))
button2.clicked.connect(lambda: random_word(text2))
button3.clicked.connect(lambda: random_word(text3))


# Run App
main_window.show()
app.exec_()
