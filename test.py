#Test syntaxs
import engine

# Importing Class
from engine import mine_engine

# Defining Variable
engine = mine_engine(10,10,20)

# Creating the map
engine.create_map()

# Printing Raw map
engine.print_map()

# Generating mines
engine.generate_mines()

# Printing game map
engine.print_map()

# Flaging a Cell
engine.flag(2,5)
engine.flag(3,6)
engine.flag(0,9)
engine.flag(7,1)

# Printing game map
engine.print_map()

#TO CHEAT AND SEE MINES_ADDRESSES :P
print(engine.mines_adds)

# Clicking on a cell
engine.click(8,4)
engine.click(4,2)
engine.click(1,6)
engine.click(2,2)
engine.click(5,7)
engine.click(0,1)
# Printing game map
engine.print_map()
