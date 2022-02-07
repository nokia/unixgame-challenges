# The Space Travel Video Game

Space Travel was an early video game developed by Ken Thompson. In 1969 he ported the game to the PDP-7, and along the way he implemented his own base libraries for programs to use, including arithmetic packages and graphics subsystems. That basic software suite was later expanded to a full operating system that would form the core of UNIX.

The game is a simulation of space travel in the solar system, with the objective of landing a spaceship on different planets and moons.

![space_travel_screenshot](https://upload.wikimedia.org/wikipedia/commons/4/46/Space_Travel_Screenshot.png)

The player can move the ship, turn the ship, and adjust the overall speed by adjusting the scale of the simulation.  The ship is affected by the gravitational pull of the astronomical body with the strongest pull. To increase or decrease the difficulty level, one can adjust the gravitational pull of the bodies. Bodies with stronger gravity are easier to land on; for bodies with weak gravity, the player typically has to adjust the scale (zoom in) to successfully land.

The game was never distributed beyond its initial locations and there are no known copies of it. To learn more about the history of the game, see what UNIX co-inventor Dennis Ritchie wrote about Thompson's video game [on his webpage](https://www.bell-labs.com/usr/dmr/www/spacetravel.html).

### Questions

  * Q1. You are given a file with two columns: the names of different bodies in the solar system, and their gravitational pull (in m/s^2).
  
  Can you order the bodies by how easy it would be to land on them in Thompson's Space Travel game when playing at the highest simulation scale (i.e. fully zoomed out)?

  Your solution file should contain just a single column with the names of planets, in the correct order.

