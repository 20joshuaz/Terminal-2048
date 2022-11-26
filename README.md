# 2048

2048 is an online game that can be played [here](https://play2048.co/). 
This program emulates the game in terminal without excessive printing.

To play, run `python3 play.py`. By default, the game is played on a 4 x 4 board 
and will stop once you reach the target tile of 2048. You can customize the target tile 
and dimensions of the board by passing in more arguments to the command. 
To play without a goal tile (play until loss), set the target tile to -1.

- `python3 play.py`: Target tile of 2048 on a 4 x 4 board
- `python3 play.py 512`: Target tile of 512 on a 4 x 4 board
- `python3 play.py 4096 5`: Target tile of 4096 on a 5 x 5 board
- `python3 play.py -1 4`: Play until loss on a 4 x 4 board
