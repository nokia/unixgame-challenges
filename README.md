# Unix Game Challenges

This repository contains the Unix Game ([https:://unixgame.io](https://www.unixgame.io/)) challenges and metadata, released under the permissive CC BY-NC 2.0 license to foster external contributions.

## Contest Data Format

A UnixGame contest consists of a series of challenges, with each challenge comprising one or more questions.

The contest server can be configured to read contest data from a directory that adheres to the following simple format:

```
contest.json
challenge1/
  README.md
  challenge.json
  input.txt
challenge2/
  README.md
  challenge.json
  input.txt
...
```

### Defining a contest

In the directory root, place a `contest.json` file with the following layout:
  
  ```json
  {
      "challenges": [
          "challenge1",
          "challenge2",
          ...
      ]
  }
  ```
  
The names `challenge1`, `challenge2` correspond to names of subdirectories. Each subdirectory defines a challenge.

### Defining a challenge

Put each challenge into its own subdirectory. The subdirectory should contain at least the following files:

```
README.md
challenge.json
input.txt
```

The `README.md` markdown file containing a description of the challenge. The markdown should have a section marked `### Questions` containing a markdown list. Each item in this list is treated as the description of a separate question.
  
The `challenge.json` file has the following layout:
  
```json
{
  "name": "challenge_name",
  "blocks": [ "sort", ... ],
  "questions": [
      {
          "question": 1,
          "input": "my_custom_input.txt",
          "blocks": [ "sort", ... ],
          "solutions": [
              "solution output 1",
              "solution output 2",
              ...
          ]
      }
  ]
}
```

Here, `name` is the title of the challenge as rendered in the UI. `blocks` is the subset of relevant blocks to solve this question, and can be overridden per-question for question-specific blocks. If no blocks are specified, all blocks are available. `questions` defines a list of questions. Each question is defined by a sequence number and must define a `solutions` field.

The `solutions` field contains a list of strings describing possible valid outputs of the user's pipeline. Our contest server compares the output of the user's program against all of these strings. If any string matches, the program is considered valid. A question can also set `input` to a text file in the challenge directory (by default this is `input.txt`).
  
The file `input.txt` defines the standard input that will be sent to the user's program for all questions in this challenge (one can define additional text files per-question using the `input` field in `challenge.json`).
