import memory_graph as mg

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
            row_str = [f'{self.data[r*self.cols + c]:4}' 
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
        result = MyMatrix(nrows, ncols)

        def dot(row, col, mid):
            """ Returns dot product of row 'row' in 'self' 
            and column 'col' in 'other'. """
            d = 0
            for i in range(mid):
                d += self[row,i] * other[i,col]
            return d
                
        # Iterate over each element in 'result'
        for r in range(nrows):
            for c in range(ncols):
                result[r,c] = dot(r, c, mid)
        return result
    
    def multiply_rows(self, other):
        assert self.cols == other.rows  # valid dimensions
        nrows, ncols, mid = self.rows, other.cols, self.cols
        result = MyMatrix(nrows, ncols)
        result.zeros()  # zero all elements
        
        def add_row(col, row, multiplier):
            """ Add row 'col' in 'other' to row 'row' in 'result'
            after multiplication by 'multiplier'. """
            for c in range(other.cols):
                result[row, c] += other[col, c] * multiplier

        # Iterate over each element in 'self'
        for r in range(self.rows):
            for c in range(self.cols):
                add_row(c, r, self[r,c])
        return result
    

    def multiply_tiled(self, other, tile_size=2):
        assert self.cols == other.rows  # valid dimensions
        nrows, ncols, mid = self.rows, other.cols, self.cols
        result = MyMatrix(nrows, ncols)
        result.zeros()  # zero all elements

        def add_tile(rr, cc, kk):
            """ Add tile 'rr', 'cc' with 'kk' offset to 'result'. """
            for r in range(rr, min(rr + tile_size, nrows)):
                for c in range(cc, min(cc + tile_size, ncols)):
                    for k in range(kk, min(kk + tile_size, mid)):
                        result[r, c] += self[r, k] * other[k, c]
        
        # Iterate over tiles
        for rr in range(0, nrows, tile_size):
            for cc in range(0, ncols, tile_size):
                for kk in range(0, mid, tile_size):
                    add_tile(rr, cc, kk)
        return result

# Show MyMatrix as table
mg.config.type_to_node[MyMatrix] = (
  lambda m:  mg.Node_Table(m, m.data, m.cols)
               if hasattr(m, 'data') else
             mg.Node_Table(m, [])
)

m = 5  # dimension that must match between two matrices for multiplication
m1 = MyMatrix(3, m)
print('m1:', m1, sep='\n')

m2 = MyMatrix(m, 4)
print('m2:', m2, sep='\n')

r1 = m1.multiply_dot(m2)
print('r1:', r1, sep='\n')

r2 = m1.multiply_rows(m2)
print('r2:', r2, sep='\n')

r3 = m1.multiply_tiled(m2)
print('r3:', r3, sep='\n')
