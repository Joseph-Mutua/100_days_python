# from turtle import Turtle, Screen

# mutua = Turtle()

# print(mutua)
# mutua.shape("turtle")
# mutua.color("coral")
# mutua.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_rows([["Pikachu", "Electric"], ["Squirtle", "Water"],
                ["Charmander", "Fire"]])
table.align = "l"
print(table)