
from tkinter import *
from tkinter import ttk

class Counter:



    def __init__(self, root):
        self.entry_value = StringVar(root, value="0.0")
        self.total_games = StringVar(root, value="0")


        root.title("Chess Game Counter")

        root.geometry("400x130")
        root.resizable(width=False, height=False)
        style =ttk.Style()
        style.configure("TButton", font="Serif 15",padding="10")
        style.configure("TEntry", font="Serif 25")
        style.configure("TLabel", font="Serif 15")


        scoreColor = StringVar()
        gamesColor = StringVar()


        ###Menu
        menubar = Menu(root)

        ###File Menu###
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Reset",command=lambda: self.press_reset())
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)



        root.config(menu=menubar)




        #score label

        ttk.Label(root,text="SCORE:").grid(row=0, column=0)

        # display for the game result
        self.result_display = ttk.Entry(root,textvariable=self.entry_value)

        self.score_label = ttk.Label(root,text=self.entry_value.get(), textvariable=self.entry_value).grid(row=0,column=2)
        # / Label

        ttk.Label(root,text="/").grid(row=0,column=3)

        #Display total number of games
        self.game_display = ttk.Entry(root,textvariable=self.total_games, width=2)

        self.games_label = ttk.Label(root,text=self.total_games.get(), textvariable=self.total_games).grid(row=0, column=4)
        #win loss draw buttons

        self.win_button = ttk.Button(root,text="Win", command=lambda: self.button_press('1.0')).grid(row=1,column=0, columnspan=2)

        self.draw_button = ttk.Button(root,text="Draw", command=lambda: self.button_press('0.5')).grid(row=1,column=2,columnspan=2)

        self.loss_button = ttk.Button(root,text="Loss", command=lambda: self.button_press('0.0')).grid(row=1,column=4,columnspan=2)

        # undo + reset buttons

        self.reset_button = ttk.Button(root,text="Reset", command=lambda: self.press_reset()).grid(row=3,column=0,columnspan=2)
        self.press_undo = ttk.Button(root,text="Undo", command=lambda: self.press_undo()).grid(row=3,column=2, columnspan=2)


    def button_press(self,value):
        entry_val =self.entry_value.get()
        entry_val = float(entry_val) + float(value)
        self.result_display.delete(0,"end")
        self.result_display.insert(0, entry_val)
        tot_games = self.total_games.get()
        tot_games = int(tot_games) + 1
        self.game_display.delete(0,"end")
        self.game_display.insert("0",tot_games)


    def press_reset(self):
        entry_val =self.result_display.get()
        tot_games = self.total_games.get()
        self.result_display.delete(0,"end")
        self.game_display.delete(0,"end")

        self.result_display.insert(0, 0.0)
        self.game_display.insert(0,0)


    def press_undo(self):
        None


### File Menu Commands
    def client_exit(self):
        exit()



root = Tk()
game_counter = Counter(root)

root.mainloop()
