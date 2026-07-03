# Pacman AI — Project 1: Search

Implementation of uninformed and informed search algorithms for the Pacman AI framework, built on the UC Berkeley CS188 Pacman projects.

## Overview

This project builds general-purpose search algorithms and uses them to solve pathfinding problems for Pacman: reaching a fixed point, visiting all four corners of a maze, and eating all the food on the board.

## What's Implemented

**`search.py`**
- **Depth-First Search** — stack-based graph search with a visited set, returns the first path found to the goal.
- **Breadth-First Search** — queue-based graph search, guarantees the shortest path in terms of number of actions.
- **Uniform Cost Search** — priority-queue search ordered by cumulative path cost, correctly relaxes nodes when a cheaper path to a state is found.
- **A\* Search** — priority-queue search ordered by cumulative cost plus a heuristic estimate to the goal.

**`searchAgents.py`**
- `CornersProblem` — a custom search problem whose state space and successor function support finding a path through all four corners of a maze.
- `AnyFoodSearchProblem.isGoalState` — goal test used by `ClosestDotSearchAgent` to greedily eat the nearest dot.

**Not yet implemented**
- `cornersHeuristic` — currently returns 0 (equivalent to uninformed search rather than a true admissible heuristic).
- `foodHeuristic` — currently returns 0.

## Project Structure

```
search/
├── search.py             # Core search algorithms (DFS, BFS, UCS, A*)
├── searchAgents.py        # Pacman agents and problem definitions (Corners, Food, etc.)
├── pacman.py              # Main game engine (do not modify)
├── game.py, util.py       # Supporting game and utility classes
├── layouts/               # Maze layouts used for testing
└── test_cases/            # Autograder test cases
```

## How to Run

Run Pacman with a chosen search algorithm:

```bash
python pacman.py -p SearchAgent -a fn=depthFirstSearch
python pacman.py -p SearchAgent -a fn=breadthFirstSearch
python pacman.py -p SearchAgent -a fn=uniformCostSearch
python pacman.py -p SearchAgent -a fn=aStarSearch,heuristic=manhattanHeuristic
```

Solve the four-corners problem:

```bash
python pacman.py -p AStarCornersAgent -l mediumCorners -z 0.5
```

Grade your work against the provided test cases:

```bash
python autograder.py
```

## Attribution

The Pacman AI projects were developed at UC Berkeley. Core projects and autograders were created by John DeNero and Dan Klein; student-side autograding was added by Brad Miller, Nick Hay, and Pieter Abbeel. Used here for educational purposes per the Berkeley AI course license — see http://ai.berkeley.edu.
