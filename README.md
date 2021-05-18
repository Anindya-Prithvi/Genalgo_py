# Genetic algorithm implementation for alphanumeric text

This is a basic implementation of a genetic algorithm in python. The main intention was to try and break unsafe hashing techniques. Although for fun I created a genetic algorithm to "guess" images.

## How it works?
This algorithm is almost like real life evolution. First a pool of random genes are spawned (much like the RNA).
The genes get a success score (which maybe the match with the target we want to achieve). The genes with higher success score replicate more and populate the pool. The unfit genes get destroyed as their population gets smaller. Also, the successful progenies are subjected to random mutations. Due to this mutation the population is able to evolve. Here the mutation can be as simple as replacing a few characters in a big word. Finally as the gene pool gets dominated by better genes the algorithm steers towards the end. We get the "best" gene and our task is complete.

## How to run (hashbreakgen.py)?
1. Download and install python 3.8 (preffered, may download any python 3 version). 
2. Download this file.
3. Right click, **edit with IDLE** (open this file with IDLE, if dont see the option, just search on google)
4. Press F5 on keyboard
5. then type the following on seperate lines after pressing return (enter) key.
`gen = Genalgo(1000, 'I am Iron Man')`
`while True:`
`gen.gen_progress()`
`time.sleep(0.3)`

You may modify the codes accordingly.
My code follows OOP coding style, hence it contains classes and methods. Feel free to customize it yourself.
