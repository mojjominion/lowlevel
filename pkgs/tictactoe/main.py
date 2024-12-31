# Player, Game, Move, Engine, GameManager, Board, BoardConfig

# Requirements
# 1. user should be able to start the game with pre-configured game board
# 2. user should be able to make a valid move
# 3. user should not be able to make an invalid move
# 4. ai should be able to make a smart and valid move
# 5. notify user on game end
# 6. show the winner and winning streak

# Non-functional:
# 1. Ai should be fast, user should not wait for long
# 2. update the board on any move reasonably fast
# 3. undo allowed


# Relationships:
# Board       --(has-a)---> BoardConfig
# Game        --(has-a)---> Board, Players, Engine 
# GameManager --(has-a)---> Game,  Players

# BoardConfig ---(has-a)--> Rules, size

