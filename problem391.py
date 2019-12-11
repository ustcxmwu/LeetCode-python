from typing import List, Tuple


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        for id1, rect1 in enumerate(rectangles):
            for id2, rect2 in enumerate(rectangles):
                if id1 == id2:
                    continue
                if self.isCover(rect1, rect2):
                    return False
        area = 0
        for rect in rectangles:
            area += self.getArea(rect)
        x1 = min(min([rect[0] for rect in rectangles]), min([rect[2] for rect in rectangles]))
        y1 = min(min([rect[1] for rect in rectangles]), min([rect[3] for rect in rectangles]))
        x2 = max(max([rect[0] for rect in rectangles]), max([rect[2] for rect in rectangles]))
        y2 = max(max([rect[1] for rect in rectangles]), max([rect[3] for rect in rectangles]))
        total_area = self.getArea([x1, y1, x2, y2])
        return total_area == area

    def isCover(self, rect1: List[float], rect2: List[float]):
        x1, y1, x2, y2 = rect1
        x3, y3, x4, y4 = rect2
        return (x4 - x1) * (x2 - x3) > 0 and (y4 - y1) * (y2 - y3) > 0

    def getArea(self, rect: List[float]):
        length = rect[0] - rect[2]
        width = rect[1] - rect[3]
        return abs(length * width)


if __name__ == '__main__':
    # rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
    # print(Solution().isRectangleCover(rectangles))
    a = [1, 2, 3, 4]
    b = [4, 5, 6, 7]
    print(min(a, b))
