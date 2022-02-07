# The ABC's of UNIX

![UNIX](https://www.bell-labs.com/usr/dmr/www/smunixblocks.jpg)

Above: photo for a [UNIX ad](https://www.bell-labs.com/usr/dmr/www/unixad.html), dated 1980, from the Lucent archives.

`fortune` is a program that displays a pseudorandom message (a "fortune cookie") from a database of quotations. It first appeared in Version 7 UNIX. The most common version of `fortune` on modern systems was written by [Ken Arnold](https://en.wikipedia.org/wiki/Ken_Arnold) while at Berkeley. It is typically used to generate a 'message of the day' on user login.

The input file contains a poem (attribution unknown) taken from a `fortune` database.
Your task is to write a program that extracts from the poem the names of all the UNIX utilities mentioned.

Hint: here's the output of `head -n 3` on the expected output of your program:

```
awk
biff
cc
```

### Questions

  * Q1. Extract all UNIX utilities mentioned in the poem in the input file.
