import tkinter as tk
from tkinter import messagebox
import model
import view

class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.model = model.Model()
        self.view = view.View(self.root)
        self.current_player = 'O'
        for x in range(3):
            for y in range(3):
                self.view.board_labels[x][y].bind(
                    '<Button>',
                    lambda e, x=x, y=y: self.label_click(x, y)
                )

    def update_board(self):
        for x in range(3):
            for y in range(3):
                text = self.model.get_player(x, y)
                if text is None:
                    text = '_'
                self.view.board_labels[x][y].config(text=text)

    def label_click(self, x, y):
        try:
            self.model.place(self.current_player, x, y)
        except ValueError:
            return
        self.update_board()
        winner = self.model.check_winner()
        msg = ''
        if winner in ['O', 'X']:
            msg = '플레이어 %s가 이겼습니다!' % self.current_player
        elif winner == model.DRAW:
            msg = '비겼습니다.'

        if winner != model.UNDEFINED:
            replay = messagebox.askyesno('게임 종료',
                                         msg + '\n다시 하시겠습니까?')
            if replay:
                self.current_player = 'O'
                self.model.clear()
                self.update_board()
            else:
                quit()
        else:
            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def run(self):
        self.root.title('틱텍토 게임')
        self.root.geometry('450x450')
        self.root.mainloop()
