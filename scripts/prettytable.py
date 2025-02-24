from python_projects.scripts.prettytable import PrettyTable 
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Quiartle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"


print(table)
