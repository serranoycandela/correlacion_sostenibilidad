class CriteriaVector:

    def __init__(self, variables, matrix):
        self.variables = variables
        self.matrix = matrix

    def update(self, variable, delta):
        """ updates variables vector when delta applied to single variable

        :param variable: index for self.variables list, to be modified by delta
        :param delta: rate of change for criterion
        """
        if type(self.matrix) is dict:
            # if matrix is a dicit variable must be the key
            assert variable in self.matrix

            self.variables = [self.matrix[variable](v + delta)
                              for v in self.variables]
        else:
            # if matrix is a list variable is an index
            for i in range(len(self.variables)):
                if self.matrix[variable][i] is None:
                    self.variables[i] += delta
                else:
                    self.variables[i] += \
                        self.matrix[variable][i](delta)

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
