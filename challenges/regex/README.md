# Background

Al Aho and Jeff Ullman won the 2020 ACM AM Turing award for their key contributions to programming language theory and implementation and their foundational work on compilers. The two began collaborating at Bell Labs in 1967 kicking off a decades-long partnership. Aho and Ullman, quite literally, wrote the books on several areas of computer science. Their textbooks **The Design and Analysis of Computer Algorithms** (1974, with John Hopcroft) and **Principles of Compiler Design** (1977) are classics in their fields and have been studied by budding computer scientists for decades. They co-authored many other textbooks and research papers and continued to jointly influence the development of computer programming well into the new millennium.

(image credit: <a href="https://awards.acm.org/about/2020-turing" target="_blank">Association for Computing Machinery</a>)

In this challenge you will be tasked with building "regular expressions". A regular expression (often abbreviated as "regex") is a sequence of characters written in a small language to describe search patterns. They are commonly used for finding specific patterns in a text editor and for parsing program text as part of a compiler.

You can find a brief introduction to the basic syntax of regular expressions on [Wikipedia](https://en.wikipedia.org/wiki/Regular_expression#Syntax). You can also peek at page 3 of [the manual for the QED text editor](https://www.bell-labs.com/usr/dmr/www/qedman.pdf) by Dennis Ritchie and Ken Thompson which concisely lists all the basic syntax.


### Questions

  * Q1. Find the regex that matches the following examples:
  
  ```
  abc
  abbbc
  abbbbbc
  ```

  but DOESN'T match the following counter-examples:

  ```
  ac
  aaabbc
  bcc
  ```

  * Q2. Find the regex that matches all positive integers, including zero. Numbers with leading zeroes (such as 007) should not match!
  
  * Q3. Find the regex that matches all even positive integers, including zero. Leading zeroes are allowed.
  
  * Q4. Find the regex that matches non-empty words over the alphabet {a, b} with at most one 'a'.
  
  Positive examples:

  ```
  a
  b
  ab
  bab
  bbbabb
  bbbbba
  ```

  Negative examples:
  ```
  aab
  abbc
  bc
  ```

  * Q5. Find the regex that matches words over the alphabet {a, b} with at least one 'a'.
  
  Positive examples:

  ```
  a
  ab
  baaab
  bbabbab
  bbbbba
  ```

  Negative examples:

  ```
  b
  ac
  bbb
  aaabbc
  ```

  * Q6. Find the regex that matches words of lowercase letters where the letters can appear only in lexicographical order. The empty string is allowed.
  
  <div class='wraparound'>
    <div>
        <p>This is a challenge originally found as an exercise in the "Purple Dragon Book" by Alfred V. Aho, Monica S. Lam, Ravi Sethi, and Jeffrey D. Ullman.</p>
        <p>In this exercise, just fill in the Regular Expression manually. No blocks are provided, but you have the full power of regular expression syntax at your disposal.</p>
        <p>Remember: with great power comes great responsibility!</p>
    </div>
  </div>


  
  Positive examples:
  ```
  abc
  cdef
  axz
  ```

  Negative examples:

  ```
  ba
  abcad
  xmb
  ```

  * Q7. Find the regex that matches words of lowercase letters containing the five common vowels {a, e, i, o, u} in lexicographical order.

  <div class='wraparound'>
    <div>
        <p>Another exercise found in the "Purple Dragon Book" by Alfred V. Aho, Monica S. Lam, Ravi Sethi, and Jeffrey D. Ullman.</p>
        <p><i>TIP: Although we supply some useful blocks here, you may want to replace the default regex block with the "power" regex block in which you can simply write the Regular Expression as in the previous excercise (see 'commands' in the toolbox).</i></p>
    </div>
  </div>

  Positive examples:
  ```
  abeicou
  baaceediou
  abbbbbeccciboou
  ```

  Negative examples:

  ```
  ac
  aaabbcou
  aeaiou
  ```

  * Q8. Find the regex that matches a structure loosely modeled after [mRNA sequences](https://en.wikipedia.org/wiki/Messenger_RNA) over the alphabet of nucleotides {A,C,T,G}.

  In eukaryotes, spliced mRNA structure consists of three main parts:
  1. Start with a start codon (ATG)
  2. Treat the coding part of the mRNA sequence as an arbitrary string of {A,C,T,G} that ends with one of three stop codons (TAA/TAG/TGA)
  3. Immediately after the stop codon there is a 'poly(A) tail'. The poly(A) tail is a long run of many adenines (A's). For the purposes of this exercise, assume the poly(A) tail consists of at least 5 adenines.

Valid Examples:

```
ATGCTGATGATGATGATAGAAAAA
ATGTGAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

Invalid Examples:

```
ATGCTGATGXTGATGATAGAAAAA
TATGCTGATGXTGATGATAGAAAAA
ATGTGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC
```

_(exercise credits will be shown after you complete the exercise)_

![Eukaryotes](https://upload.wikimedia.org/wikipedia/commons/7/7d/Eukaryota_diversity_2.jpg)

(image source: [wikipedia](https://en.wikipedia.org/wiki/Eukaryote))

  * Q9. Find the regex that matches the Hawaiian fish `humuhumunukunukuapua'a` in the input text. When you succeed you will learn how to pronounce it :-)

  ![Humuhumunukunukuapua'a](https://upload.wikimedia.org/wikipedia/commons/b/b8/Picasso.triggerfish.arp.jpg)

  <!-- * Q10. Match only the words that appear more than once on a single line. Use a 'capturing group (...)' to capture the matching words.

```
Work it harder, make it better
Do it faster, makes us stronger
More than ever, hour after hour
Work is never over
``` -->
