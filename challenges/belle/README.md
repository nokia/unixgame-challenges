# The Belle Chess Computer

Ken Thompson, co-inventor of UNIX, is also an avid chess player. At Bell Labs, together with colleague Joe Condon he built [**Belle**](https://www.chessprogramming.org/Belle), a chess computer that was five times winner of the American Computer Chess Championship and that won the third World Computer Chess Championship (WCCC) in 1980.

![Ken Thompson and Joe Condon with Belle](https://images.computerhistory.org/chess/bell-laboratories.belle.thompson-ken-condon-joe.c1977.l062302004.bell-laboratoies.jpg?w=600)

Chess players have invented a notation called [algebraic notation](https://en.wikipedia.org/wiki/Algebraic_notation_(chess)) to record and describe moves in a game of chess. It is based on a system of coordinates that uniquely identify each square on the chessboard, as depicted in the figure below:

![figure of chess board](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/SCD_algebraic_notation.svg/242px-SCD_algebraic_notation.svg.png)

A unique coordinate is assigned to each square on the board using a letter (a to h, the file) and a number (1 to 8, the rank).

Below is a recording of the chess match between chess computers Belle from Bell Labs and the University of Michigan’s CHAOS at the 1980 WCCC in Linz, Austria (Belle won the game and the tournament in a closely matched competition). Belle played White.

![figure of belle vs chaos](https://images.computerhistory.org/chess/wccc-linz.belle-vs-chaos.1980.monty-newborn.102645444.jpg?w=600)

([image credit: Computer History Museum](https://www.computerhistory.org/chess/stl-432a034fb7102/))

```
1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.Nf3 dxe5 5.Nxe5 g6 6.g3 Bf5 7.c4 Nb4 8.Qa4+ N4c6
9.d5 Bc2 10.Qb5 Qd6 11.Nxc6 Nxc6 12.Nc3 Bg7 13.Qxb7 O-O 14.Qxc6 Qb4 15.Kd2 Be4
16.Rg1 Rfb8 17.Bh3 Bh6+ 18.f4 Qa5 19.Re1 f5 20.Qe6+ Kf8 21.b3 Bg7 22.Bb2 Bd4
23.g4 Rb6 24.Qd7 Rd6 25.Qa4 Qb6 26.Ba3 Bxc3+ 27.Kxc3 Rdd8 28.Rad1 Qf2 29.gxf5
Qc2+ 30.Kd4 gxf5 31.Qc6 Qf2+ 32.Ke5 Kg8 33.Rg1+ Kh8 34.Bxe7 Qb2+ 35.Rd4 Qg2
36.Qf6+ Kg8 37.Bxg2 Rxd5+ 38.Ke6 h6 39.Qxh6 Re5+ 40.fxe5 Rf8 41.Bf3# 1-0
```

For the purposes of this question, all that is needed to understand this notation is the following:

A game is written as a series of moves as White/Black pairs, preceded by the move number and a period. For example, in the above match the first two moves are written `1.e4 Nf6`

Each move of a piece is indicated by the piece's uppercase letter, plus the coordinate of the destination square. For example, `Be5` (move a bishop to e5), `Nf6` (move a knight to f6). For pawn moves, a letter indicating pawn is not used, only the destination square is given. For example, `e4` (move a pawn to e4). Pieces are encoded as `K` for king, `Q` for queen, `R` for rook, `B` for bishop, and `N` for knight.

When a piece makes a capture, an `x` is inserted immediately before the destination square. For example, `Bxe5` (bishop captures the piece on e5). When a pawn makes a capture, the file from which the pawn departed is used to identify the pawn. For example, `exd5` (pawn on the e-file captures the piece on d5).

The special chess move of “Castling” between the King and a Rook is indicated by the special notations `O-O` (for kingside castling) and `O-O-O` (queenside castling).

A move that places the opponent's king in check has the symbol `+` appended. 

Checkmate at the completion of moves is represented by the symbol `#`.

The notation 1–0 at the completion of moves indicates that White won, 0–1 indicates that Black won, and ½–½ indicates a draw.

### Questions

  * Q1. How many rounds did the game last? (a round is simply a pair of moves by each of the players, or the final move resulting in checkmate)

  * Q2. How many pieces did Belle capture in this game?

  * Q3. How many pieces did Belle capture with a pawn in this game?

  * Q4. Create a table describing how many captures were made by each type of piece (king, queen, rook, bishop or knight) in this game by Belle, not counting captures made by pawns. The output format must be a number followed by K, Q, R, B or N to denote each type, one line per piece, sorted in descending order, for example:

```
4 Q
2 B
1 R
```

  * Q5. Same as Q4 except captures made by pawns must be counted as well (use P to denote pawns)
  
<!-- For Q4, Q5 beware for ambiguous solutions: there are ties. How to rank the ties? (or allow all permutations that respect ranking) -->

  * Q6. Which was the type of piece (K, Q, R, B, N or P) that Belle used the most?
