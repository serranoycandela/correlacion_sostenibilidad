class CriteriaVector:

    def __init__(self, variables, matrix):
        self.variables = variables
        self.matrix = matrix

    def update(self, variable, delta):
        """
        updates whole variables vector when delta applied to single variable

        :param variable: index for self.variables list, to be modified by delta
        :param delta: rate of change for criterion
        """
        if type(self.matrix) is dict:
            # if matrix is a dicit variable must be the key
            assert variable in self.matrix

        for i in range(len(self.variables)):
            if i == variable:  # TODO: write dict condition
                self.variables[i] += delta
            elif self.matrix[variable][i] is None:
                pass
            else:
                self.variables[i] += self.matrix[variable][i](delta)                


    def hist(self):
        """
        plot matplotlib histogram
        :returns: fig
        """
        pass

    def glyph(self):
        """
        plots hier-o-glyph from criteria vector
        """
        pass
