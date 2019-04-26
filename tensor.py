import numpy as np
from numpy import linalg
### Class for tensor object

class Tensor:
    def __init__(self, dimension, values, color):
        """
        Initialize the tensor object with dimension and values
        """
        try:
            dimension = int(dimension)
            if dimension >= 0:
                self.dimension = dimension
            else:
                raise Exception('Dimension should be non negative.')
        except:
            raise Exception('Invalid type of dimension.')

        try:
            self.values = np.asarray(values)
        except:
            raise Exception('Values should have similar structure to a {} tensor'.format(self.dimension))

        try:
            color = str(color)
            if isinstance(color, str):
                self.color = color
            else:
                raise Exception('Color should be a string.')
        except:
            raise Exception('Color should be a string')
        self.exp = self._calculate_exp()


    def _calculate_exp(self):
        """
        Calculate exp based on different concepts based on the dimension of the tensor
        scalar : value
        vector : length
        matrix : determinant
        """
        if self.dimension == 0:
            return float(self.values)
        elif self.dimension == 1:
            # length of the vector
            return linalg.norm(self.values)
        elif self.dimension == 2:
            # determinant of the matrix
            return linalg.det(self.values)
        else:
            return -1

    def _dot_product(self,Tensor):
        """
        dot product between 2 vectors
        """
        if self.dimension == Tensor.dimension == 1:
            self.exp = np.dot(self.values,Tensor.values)
        else:
            print("The dimensions of the vectors don't match")
    def _element_wise_add(self,Tensor)
        """
        addition between 2 tensor with same shape
        """
        if (self.dimension == Tensor.dimension) and (self.values.shape == Tensor.values.shape):
            self.values += a.values