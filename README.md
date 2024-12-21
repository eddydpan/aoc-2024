# Advent of Code 2024

This repo is a way I'm storing my progress on the AOC 2024. I'm starting 
12/21/24. I haven't really committed to trying as many problems as I can for 
the AOC, so I am very curious as to where I'll end up with another year of 
programming under my belt :)

[Adevent of Code 2024](https://adventofcode.com/2024)


### Day 1

I learned about Heaps being auto-sorted, which made this problem really easy 
and run in less than a hundredth of a second. The heapq documentation is pretty
good and easy to follow. Heaps are datatstructures that are both sorted and 
decreasing. For part 2, I used Counter from the Python collections module, 
which helped me get a dictionary of the number of occurences for each of the 
items in the right list so I could just reference them in the left list. It 
also helped that the Counter object would return 0 if I tried to access an
element that didn't exist in it. 