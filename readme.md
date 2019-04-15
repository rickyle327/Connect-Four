# Readme

## Note to Team
Just so everyone's aware, the read in and read out functions were in Doug's example and should not be changed. The two most important functions for this program are as follows:

The `valid_moves` function is what determines where moves are legal (mainly whether or not a column is full). This was in the original and does not need to be changed. 

The `player_moves` function is what I added and determines how the computer makes its move. Essentially the `valid_moves` function will pass an array, from 0 to whatever the max_width of columns that have empty slots. The `player_moves` will select a column to 'drop' its token in, returning an int that denotes that column. Right now, this selection is random, but as we progress, I'm assuming we will want to add to it.

## To run
Please ensure that the player and driver are in the same directory and the `define exe-2` points to the path of python player executable (this is under the `dist` directory), then change `define arg-2` to `(define arg-2 '())` 
To run against itself also replace player `define exe-2` to the same path as above, then also change `define arg-1` to same syntax as above.

PyInstaller was used to create the executable


## To Run Mac
Change 'define exe-1 or exe-2' to the executable of the main source code file. 

Example:
;;; These will eventually be command line arguments.
(define exe-1 "connect-four-naive")
(define args-1 '())
(define exe-2 "cf")
(define args-2 '())
