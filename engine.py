import random

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')

class mine_engine:
    mine_map = Array() # [[row]]
    mines_adds = Array() # [addresses in mine_map]
    map_size = Array() # row x col -> exp: 8 x 8
    map_flaged = Array()
    num_mines = int()

    def __init__(self):
        pass

    def __str__(self):
        pass



    def message(self,result ,operation, cause = None):
        """
        Prints success or failor message.
        result is bool
        operation is string
        """
        if result:
            print(color.GREEN + f'{operation} executed successfully')
        else:
            print(color.RED + f'Error in executing {operation} {"\n -> " + cause if cause else ""}')





    def map_size(self,rows,cols):
        """
        Will set map_size array
        returns bool
        """
        if int(rows)<100 && int(cols)<100:
            self.map_size = [rows,cols]
            self.message(True,'map_size')
            return True
        else:
            self.message(False,'map_size', 'invalid inputs')
            return False

    def print_map(self):
        if check_vars():
            for num ,row in enumerate(self.mine_map):
                if num == 0:
                    print('---'*self.map_size[1])
                print(f'{f'|{col}|' for col in row}')
                print('---'*self.map_size[1])
        else:
            self.message(False,'print_map','Error in reading variables.')


    def check_vars(self):
        """
        Checks if game map and variables are defined correctly to start the game.
        checks :
            map_size = Array() # row x col -> exp: 8 x 8
            num_mines = int()
        returns bool
        """
        if self.map_size && self.num_mines:
            return True
        else:
            return False

    def create_map(self):
        """
        Creates a new game mine map
        returns mines' array
        """
        if check_vars() :
            self.mine_map = []
            for row in range(self.map_size[0]):
                for col in range(self.map_size[1]):
                    self.mine_map[row][col] = ' '
            self.message(True,'create_map')
        else:
            self.message(False,'create_map','Error in reading variables.')

    def generate_mines(self):
        """
        Generates mines addresses and puts them into mines_adds array.
        """
        if check_vars() && self.mine_map && self.num_mines:
            for mine in range(self.num_mines):
                while True:
                    randrow = random.randint(0,self.map_size[0])
                    randcol = random.randint(0,self.map_size[1])
                    if [randrow,randcol] not in self.mines_adds:
                        self.mines_adds.append([random,randcol])
                        break
            self.message(True,'generate_mines')
        else:
            self.message(False,'create_map',"""Error in reading variables or there is no map created,
                                                create a map by runngin create_map() function""")


    def check_cell(self,row,col):
        """
        Will return addresses of mines around it.[[row,col]]
        if it is mine, returs True.
        """
        return [cell for cell in [[crow,col] for crow in [row+1,row-1]]+[[row,ccol] for ccol in [col+1,col-1]] if cell in self.mines_adds]


    def flag(self,row,col):
        """
        Flags a selected cell, flags cell addresses will be saved in map_flaged and mine_map array.
        returns bool
        """
        if self.check_vars():
            if [row,col] in self.map_flaged:
                self.map_flaged.remove([row,col])
                self.mine_map[row][col] = " "
            else:
                self.map_flaged.append([row,col])
                self.mine_map[row][col] = "P"
        else:
            self.message(False,'flag',"""Error in reading variables or there is no map created,
                                                create a map by runngin create_map() function""")

    def click(self,row,col):
        """
        Will action selecting a cell, if it is mine will blow,
        otherwise will reveal number of mines near for selected cells,
        but if it is zero, checks for each 4 neighbours,if they are numbers,
        reveals them, but if each is zero, again that neighbour checks for unreveled neighbours.
        """
        pass

    def game_over(self):
        clear_terminal()
        print(color.BOLD + color.RED + 'GAME OVER!')

    def game_win(self):
        clear_terminal()
        print(color.BOLD + color.YELLOW + 'YOU WON!')
