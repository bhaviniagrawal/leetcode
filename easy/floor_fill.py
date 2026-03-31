class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        self.fill(image, sr, sc, image[sr][sc], newColor)
        return image
    

    def fill(self, image: List[List[int]], sr: int, sc: int, color: int, newColor: int):
        # out of bounds
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]):
            return
        if image[sr][sc] != color:
            return
            
        image[sr][sc] = newColor
        self.fill(image, sr - 1, sc, color, newColor)
        self.fill(image, sr + 1, sc, color, newColor)
        self.fill(image, sr, sc - 1, color, newColor)
        self.fill(image, sr, sc + 1, color, newColor)


   