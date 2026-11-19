
class MyMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [i for i in range(rows*cols)]

    def zeros(self):
        self.data = [0] * len(self.data)
        
    def __repr__(self):
        all_rows = ''
        for r in range(self.rows):
            row_str = [f'{self.data[r*self.cols + c]:5}' 
                       for c in range(self.cols)]
            all_rows += ''.join(row_str) + '\n'
        return all_rows
        
    def __getitem__(self, key):
        r, c = key
        return self.data[r*self.cols + c]
    
    def __setitem__(self, key, value):
        r, c = key
        self.data[r*self.cols + c] = value
            
    def multiply_dot(self, other):
        assert self.cols == other.rows  # valid dimensions
        nrows, ncols, mid = self.rows, other.cols, self.cols
        
        def dot(self, other, row, col, mid):
            """ Returns dot product of row 'row' in 'self' 
            and column 'col' in 'other'. """
            d = 0
            for i in range(mid):
                d += self[row,i] * other[i,col]
            return d
                
        result = MyMatrix(nrows, ncols)
        for r in range(nrows):
            for c in range(ncols):
                result[r,c] = dot(self, other, r, c, mid)
        return result
    
    def multiply_rows(self, other):
        assert self.cols == other.rows  # valid dimensions
        nrows, ncols, mid = self.rows, other.cols, self.cols
        result = MyMatrix(nrows, ncols)
        result.zeros()  # zero all ellements
        
        def add_row(other, col, result, row, multiplier):
            """ Add row 'col' in 'other' to row 'row' in 'result'
            after multiplication by 'multiplier'. """
            for c in range(other.cols):
                result[row, c] += other[col, c] * multiplier

        for r in range(self.rows):
            for c in range(self.cols):
                add_row(other, c, result, r, self[r,c])
        return result


# Show MyMatrix as table
mg.config.type_to_node[MyMatrix] = (
  lambda m:  mg.Node_Table(m, m.data, m.cols)
               if hasattr(m, 'data') else
             mg.Node_Table(m, [])
)

m1 = MyMatrix(3, 5)
print(m1)

m2 = MyMatrix(5, 4)
print(m2)

r1 = m1.multiply_dot(m2)
print(r1)

r2 = m1.multiply_rows(m2)
print(r2)
