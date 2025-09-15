# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #use stack
    stack = util.Stack()
    visited = set()
    #push initial state in
    stack.push(((problem.getStartState(), "", 0), []))
    #list of directions agent took
    finaltravel = []
    
    #while loop with condition of a non-empty stack
    while not stack.isEmpty():
        pop = stack.pop()
        #pop[0][0] is the current state
        if problem.isGoalState(pop[0][0]):
            finaltravel = curtraversal
            print(finaltravel)
            return pop[1]
        #add current state to explored set.
        visited.add(pop[0][0])
        #checking for successor states. I is each state that succeeds the pop state
        #remember i is the successor of pop[0][0] containing a state, move, and of course cost
        for i in problem.getSuccessors(pop[0][0]):
            curtraversal = []
            state = i[0]
            move = i[1]
            cost = i[2]
            print(state)
            print(move)
            if state not in visited:
                curtraversal = list(pop[1])
                curtraversal.append(move)
                stack.push(((state, move, cost), curtraversal))
                
            
    
    # util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    visited = set()
    queue.push(((problem.getStartState(), "", 0), []))
    travel = []
    while not queue.isEmpty():
        pop = queue.pop()
        if problem.isGoalState(pop[0][0]):
            travel = curtravel
            print(travel)
            return pop[1]
        if pop[0][0] not in visited:
            visited.add(pop[0][0])
            for i in problem.getSuccessors(pop[0][0]):
                curtravel = []
                state = i[0]
                move = i[1]
                cost = i[2]
                # print(state)
                # print(move)
                curtravel = list(pop[1])
                curtravel.append(move)
                queue.push(((state, move, cost), curtravel))
            
            
                
            
    # util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # same logic as bfs, but with cost effectiveness
    # use pq(priority queue)
    pq = util.PriorityQueue()
    visited = set()
    pq.push((problem.getStartState(), [], 0), 0)
    pop = pq.pop()
    travel = []
    
    # while not pq.isEmpty() was not working as most likely I reached the end of the non-visited pq. So instead I'm gonna change it to checking the goal state.
    while not problem.isGoalState(pop[0]):
        visited.add(pop[0])
        # When placed inside of the inner loop, I'm essentially starting the whole process over again for each successor. Like retracing my steps    
        for i in problem.getSuccessors(pop[0]):
            curtravel = []
            priority = 0
            state = i[0]
            move = i[1]
            cost = i[2]
            
            if state not in visited:
                curtravel = list(pop[1])
                curtravel.append(move)
                priority = pop[2] + cost
                pq.update((state, curtravel, priority), priority)
        pop = pq.pop()
        
    
    travel = pop[1]
    return travel
            
                
                
            
            
                
        
    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
