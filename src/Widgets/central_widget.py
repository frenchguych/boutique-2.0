from typing import List
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QLabel, QLayout, QScrollArea, QVBoxLayout, QWidget

from Widgets.card import Card


class CentralWidget(QScrollArea):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        self.createComponents()

    def createComponents(self) -> None:
        self.scroll_widget_layout = QVBoxLayout()

        self.scroll_widget = QWidget(self)
        self.scroll_widget.setLayout(self.scroll_widget_layout)

        self.setWidgetResizable(True)
        self.setWidget(self.scroll_widget)
        #self.setBackgroundRole(QPalette.Light)

    # def clear(self) -> None:
    #     while self.scroll_widget_layout.count():
    #         item = self.scroll_widget_layout.takeAt(0)
    #         if item and item.widget():
    #             item.widget().deleteLater()
    #             self.scroll_widget_layout.removeWidget(item.widget())

    # def addCard(self, widget: Card) -> None:
    #     widget.setParent(self.scroll_widget)
    #     self.scroll_widget_layout.addWidget(widget)

    # def addStretch(self) -> None:
    #     self.scroll_widget_layout.addStretch()

    def addCards(self, cards: List[Card]) -> None:
        while self.scroll_widget_layout.count():
            item = self.scroll_widget_layout.takeAt(0)
            if item and item.widget():
                item.widget().deleteLater()
                self.scroll_widget_layout.removeWidget(item.widget())
        for card in cards:
            self.scroll_widget_layout.addWidget(card)
        self.scroll_widget_layout.addStretch()
