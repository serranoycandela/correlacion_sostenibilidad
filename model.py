class CriteriaVector:

    def __init__(self, criteria, matrix):
        self.criteria = criteria
        self.matrix = matrix

    def update(self, criterion, delta):
        """ updates criteria vector when delta applied to criterion

        :param criterion: index for self.criteria list, to be modified by delta
        :param delta: rate of change for criterion
        """

    def hist(self):
        """
        plot matplotlib histogram
        :returns: fig?
        """

    def glyph(self):
        """
        plots hier-o-glyph from criteria vector
        """
