class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newcolor: int) -> List[List[int]]:
        
        def dfs_fill(image, sr, sc, prevcolor, newcolor):
            rows, cols = len(image), len(image[0])

            if (
                sr < 0 or sc < 0 or sr >= rows or sc >= cols or
                image[sr][sc] != prevcolor or image[sr][sc] == newcolor
            ):
                return

            image[sr][sc] = newcolor
            dfs_fill(image, sr + 1, sc, prevcolor, newcolor)
            dfs_fill(image, sr - 1, sc, prevcolor, newcolor)
            dfs_fill(image, sr, sc + 1, prevcolor, newcolor)
            dfs_fill(image, sr, sc - 1, prevcolor, newcolor)

        prevcolor = image[sr][sc]
        dfs_fill(image, sr, sc, prevcolor, newcolor)

        return image
