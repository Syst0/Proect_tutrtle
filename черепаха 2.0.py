class LabirintTurtle:
    def __init__(self, *args, **kwargs):
        self.pole = []
        self.pole1 = []
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.way = []
    def load_map(self, name, *args, **kwargs):
        f = open(name, 'r') 
        i = 0
        for line in f: 
            self.pole.append([])
            self.pole1.append([])
            for j in range(len(line)): 
                self.pole[i].append(line[j]) 
                self.pole1[i].append(line[j])
            i += 1
        if self.pole[-2][0].isdigit() and self.pole[-1][0].isdigit():
            self.x = int(self.pole[-2][0])
            self.y = int(self.pole[-1][0])
        self.w = len(self.pole[0]) - 1
        self.h = len(self.pole) - 2 

    def show_map(self, turtle = False, *args, **kwargs):
        if not turtle:
            for i in range(self.h):
                for j in range(self.w):
                    print(self.pole[i][j], end='')
                print ()
                
        else:
            for i in range(self.h):
                for j in range(self.w):
                    if i == self.x and j == self.y:
                        print("A", end='')
                    else:
                        print(self.pole[i][j], end='')
                print ()
                
    def check_map(self, *args, **kwargs):
        for i in range(self.h):
            for j in range(self.w):
                if self.pole[i][j] != '*' and self.pole[i][j] != " ":
                    return False
        if not self.pole[-2][0].isdigit() or not self.pole[-1][0].isdigit():
            return False
        count = 0
        for i in range(self.w):
            if self.pole[0][i] == ' ':
                count += 1
            if self.pole[self.h - 1][i] == ' ':
                count += 1
        for i in range(self.h):
            if self.pole[i][0] == ' ':
                count += 1
            if self.pole[i][self.w - 1] == ' ':
                count += 1
        if count == 0:
            return False
        if self.x >=self.w or self.x < 0 or self.y >= self.h or self.y < 0:
            return False
        if self.pole[self.x][self.y] == '*':
            return False
        if self.f(self.x, self.y) == -1:
            self.clear_pole1()
            return False
        self.clear_pole1()
        return True
        
    def f(self, a, b, n = 0, *args, **kwargs):
        if self.pole1[a][b] != ' ':
            return -1
        if a == 0 or a == self.w - 1 or b == 0 or b == self.h - 1:
            self.pole1[a][b] = '.'
            return 0
        self.pole1[a][b] = n
        r = [0]*4
        r[0] = self.f(a+1,b,n+1)
        r[1] = self.f(a,b+1,n+1)
        r[2] = self.f(a-1,b,n+1)
        r[3] = self.f(a,b-1,n+1)
        if r[0] == r[1] == r[2] == r[3] == -1:
            return -1
        
        for i in range(4):
            if r[i] != -1:
                m = r[i]
                mi = i
                break
        for i in range(4):
            if r[i] != -1:
                if m > r[i]:
                    m = r[i]
                    mi = i
        self.pole1[a][b] = '.'
        if mi == 0:
            self.way.append('вниз')
        elif mi == 1:
            self.way.append('вправо')
        elif mi == 2:
            self.way.append('вверх')
        elif mi == 3:
            self.way.append('влево')
        
        if n == 0:
            for i in range(self.h):
                for j in range(self.w):
                    if self.pole1[i][j] != '*' and self.pole1[i][j] != '.':
                        self.pole1[i][j] = ' '
        return m + 1
        
    def show_map1(self, turtle = True, *args, **kwargs):
        res = self.f(self.x, self.y)
        if not turtle:
            for i in range(self.h):
                for j in range(self.w):
                    print(self.pole1[i][j], end='')
                print()
                
        else:
            for i in range(self.h):
                for j in range(self.w):
                    if i == self.x and j == self.y:
                        print("A", end='')
                    else:
                        print(self.pole1[i][j], end='')
                print ()
        self.clear_pole1()
    def exit_count_step(self, *args, **kwargs):
        res = self.f(self.x, self.y)
        self.clear_pole1()
        print(res)
    def exit_show_step(self, *args, **kwargs):
        res = self.f(self.x, self.y)
        for i in range(self.h):
            for j in range(self.w):
                if i == self.x and j == self.y:
                    print("A", end='')
                else:
                    print(self.pole1[i][j], end='')
            print()
        for i in range(len(self.way)-1,-1,-1):
            print (len(self.way)-i,self.way[i])
        self.clear_pole1()
    def clear_pole1(self):
        self.pole1 = self.pole
        self.way = []