import tkinter as tk
from tkinter import messagebox

class TicTacToe:

    def __init__(self, root):

        self.root = root
        self.root.title("Tic Tac Toe - Logic Version")
        self.turno = "X"
        self.tablero = [""] * 9
        self.botones = []

        self.crear_interfaz()


    def crear_interfaz(self):

        for i in range(9):

            boton = tk.Button(
                self.root,
                text="",
                font=('Arial', 20),
                width=5,
                height=2,
                command=lambda i=i: self.marcar_casilla(i)
            )

            boton.grid(row=i//3, column=i%3)

            self.botones.append(boton)


        boton_reset = tk.Button(
            self.root,
            text="Reiniciar",
            font=('Arial', 15),
            command=self.reiniciar
        )

        boton_reset.grid(row=3, column=0, columnspan=3, sticky="we")


    def marcar_casilla(self, i):

        if self.tablero[i] == "":

            self.tablero[i] = self.turno

            self.botones[i].config(text=self.turno)

            if self.verificar_ganador():

                messagebox.showinfo("Ganador", f"Jugador {self.turno} gana")
                self.reiniciar()

            elif "" not in self.tablero:

                messagebox.showinfo("Empate", "Es un empate")
                self.reiniciar()

            else:

                self.turno = "O" if self.turno == "X" else "X"


    def verificar_ganador(self):

        combinaciones = [

            (0,1,2),
            (3,4,5),
            (6,7,8),

            (0,3,6),
            (1,4,7),
            (2,5,8),

            (0,4,8),
            (2,4,6)

        ]

        for a,b,c in combinaciones:

            if self.tablero[a] == self.tablero[b] == self.tablero[c] != "":

                return True

        return False


    def reiniciar(self):

        self.tablero = [""] * 9

        for boton in self.botones:

            boton.config(text="")

        self.turno = "X"



if __name__ == "__main__":

    root = tk.Tk()

    app = TicTacToe(root)

    root.mainloop()