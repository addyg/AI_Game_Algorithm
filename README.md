# AI Game Algorithm
An AI algorithm to play a Laser Checkmate game against a Human adversary.

Laser Checkmate is a board game in which two players take turns placing laser emitters on a square N×N board. Each emitter shoots laser beams in eight directions: up, down, left, right, and all four diagonal directions. The beams travel up to 3 squares in each direction, but are unable to travel through walls (around the border of the grid) or blocks (occupying squares within the grid). The goal of the game is to place emitters so that your beams cover more squares than your opponent’s lasers do.

Coverage of a square is not mutually exclusive, and a square can be covered by both players at the same time.

The game terminates when there are no valid moves. The final score for each player is the number of squares that their laser beams cover, including the squares where their laser emitters are placed. The game winner is the one who has the higher score in the end.

