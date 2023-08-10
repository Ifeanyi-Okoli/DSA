""" 
Depth First Search Method
Def dfs(I,j)
1.	Initialize an empty stack and set
Visit = set()
Q= collections.deque()
2.	Push the starting node into the stack and set
Visit.add(I,j)
q.append((I,j))
3. while the stack is not empty
While q:
	Pop a node the stack
	Row, col = q.popleft()
	If the node has not been visited, 
Mark it as visited
		Directions = [[1,0], [0,1], [-1,0], [0,-1]]
		Perform other computations necessary.
	Repeat step 3 until stack is empty

"""


import collections

# The function numIslands takes a 2D grid as input and returns the number of islands as an integer.
def numIslands(grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        The code begins by checking if the grid is empty (if not grid). If the grid is empty, it means there are no islands, so the function immediately returns 0.
        """
        if not grid:
            return 0
        # The variables rows and cols are initialized with the number of rows and columns in the grid, respectively. The length of the grid gives the number of rows, and the length of any row gives the number of columns.
        rows, cols = len(grid), len(grid)
        
        # The visit set is initialized to keep track of visited cells. It stores the coordinates of cells that have been visited during the depth-first search (DFS) traversal.
        visit = set()
        
        # The islands variable is initialized to 0. This variable will store the count of islands.
        islands = 0
        
        # The dfs function is defined to perform the depth-first search traversal. It takes the coordinates (i, j) of a cell as input.
        def dfs(i, j):
            # Inside the dfs function, a deque object q is initialized to store the cells to be visited. The visit set is updated to include the current cell (i, j).
            q = collections.deque()
            
            visit.add((i, j))
            
            # The current cell (i, j) is added to the q deque using q.append((i, j)).
            q.append((i, j))
            print(q)
            print(visit)
            # The DFS traversal begins with a while loop that continues until the q deque is empty.
            while q:
                # In each iteration of the while loop, a cell is dequeued from the left side of the q deque using q.popleft(). The variables row and col store the coordinates of the dequeued cell.
                row, col = q.popleft()
                # The directions variable is a list of coordinate offsets that represent the four possible directions to explore from the current cell: right, down, left, and up. The offsets are [1,0] (down), [0,1] (right), [0,-1] (left), and [-1,0] (up).
                directions =  [[1,0], [0,1], [0,-1], [-1,0]]
                
                # The code then iterates over each direction in the directions list using the for dr, dc in directions: loop.
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visit:
                        visit.add((r, c))
                        q.append((r, c))
                        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visit:
                    dfs(i, j)
                    islands += 1
        return islands
        
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
    
print(numIslands(grid))