!pip install sympy
import sympy
#program to determine evolutionarily stable strategies from a payoff matrix (refer to (Broom & Cannings, 2010))
def find_ess(payoff_matrix): #needs to be reprogrammed to accept an arbitrary number of strategies
    #find a nash equilibrium by setting population values equal to each other and solving for percentages
    population_1, population_2, population_3 = sympy.symbols('x y z')
    equation1 = sympy.Eq(payoff_matrix[0][0]*population_1 + payoff_matrix[0][1]*population_2 + payoff_matrix[0][2]*population_3, payoff_matrix[1][0]*population_1 + payoff_matrix[1][1]*population_2 + payoff_matrix[1][2]*population_3)
    equation2 = sympy.Eq(payoff_matrix[1][0]*population_1 + payoff_matrix[1][1]*population_2 + payoff_matrix[1][2]*population_3, payoff_matrix[2][0]*population_1 + payoff_matrix[2][1]*population_2 + payoff_matrix[2][2]*population_3)
    populations_solved = sympy.solve((equation1, equation2), (population_1, population_2, population3)
    population_ratios = sympy.solve((equation1.subs(population_1 = 1), equation2.subs(population_1 = 1)), (population_2, population_3))
    return population_ratios
    #determine the stability of the nash equilibrium by creating a C matrix. eigenvalues must all be negative for the nash equilibrium to be an ess
    
