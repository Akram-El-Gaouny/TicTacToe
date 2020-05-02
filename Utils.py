class Utils(object):
    def indexConverter(self, constant, row, columns):
        """
        (int,int,int) -> int
        return a 1d index from a 2d index 
        constant -- Board Columns
        row -- row number of the index
        columns -- column number of the index

        """
        return (constant * row ) + columns


