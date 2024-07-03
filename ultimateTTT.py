import random 
import math
import sys

class Game:
        def __init__(self):
            self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(9)]
            self.current_player = 1
            self.last_move = (-1, -1)
            self.winner = 0
            self.small_grid = [ 
                                0, 0, 0, 
                                0, 0, 0, 
                                0, 0, 0
                            ]

        def get_legal_actions(self):
            legal_actions = []
            if self.last_move == (-1, -1):
                for i in range(9):
                    for j in range(9):
                        legal_actions.append((i, j))
                return legal_actions
            small_grid_index = (self.last_move[1] % 3) + 3 * (self.last_move[0] % 3)
            if self.small_grid[small_grid_index] == 0:
                legal_actions = self.legal_action_small(small_grid_index)
            else:
                for i in range(9): #index grid
                    if self.small_grid[i] == 0:
                        t = self.legal_action_small(i)
                        for j in t:
                            legal_actions.append(j)
            return legal_actions

        def legal_action_small(self, smIndex):
            x = (smIndex // 3) * 3
            y = (smIndex * 3) % 9
            l = []
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if self.board[i][j] == 0:
                        l.append((i, j))
            return l

        def make_move(self, x, y):
            self.board[x][y] = self.current_player
            self.last_move = (x, y)
            smIndex = (y % 3) + 3 * (x % 3)
            self.check_winner(smIndex)
            self.current_player = 3 - self.current_player
        
        def check_winner(self, smIndex):
            x = (smIndex // 3) * 3
            y = (smIndex * 3) % 9
            g = []
            for i in range(x, x + 3):
                t = []
                for j in range(y, y + 3):
                    t.append(self.board[i][j])
                g.append(t)
            for i in range(3):
                    if g[i][0] == g[i][1] and g[i][2] == g[i][1] and g[i][0] != 0:
                        self.small_grid[smIndex] = g[i][0]
                        return
                    if g[0][i] == g[1][i] and g[2][i] == g[1][i] and g[0][i] != 0:
                        self.small_grid[smIndex] = g[0][i]
                        return
            if g[0][0] == g[1][1] and g[0][0] == g[2][2] and g[0][0] != 0:
                self.small_grid[smIndex] = g[0][0]
                return
            if g[0][2] == g[1][1] and g[0][2] == g[2][0] and g[0][2] != 0:
                self.small_grid[smIndex] = g[0][2]
                return
            o = False
            for i in range(3):
                for j in range(3):
                    if g[i][j] == 0:
                        o = True
                        break
                if o:
                    break
            if not o:
                self.small_grid[smIndex] = -1
        
        def check_winner_small(self):
            g = self.small_grid
            for i in range(0, 9, 3):
                if (g[i] == g[i + 1] and g[i] == g[i + 2]) and g[i] != 0:
                    # print('Vainceur:', g[i])
                    self.winner = g[i]
                    return True
            for i in range(3):
                if (g[i] == g[i + 3] and g[i] == g[i + 6]) and g[i] != 0:
                    # print('Vainceur:', g[i])
                    self.winner = g[i]
                    return True
            if g[0] == g[4] and g[0] == g[8] and g[0] != 0:
                # print('Vainceur:', g[6])
                self.winner = g[6]
                return True
            if g[2] == g[4] and g[2] == g[6] and g[2] != 0:
                # print('Vainceur:', g[6])
                self.winner = g[6]
                return True
            o = False
            for i in range(9):
                if g[i] == 0:
                    o = True
            if o:
                return False
            self.winner = -1
            # print('Match nul')
            return True
            

        def is_terminal(self):
            for i in range(9):
                if self.small_grid[i] == 0:
                    self.check_winner(i)
            return self.check_winner_small()

        def display(self):
            for i in range(3):
                for j in range(3):
                    grid = self.board[3 * i + j]
                    print(' '.join(('X' if cell == 1 else 'O') if cell != 0 else '.' for cell in grid[0:3]), end = ' | ')
                    print(' '.join(('X' if cell == 1 else 'O') if cell != 0 else '.' for cell in grid[3:6]), end = ' | ')
                    print(' '.join(('X' if cell == 1 else 'O') if cell != 0 else '.' for cell in grid[6:9]))
                if i < 2:
                    print('-' * 21)

        def display_small(self):
            print("SMALLLLLL:")
            for i in range(9):
                if i % 3 == 0:
                    print()
                print(self.small_grid[i], end = '\t')
            print()
                
game = Game()

while not game.is_terminal():
    legales_moves = game.get_legal_actions()
    #print(*legales_moves)
    choice_bot = random.choice(legales_moves)
    print("BOT X", choice_bot, game.current_player)
    x, y = choice_bot
    # print('Veuillez choisir un move:')
    # x, y = map(int, input().split())
    game.make_move(x, y)
    # game.display_small() 
    game.display()
    if game.is_terminal():
        break
    legales_moves = game.get_legal_actions()
    choice_bot = random.choice(legales_moves)
    print('Bot O: ', choice_bot, game.current_player)
    x1, y1 = choice_bot
    game.make_move(x1, y1)
    # game.display_small()
    game.display()

print() 

if game.winner == -1:
    print("Match nul")
else:
    print("Vainceur : ", 'X' if game.winner == 1 else 'O')

# game.display_small()    
# game.display()

#display small montre le grand Grille du tictactoe

