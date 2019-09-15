[![Build Status](https://travis-ci.org/64bit-lab/Logik.svg?branch=master)](https://travis-ci.org/64bit-lab/Logik)

# Logik

This program provide a simple way to manipulate and interact with propositional logic expressions.

## NOTES

> Logik is an educationnal project. It is not designed to be powerful and robust. But it can be used as a tool to solve logic exercices at a Bachelor level.

> If you want to take part in the developpement of Logik in any way you want, feel free to pull request !

## FEATURES

Logik provides 3 main features :

+ Evaluating expressions from the propositional logic
+ Building truth tables from parametrized expressions
+ Extracting the syntax tree of an expression

## How to use Logik ?

Logik is designed to be use in a terminal. You can install it by executing the following command directly inside the main folder. (you need to `git clone https://github.com/64bit-lab/Logik` first)

```
$ python3 setup.py install
```

This will install Logik directly on your machine. You can then start logik by typing :

```
$ logik
```

This will start the interactive command line interface :

```
$ logik
[ command ] @ # type a command here
```

### Commands

+ `tree`    : inputs a formula and display its syntax tree
+ `table`   : inputs a formula and display its truth table
+ `solve`   : **WIP**, will apply resolution algorithm to a set of clauses
+ `cnf`     : convert a formula into conjunctive normal form
+ `clauses` : inputs a formula and display it as a set of clauses

### Syntax of logical expressions/formulas

The syntax of the expressions in Logik is really simple :

**True | Top**
```
1
```

**False | Bottom**
```
0
```

**Implications**
```
a -> b
```

**Conjunction**
```
a et b
```

**Disjunction**
```
a ou b
```

**Negation**
```
non a
```

You can use parenthesis to write some more complex expressions :

```
(a ou b) -> (a et c) or ((a et d) or (b -> (c and e)))
```

## TODO(S)

There is still a lot of things which can be added to improve this project. Here is a list of cool features to add in the future :

+ SAT Solver
+ Predicate logic
+ API to manipulate formulas directly in any python project
+ and more ... (feel free to propose your own suggestions)
















