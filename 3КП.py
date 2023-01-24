from tkinter import *
import time
import random
tk = Tk()
tk.title('Game')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
basis = Canvas(tk, width=700, height=600, highlightthickness=0)
basis.pack()
tk.update()


class Ball:
    def __init__(self, basis, platform, score, color):
        self.basis = basis
        self.platform = platform
        self.score = score
        self.id = basis.create_oval(15,15, 40, 40, fill=color)
        self.basis.move(self.id, 220, 120)
        starts = [-2, -1, 1, 2]
        random.shuffle(starts)
        self.x = starts[1]
        self.y = -2
        self.basis_height = self.basis.winfo_height()
        self.basis_width = self.basis.winfo_width()
        self.hit_bottom = False
    def hit_platform(self, pos):
        platform_pos = self.basis.coords(self.platform.id)
        if pos[2] >= platform_pos[0] and pos[0] <= platform_pos[2]:
            if pos[3] >= platform_pos[1] and pos[3] <= platform_pos[3]:
                self.score.hit()
                return True
        return False
    def draw(self):
        self.basis.move(self.id, self.x, self.y)
        pos = self.basis.coords(self.id)
        if pos[1] <= 0:
            self.y = 2
        if pos[3] >= self.basis_height:
            self.hit_bottom = True
            basis.create_text(250, 120, text='Вы проиграли', font=('Courier', 30), fill='blue')
        if self.hit_platform(pos) == True:
            self.y = -2
        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= self.basis_width:
            self.x = -2


class Platform:

                def __init__(self, basis, color):
                    self.basis = basis
                    self.id = basis.create_rectangle(0, 0, 120, 10, fill=color)
                    start_1 = [45, 54, 80, 110, 140, 160, 220]
                    random.shuffle(start_1)
                    self.starting_point_x = start_1[0]
                    self.basis.move(self.id, self.starting_point_x, 300)
                    self.x = 0
                    self.basis_width = self.basis.winfo_width()
                    self.basis.bind_all('<KeyPress-Right>', self.turn_right)

                    self.basis.bind_all('<KeyPress-Left>', self.turn_left)
                    self.started = False
                    self.basis.bind_all('<KeyPress-Return>', self.start_game)

                def turn_right(self, event):
                    self.x = 4
                def turn_left(self, event):
                    self.x = -3
                def start_game(self, event):
                    self.started = True
                def draw(self):
                    self.basis.move(self.id, self.x, 0)
                    pos = self.basis.coords(self.id)
                    if pos[0] <= 0:
                        self.x = 0
                    elif pos[2] >= self.basis_width:
                        self.x = 0


class Score:

    def __init__(self, basis, color):
        self.score = 0
        self.basis = basis
        self.id = basis.create_text(450, 10, text=self.score, font=('Courier', 15), fill=color)


    def hit(self):
        self.score += 2


        self.basis.itemconfig(self.id, text=self.score)

score = Score(basis, 'green')
platform = Platform(basis, 'Yellow')
ball = Ball(basis, platform, score, 'black')
while not ball.hit_bottom:
    if platform.started == True:
        ball.draw()
        platform.draw()

    tk.update_idletasks()

    tk.update()

    time.sleep(0.009)

time.sleep(3)

