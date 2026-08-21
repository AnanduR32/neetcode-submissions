class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        nrow = len(heights)
        ncol = len(heights[0])
        canReachPacific = [[False for _ in range(ncol)] for _ in range(nrow)]
        canReachAtlantic = [[False for _ in range(ncol)] for _ in range(nrow)]
        visited = [[False for _ in range(ncol)] for _ in range(nrow)]
        output = []
        def helperPacific(i, j, prev, visited):
            if i == nrow or j == ncol:
                return True

            if (
                i == -1
                or j == -1
                or (i,j) in visited
                or heights[i][j] > prev
            ):
                return False
                
            visited.add((i,j))
            res = (
                helperPacific(i + 1, j, heights[i][j], visited)
                or helperPacific(i, j + 1, heights[i][j], visited)
                or helperPacific(i - 1, j, heights[i][j], visited)
                or helperPacific(i, j - 1, heights[i][j], visited)
            )
            return res


        def helperAtlantic(i, j, prev, visited):
            if i == -1 or j == -1:
                return True
            if (
                i == nrow 
                or j == ncol
                or (i,j) in visited
                or heights[i][j] > prev
            ):
                return False
     
            visited.add((i,j))
            res = (
                helperAtlantic(i - 1, j, heights[i][j], visited)
                or helperAtlantic(i, j - 1, heights[i][j], visited)
                or helperAtlantic(i + 1, j, heights[i][j], visited)
                or helperAtlantic(i, j + 1, heights[i][j], visited)
            )
            return res

        for i in range(nrow):
            for j in range(ncol):
                canReachAtlanticBool = helperPacific(i,j,float('inf'),set())
                canReachPacificBool = helperAtlantic(i,j,float('inf'),set())
                if canReachAtlanticBool and canReachPacificBool:
                    output.append([i,j])

        return output