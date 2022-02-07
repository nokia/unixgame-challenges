# The C Programming Language

The [C programming language](https://en.wikipedia.org/wiki/C_(programming_language)) was designed by [Dennis Ritchie](https://www.bell-labs.com/usr/dmr/www/index.html) at Bell Labs. The UNIX kernel was originally written in assembler, but was later rewritten in C.

<img src="http://code.danyork.com/files/2011/10/KandR-CProgrammingLang.jpg" width="60%" alt="Photo of the cover of the C Programming Language book">


You are given the following text file, containing the code of the venerable ["hello world"](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) C program. This program prints the words "hello, world":

```c
main()
{
    printf("hello, world\n");
}
```

The first person to implement the above program was [Brian W. Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan), who used it as the very first example of a C program in the C Programming Language book, also known as the "K&R book" or the "C Bible". It has since become tradition to introduce novice programmers to a new programming language through "hello, world" programs.

### Questions

  * Q1. Build a program that takes the above program text as input and extracts from it the words "hello, world" - thus generating the same output that the C program would if it were executed. Your solution does not need to work for arbitrary C programs, only for this one.