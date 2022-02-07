# Welcome

The Unix Game is a fun, low-barrier-to-entry programming contest where players solve 
coding challenges by constructing "pipelines" of UNIX text processing utilities to compute the solution.
Press the button below to take a quick tour around the UI:

<center><button class="w3-btn w3-blue submit" onclick="startIntroduction();" style="margin:20px;">Take a tour!</button></center>

Check the [leaderboard](/leaderboard) to see how you compare against other players. You can download a badge of honor from your [profile page](/profile) to showcase your progress to your friends.

Are you ready to crack your first question?

## Warm-up: UNIX at Bell Labs

In this first challenge you are given a file containing the names of Bell Labs staff that made key technical contributions to UNIX, based on [a list](https://www.princeton.edu/~hos/Mahoney/unixpeople.htm) from Michael S. Mahoney, Professor of History at Princeton.

Here are the first 5 lines in the file:

```
Ken Thompson
Dennis Ritchie
Joe Osanna
Bob Morris
Doug McIlroy
```

Click on each question below to find out what you're asked to do with this file.

### Questions

  * Q1. Extract the last name of each person and sort the list of last names in alphabetical order.
  
  We have already provided the command to extract the last name. Can you find the command to sort lines?

  When you're happy with your code, press the 'Submit' button to validate your solution.

  * Q2. Extract only Ken Thompson and Dennis Ritchie's last names. Hint: look at Thompson and Ritchie's names in the list. What's special about the position of these lines in the file? Can you find a command that lets you get just those lines?
  * Q3. Count how many times each first name appears in the list and sort the names by how many times they occur in the file, starting with the most common name. The first line should look like this:
    
```
   3 Joe
``` 

Hint: carefully study the `uniq -c` command. To make it work correctly, you'll first need to combine it with another command.
