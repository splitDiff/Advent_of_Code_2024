class Matrix:

    def __init__(self,mat):
        self.matrix = mat
        self.h = len(self.matrix)
        self.w = len(self.matrix[0])


    def cell(self,p1):
        x,y = p1
        if 0 <= x < len(self.matrix[0]) and 0 <= y < len(self.matrix):
            return self.matrix[y][x]
        return None

    def set(self,p1, value):
        x,y = p1
        if 0 <= x < len(self.matrix[0]) and 0 <= y < len(self.matrix):
            self.matrix[y][x] = value
        return None
    
    def rng(self,p1,p2):
        x1,y1 = p1
        x2,y2 = p2
        result = []
        for j in range(y1, y2 + 1):
            for i in range(x1, x2 + 1 ):
                result.append(self.cell((i,j)))
        return result

    def prt(self):
        output = ''
        for j in range(0, len(self.matrix)):
            for i in range(0, len(self.matrix[0])):
                output +=  f"{self.cell((i,j))}"
            output += f"\n"
        output = output.strip()
        return output


    def prt_p(self, p):
        output = ''
        x, y = p
        for j in range(0, len(self.matrix)):
            for i in range(0, len(self.matrix[0])):
                if i == x and j == y:
                    output += "*"
                else:
                    output +=  f"{self.cell((i,j))}"
            output += f"\n"
        output = output.strip()
        return output