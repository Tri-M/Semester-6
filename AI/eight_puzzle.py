class Node:
    def __init__(self, data, level, fval):
        self.data = data
        self.level = level
        self.fval = fval

    def genNext(self):
        x, y = self.findPosBlank(self.data, '_')
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        kids = []
        for i in val_list:
            kid = self.shiftPos(self.data, x, y, i[0], i[1])
            if kid is not None:
                kid_node = Node(kid, self.level + 1, 0)
                kids.append(kid_node)
        return kids

    def shiftPos(self, puz, x1, y1, x2, y2):
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            puzTemp = []
            puzTemp = self.xeroxCopyMatrix(puz)
            temp = puzTemp[x2][y2]
            puzTemp[x2][y2] = puzTemp[x1][y1]
            puzTemp[x1][y1] = temp
            return puzTemp
        else:
            return None

    def xeroxCopyMatrix(self, root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def findPosBlank(self, puz, x):  
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j


class Puzzle:
    def __init__(self, size):
        self.n = size
        self.open = []
        self.closed = []

    def takeInput(self):
        puz = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f(self, start, goal):
        # Heuristic function to calculate Heuristic value f(x) = h(x) + g(x)
        return self.h(start.data, goal) + start.level

    def h(self, start, goal):
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp

    def process(self):
        print("enter the start state matrix \n")
        start = self.takeInput()
        print("enter the goal state matrix \n")
        goal = self.takeInput()
        start = Node(start, 0, 0)
        start.fval = self.f(start, goal)
        self.open.append(start)
        print("\n\n")
        while True:
            cur = self.open[0]
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")
            if (self.h(cur.data, goal) == 0):
                break
            for i in cur.genNext():
                i.fval = self.f(i, goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]
            self.open.sort(key=lambda x: x.fval, reverse=False)


puz = Puzzle(3)
puz.process()
