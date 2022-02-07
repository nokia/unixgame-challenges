> Copyright 2019-2022 Nokia
>
> Licensed under the Creative Commons Attribution 2.0 Generic license
> 
> SPDX-License-Identifier: CC-BY-2.0

# sort

Sort lines of text files.

origin: v1 AT&T UNIX [my man pages say v3?]

Sort a file in ascending order:

    sort filename

Sort a file in descending order:

    sort -r filename

Sort a file using numeric rather than alphabetic order:

    sort -n filename

Sort the passwd file by the 3rd field, numerically:

    sort -t: -k 3n /etc/passwd

Random shuffle lines in a file:

    sort -R filename

# wc

Count words, bytes, or lines.

origin: v1 AT&T UNIX

Count lines in file:

    wc -l file

Count words in file:

    wc -w file

# cut

Cut out fields from STDIN or files.

origin: AT&T System III UNIX

Cut out the first sixteen characters of each line of STDIN:

    cut -c 1-16

Cut out the fifth field of each line, using a colon as a field delimiter (default delimiter is tab):

    cut -d':' -f5

Cut out the 2nd and 10th fields of each line, using a semicolon as a delimiter:

    cut -d';' -f2,10

# awk

General-purpose text processing tool.

Assumes files are built from records (by default, one record per line)
and records are built from fields (by default, separated by a space)

origin: v7 AT&T UNIX

Extract the second word from each line

    awk '{print $2}'

Extract the second TAB-separated field from each line

    awk 'BEGIN {FS="\t"} {print $2}'

# head

Output the first part of files.

origin: PWB UNIX

Output the first few lines of a file:

    head -n count_of_lines filename

# tail

Display the last part of a file.

origin: PWB UNIX

Show last 'num' lines in file:

    tail -n num file

# grep

filter lines matching pattern

origin: v4 AT&T UNIX [man pages say v6?]

Search for an exact string:

    grep search_string

Search in case-insensitive mode:

    grep -i search_string

Use extended regular expressions (supporting ?, +, {}, () and |):

    grep -E regex

Invert match for excluding specific strings:
  
    grep -v search_string

# nl

A utility for numbering lines, either from a file, or from standard input.

origin: System III [man pages say AT&T System V UNIX]

Number non-blank lines in a file:
  
    nl file

Number all lines including blank lines:

    nl -b a

# paste

merge lines of files

origin: Version 32V AT&T UNIX

Join all the lines into a single line, using the specified delimiter:
  
    paste -s -d delimiter

# uniq

Output the unique lines from the given input or file.
Since it does not detect repeated lines unless they are adjacent, we need to sort them first.

origin: uniq (v3 AT&T UNIX)

Display each line once:

    sort file | uniq

Display only unique lines:

    sort file | uniq -u

Display only duplicate lines:

    sort file | uniq -d

Display number of occurrences of each line along with that line:

    sort file | uniq -c

Display number of occurrences of each line, sorted by the most frequent:
(Count the number of times each line occurs in file)

    sort file | uniq -c | sort -nr

# sed

stream editor

origin: v7 AT&T UNIX

Replace the first occurrence of a string in a file, and print the result:

    sed 's/find/replace/' filename

Replace all occurrences of a string in a file, and print the result:

    sed 's/find/replace/g' filename

Replace only on lines matching the line pattern:

    sed '/line_pattern/s/find/replace/' filename
    
Print lines starting with one containing FOO and ending with one containing BAR.

    sed -n '/FOO/,/BAR/p'

Delete the 2nd line:

    sed '2d'

Delete the first 10 lines:

    sed '1,10d'

Emulate unix2dos (add CR before each NL):

    sed -e 's/$/\r/' < unix.txt > win.txt

Duplicate each line in a file:

    sed -n 'p;p;'
    
Duplicate the second line in a file:

    sed '2p'

Select the second line in a file:

    sed -n '2p'

Append the character 'x' to each line in a file:

    sed 's/$/x/'

Prepend the character 'x' to each line in a file:

    sed 's/^/x/'

# tr

Translate characters: run replacements based on single characters and character sets.

origin: v4 AT&T UNIX

Replace all characters 'd' by 'E':

    tr 'd' 'E'
    
Replace ',' characters by newlines:

    tr "," "\n"

Join all lines in a file (delete all newlines):

    tr -d "\n"

Lowercase all characters:

    tr '[A-Z]' '[a-z]'

# rev

Reverse lines of text characterwise.

origin: unknown

    rev

# fmt

Reformat a text file by joining its paragraphs and limiting the line width to given number of characters (75 by default).

origin: 3BSD

Put each word in a file on its own line:

    fmt -w 1

# less useful text transforms

# fold

Wraps each line in an input file to fit a specified width and prints it to the standard output.

origin: 1BSD

Wrap each line to default width (80 characters):

    fold file

Wrap each line to width "30":

    fold -w30 file

# find

Find files or directories under the given directory tree, recursively.

origin: v1 AT&T UNIX

Find files by extension:

    find root_path -name '*.ext'

## split

Split a file into pieces.

origin: v3 AT&T UNIX

csplit? (PWB UNIX) [ok]

Split a file, each split having 10 lines (except the last split):

    split -l 10 filename

# binary operations

Commands operating on two input files.

Perhaps less suited to building simple (linear) pipelines?

## join

Join lines of two sorted files on a common field.

origin: v7 AT&T UNIX [tbc]

Join two files on the first (default) field:

    join file1 file2

## diff

Compare files and directories.

origin: v5 AT&T UNIX [tbc]

Compare files:

    diff file1 file2


# misc

### useful transformations

Break one word per line with `perl -pe 's/\s+/\n/g'`

Remove all blank lines with `perl -ne 'print if /\S/'`

