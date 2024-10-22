# ROCK_PAPER_SCISSOR_GAME
This code constructs a GUI for a Rock-Paper-Scissors game that is built in the Python language and makes use of the Tkinter library. 
In this game, users can compete against a computer foe by going head to head with either a rock, paper or scissors.

Class Structure: The primary class RockPaperScissorsGame is extended from tk.Tk which is a top widget for the application Most of the components of the user interface are 
created in the init method including the title,enabling the application to run in full screen and loading game images. 
In cases where any background or any of the game images fails to load, such a message is shown and the application is exited.

Game Logic: The play method controls the entire game structure. Whenever the player makes a selection, the computer picks another selection randomly and the winner is who has 
the dominant combination of the two. Labels are updated with this information and as well the images of the user’s and the computer’s selections are shown respectively on the interface. 
And having a mouse click also optimizes the use of screen components such as buttons and levers which are associated with graphical user interfaces which 
are appealing to users of the software as they feature different colors and font types for the frames, buttons and labels.

The code here makes it possible for the audience to actively participate in a classic games of Rock-Paper-Scissors integrating python’s application development tool
for GUI in the game.
