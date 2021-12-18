# advent-of-code
Python3 bases solutions for 2021 Advent of Code
https://adventofcode.com/2021
## 2021
###Day 6:
For part 1, I used just an array with position of each fish.
So there was a array entry per fish.  This was fast enough for 
 a few day.  But with part 2 going to 256 days quickly over
powered my laptop and was getting very slow to calculate.
Moved to array index being the number of fish at given position
vastly increased speed of calculation.
```
PART1: Lantern Fish after  80: 391671
PART2: Lantern Fish after 256: 1754000560399
```

###Day 7:
The calculation of best position is a bit brute forced
```
PART1: Moved to pos 341 using 344605
PART2: Moved to pos 472 using 93699985
```


###Day 8:
Stole idea from REDDIT for part 2
```
Advent of Code 2021 - Day 8
PART1:  539
PART1:  1084606
```

###Day 9:
Added utils module for common convert, init, load methods
```
PART1: Low   =  494
PART2: Basin =  1048128
```

###Day 10
```
PART1: Invalid Lines =  316851
PART2: Incomplete Lines =  2182912364
```

###Day 11
Refactored to add Grid base class
```
PART1: Flashes after Step 100 = 1625
PART2: All flashed on Step  244
```

###Day 12
Took multiple tries to get recursion to work
```
PART1: Paths = 5576
PART2: Paths = 152837
```

###Day 13
```
PART1:  704
PART2:  HFAJBEHC
  0 #  #  ##   ##    ## ###  #### #  #  ##  
  1 #  # #  # #  #    # #  # #    #  # #  # 
  2 #### #    #  #    # ###  ###  #### #    
  3 #  # # ## ####    # #  # #    #  # #    
  4 #  # #  # #  # #  # #  # #    #  # #  # 
  5 #  #  ### #  #  ##  ###  #### #  #  ##  
```

###Day 14
```
PART1: After 10 steps:  2549
PART2: After 40 steps:  2516901104210
```

###Day 15
Recursive algorith ok for example but not input
Dijkstra algorith ok for example and port 1, but not part 2

```
PART1: 626
```