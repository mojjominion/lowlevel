# Player, Game, Move, Engine, GameManager, Board, BoardConfig

## Requirements
- user should be able to start the game with pre-configured game board
- user should be able to make a valid move
- user should not be able to make an invalid move
- ai should be able to make a smart and valid move
- notify user on game end
- show the winner and winning streak

## Non-functional:
- Ai should be fast, user should not wait for long
- update the board on any move reasonably fast
- undo allowed


## Relationships:
- Board       --(has-a)---> BoardConfig
- Game        --(has-a)---> Board, Players, Engine 
- GameManager --(has-a)---> Game,  Players
- BoardConfig --(has-a)---> Rules, size

