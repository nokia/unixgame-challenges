# The Nokia Snake

The classic arcade game [Snake](https://en.wikipedia.org/wiki/Snake_(video_game_genre)) became wildly popular when a variant of the game was released on Nokia 3300 series phones. In the game, the player steers a snake towards an apple.

You are given a file with instructions that control how the snake moves on a 2D grid.

The snake follows instructions top to bottom.

There are only three instructions: `move forward`, `turn left` and `turn right`.

Turning left or right changes the orientation of the snake by 90 degrees without changing its position. Moving forward lets the snake move 1 step forward in the direction it is facing.

If the snake bumps against the edge of the grid or against a wall, it remains at its previous position.

Look below to see the starting position of the snake and the target position of the apple.

The starting list of instructions is:

```
turn left
turn left
move forward
turn right
turn right
move forward
turn left
move forward
```

### Questions

  * Q1. Your task is to transform this list of instructions such that if the snake follows the new instructions top to bottom, it ends on the location of the apple.

Hint: you can delete instructions by removing lines, copy instructions by duplicating lines, and rearrange instructions by swapping lines.
