from warnings import warn
import heapq

# Create a node class
class Node():
    def __init__(self, parent = None, position = None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __repr__(self):
        return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"

    def __lt__(self, other):
        return self.f < other.f 

    def __gt__(self, other):
        return self.f > other.f 

def returnPath(currentNode):
    path = []
    current = currentNode
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1] # return reversed path

# A* algorithm: it will return a list of tuples as a path from the given start to the given goal in the given maze
def AStarPathFinding(maze, start, goal): 
    # Create start and goal node
    startNode = Node(None, start)
    startNode.g = startNode.h = startNode.f = 0
    goalNode = Node(None, goal)
    goalNode.g = goalNode.h = goalNode.f = 0

    # Initialize open and closed list
    openList = []
    closedList = []

    # Heapify the open list and add the start node
    heapq.heapify(openList)
    heapq.heappush(openList, startNode)

    # Add a stop condition
    outerIteration = 0
    maxIteration = len(maze[0]) * len(maze) // 2

    # Moving rules
    motions = ((0, -1), (0, 1), (-1, 0), (1, 0))

    # Loop until we find the goal
    while len(openList) > 0:
        outerIteration += 1

        # Get the current node
        currentNode = heapq.heappop(openList)
        closedList.append(currentNode)

        if outerIteration > maxIteration:
            # If we hit this point return the path such as it is
            # It will not contain the destination
            warn("Giving up on path finding too many iterations")
            return returnPath(currentNode)

        # Found the goal
        if currentNode == goalNode:
            return returnPath(currentNode)

        # Generate children
        children = []

        for move in motions:
            # Get node position
            nodePosition = (currentNode.position[0] + move[0], currentNode.position[1] + move[1])

            # Make sure within range
            if nodePosition[0] > (len(maze) - 1) or nodePosition[0] < 0 or nodePosition[1] > (len(maze[len(maze)-1]) -1) or nodePosition[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[nodePosition[0]][nodePosition[1]] != 0:
                continue

            # Create new node
            newNode = Node(currentNode, nodePosition)

            # Append
            children.append(newNode)

        # Loop through children
        for child in children:
            # Child is on the closed list
            if len([closedChild for closedChild in closedList if closedChild == child]) > 0:
                continue

            # Calculate the f, g, and h values
            child.g = currentNode.g + 1
            child.h = ((child.position[0] - goalNode.position[0]) ** 2) + ((child.position[1] - goalNode.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            if len([openNode for openNode in openList if child.position == openNode.position and child.g > openNode.g]) > 0:
                continue

            # Add the child to the open list
            heapq.heappush(openList, child)

    warn("Couldn't get a path to destination")
    return None


maze = [[0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 1, 1, 0, 0, 1, 0, 0, 1, 1],
        [0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0]]

start = (0, 0)
goal = (9, 9)

path = AStarPathFinding(maze, start, goal)
print(path)