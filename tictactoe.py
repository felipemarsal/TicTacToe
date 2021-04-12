class ticTacToe:

    def __init__(self):
        self.count_x = 0
        self.count_y = 0
        self.count = 0

        self.var0 = " "
        self.var1 = " "
        self.var2 = " "
        self.var3 = " "
        self.var4 = " "
        self.var5 = " "
        self.var6 = " "
        self.var7 = " "
        self.var8 = " "

    def grid(self):
        print(f"""---------
| {self.var0} {self.var1} {self.var2} |
| {self.var3} {self.var4} {self.var5} |
| {self.var6} {self.var7} {self.var8} |
---------""")

        self.row_0 = self.var0 + self.var1 + self.var2
        self.row_1 = self.var3 + self.var4 + self.var5
        self.row_2 = self.var6 + self.var7 + self.var8
        self.column_0 = self.var0 + self.var3 + self.var6
        self.column_1 = self.var1 + self.var4 + self.var7
        self.column_2 = self.var2 + self.var5 + self.var8
        self.diagonal_sleft = self.var0 + self.var4 + self.var8
        self.diagonal_sright = self.var2 + self.var4 + self.var6

        self.all_rows = [self.row_0, self.row_1, self.row_2]
        self.all_columns = [self.column_0, self.column_1, self.column_2]
        self.all_diagonals = [self.diagonal_sleft, self.diagonal_sright]

        self.all_together = [self.all_rows, self.all_columns, self.all_diagonals]

        self.all_units = [''.join(x) for i in self.all_together for x in i]

        self.all_matches_list = [x for i in self.all_together for x in i if x == "OOO" or x == "XXX"]
        self.all_matches = "".join(self.all_matches_list)

    def coordinate(self):
        coordinates = input("Enter the coordinates: ")
        coordinates_number = [int(x) for x in coordinates if x.isdigit()]

        while True:
            if coordinates[0].isdigit() and coordinates[2].isdigit():
                pass
                if (1 <= int(coordinates[0]) <= 3) and (1 <= int(coordinates[2]) <= 3):
                    break
                else:
                    print("Coordinates should be from 1 to 3!")
                    coordinates = input("Enter the coordinates: ")
                    coordinates_number = [int(x) for x in coordinates if x.isdigit()]
            else:
                print("You should enter numbers!")
                coordinates = input("Enter the coordinates: ")
                coordinates_number = [int(x) for x in coordinates if x.isdigit()]

        return coordinates_number

    def x_position(self):
        user_coordinates = self.coordinate()
        if user_coordinates == [1, 1]:
            if self.var0 == " ":
                self.var0 = "X"
                self.grid()
            else:
                print("This cell is occupied! Choose another one!")
                self.x_position()
        elif user_coordinates == [1, 2]:
            if self.var1 == " ":
                self.var1 = "X"
                self.grid()
            else:
                print("This cell is occupied! Choose another one!")
                self.x_position()

        elif user_coordinates == [1, 3]:
            if self.var2 == " ":
                self.var2 = "X"
                self.grid()
            else:
                print("This cell is occupied! Choose another one!")
                self.x_position()

        elif user_coordinates == [2, 1]:
            if self.var3 == " ":
                self.var3 = "X"
                self.grid()
            else:
                print("This cell is occupied! Choose another one!")
                self.x_position()

        elif user_coordinates == [2, 2]:
            if self.var4 == " ":
                self.var4 = "X"
                self.grid()
            else:
                print("This cell is occupied! Choose another one!")
                self.x_position()

        elif user_coordinates == [2, 3]:
            if self.var5 == " ":
                self.var5 = "X"
                self.grid()
            else:
                print("This cell is occupied! Choose another one!")
                self.x_position()

        elif user_coordinates == [3, 1]:
            if self.var6 == " ":
                self.var6 = "X"
                self.grid()

            else:
                print("This cell is occupied! Choose another one!")
                self.x_position()

        elif user_coordinates == [3, 2]:
            if self.var7 == " ":
                self.var7 = "X"
                self.grid()
            else:
                print("This cell is occupied! Choose another one!")
                self.x_position()

        elif user_coordinates == [3, 3]:
            if self.var8 == " ":
                self.var8 = "X"
                self.grid()
            else:
                print("This cell is occupied! Choose another one!")
                self.x_position()

    def o_position(self):
        user_coordinates = self.coordinate()
        if user_coordinates == [1, 1]:
            if self.var0 == " ":
                self.var0 = "O"
                self.grid()
            else:
                print("This cell is occupied! Choose another one!")
                self.o_position()
        elif user_coordinates == [1, 2]:
            if self.var1 == " ":
                self.var1 = "O"
                self.grid()
            else:
                print("This cell is occupied! Choose another one!")
                self.o_position()

        elif user_coordinates == [1, 3]:
            if self.var2 == " ":
                self.var2 = "O"
                self.grid()
            else:
                print("This cell is occupied! Choose another one!")
                self.o_position()

        elif user_coordinates == [2, 1]:
            if self.var3 == " ":
                self.var3 = "O"
                self.grid()
            else:
                print("This cell is occupied! Choose another one!")
                self.o_position()

        elif user_coordinates == [2, 2]:
            if self.var4 == " ":
                self.var4 = "O"
                self.grid()
            else:
                print("This cell is occupied! Choose another one!")
                self.o_position()

        elif user_coordinates == [2, 3]:
            if self.var5 == " ":
                self.var5 = "O"
                self.grid()
            else:
                print("This cell is occupied! Choose another one!")
                self.o_position()

        elif user_coordinates == [3, 1]:
            if self.var6 == " ":
                self.var6 = "O"
                self.grid()

            else:
                print("This cell is occupied! Choose another one!")
                self.o_position()

        elif user_coordinates == [3, 2]:
            if self.var7 == " ":
                self.var7 = "O"
                self.grid()
            else:
                print("This cell is occupied! Choose another one!")
                self.o_position()

        elif user_coordinates == [3, 3]:
            if self.var8 == " ":
                self.var8 = "O"
                self.grid()
            else:
                print("This cell is occupied! Choose another one!")
                self.o_position()

    def draw(self):
        if ((self.x_wins() is False) or (self.o_wins() is False)) and (self.var0 != " " and self.var1 != " " and
                self.var2 != " " and self.var3 != " " and self.var4 != " " and self.var5 != " " and self.var6 != " "
                and self.var7 != " " and self.var8 != " "):
                print("Draw")
                return True
        else:
            return False

    def x_wins(self):

        if self.all_matches == "XXX":
            print("X wins")
            return True
        else:
            return False

    def o_wins(self):

        if self.all_matches == "OOO":
            print("O wins")
            return True
        else:
            return False

game = ticTacToe()
game.grid()

while True:
    game.x_position()
    if game.x_wins():
        break
    if game.draw():
        break
    game.o_position()
    if game.o_wins():
        break
    if game.draw():
        break