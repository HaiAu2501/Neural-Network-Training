import math

# F01
class SphereFunction:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def evaluate(self, x):
        return sum(xi**2 for xi in x)

# F02
class EllipsoidFunction:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def evaluate(self, x):
        return sum((i + 1) * (xi**2) for i, xi in enumerate(x))

# F03
class SumOfDifferentPowersFunction:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def evaluate(self, x):
        return sum(abs(xi) ** (i + 1) for i, xi in enumerate(x))

# F04
class QuinticFunction:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def evaluate(self, x):
        return sum(abs(xi**5 - 3*xi**4 + 4*xi**3 + 2*xi**2 - 10*xi - 4) for xi in x)

# F05
class DropWaveFunction:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def evaluate(self, x):
        numerator = 1 + math.cos(12 * math.sqrt(sum(xi**2 for xi in x)))
        denominator = 0.5 * sum(xi**2 for xi in x) + 2
        return 1 - numerator / denominator

# F06
class WeierstrassFunction:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.a = 0.5
        self.b = 3
        self.kmax = 20

    def evaluate(self, x):
        part1 = sum(sum(self.a**k * math.cos(2 * math.pi * self.b**k * (xi + 0.5)) 
                        for k in range(self.kmax + 1)) for xi in x)
        part2 = self.dimensions * sum(self.a**k * math.cos(2 * math.pi * self.b**k * 0.5) 
                                      for k in range(self.kmax + 1))
        return part1 - part2

# F07
class Alpine1Function:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def evaluate(self, x):
        return sum(abs(xi * math.sin(xi) + 0.1 * xi) for xi in x)

# F08
class AckleysFunction:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def evaluate(self, x):
        a = 20
        b = 0.2
        c = 2 * math.pi
        sum_sq_term = -b * math.sqrt(sum(xi**2 for xi in x) / self.dimensions)
        cos_term = sum(math.cos(c * xi) for xi in x) / self.dimensions
        return -a * math.exp(sum_sq_term) - math.exp(cos_term) + a + math.e

# F09
class GriewanksFunction:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def evaluate(self, x):
        sum_term = sum(xi**2 for xi in x) / 4000
        product_term = math.prod(math.cos(xi / math.sqrt(i+1)) for i, xi in enumerate(x))
        return sum_term - product_term + 1
    
# F10
class RastriginsFunction:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def evaluate(self, x):
        return sum((xi**2 - 10 * math.cos(2 * math.pi * xi)) for xi in x) + 10 * self.dimensions
    
# F11
class HappyCatFunction:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def evaluate(self, x):
        sum_sq = sum(xi**2 for xi in x)
        sum_x = sum(xi for xi in x)
        return (abs(sum_sq - self.dimensions)**(1/4)) + (0.5*sum_sq + sum_x) / self.dimensions + 0.5
    
# F12 
class HGBatFunction:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def evaluate(self, x):
        sum_sq = sum(xi**2 for xi in x)
        sum_x = sum(xi for xi in x)
        return (abs(sum_sq**2 - sum_x**2)**(1/2)) + (0.5*sum_sq + sum_x) / self.dimensions + 0.5

# F13
class RosenbrocksFunction:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def evaluate(self, x):
        return sum(100 * (x[i+1] - x[i]**2)**2 + (x[i] - 1)**2 for i in range(self.dimensions - 1))

# F14
class HighConditionedEllipticFunction:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def evaluate(self, x):
        return sum((10**6)**((i - 1)/(self.dimensions - 1)) * (xi**2) for i, xi in enumerate(x, start=1))

# F15
class DiscusFunction:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def evaluate(self, x):
        return 10**6 * x[0]**2 + sum(xi**2 for xi in x[1:])

# F16
class BentCigarFunction:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def evaluate(self, x):
        return x[0]**2 + 10**6 * sum(xi**2 for xi in x[1:])

# F17
class PermDBetaFunction:
    def __init__(self, dimensions, beta=0.5):
        self.dimensions = dimensions
        self.beta = beta

    def evaluate(self, x):
        return sum(
            sum((j**i + self.beta) * ((x[j-1] / j)**i - 1) for j in range(1, self.dimensions + 1))**2
            for i in range(1, self.dimensions + 1)
        )
    
# F18
class SchaffersF7Function:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def evaluate(self, x):
        sum_term = 0
        for i in range(self.dimensions - 1):
            si = math.sqrt(x[i]**2 + x[i+1]**2)
            sum_term += (si**0.5 + si**0.5 * math.sin(50 * si**0.2)**2)
        return (sum_term / (self.dimensions - 1))**2

# F19
class ExpandedSchaffersF6Function:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def g(self, x, y):
        return 0.5 + (math.sin(math.sqrt(x**2 + y**2))**2 - 0.5) / (1 + 0.001 * (x**2 + y**2))**2

    def evaluate(self, x):
        value = sum(self.g(x[i], x[i+1]) for i in range(self.dimensions - 1))
        value += self.g(x[self.dimensions - 1], x[0])  # wrap-around case for the last and first element
        return value

# F20
class RotatedHyperEllipsoidFunction:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def evaluate(self, x):
        return sum((self.dimensions + 1 - i) * (xi ** 2) for i, xi in enumerate(x, start=1))