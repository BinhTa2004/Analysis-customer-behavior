from cvxopt import matrix, solvers

a = 4
x1 = [0, a, 1]
x2 = [a, 0, 1]
x3 = [2, 1, a]
y = [1, 1, -1]

Q = matrix([
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 0.0]
])

p = matrix([0.0, 0.0, 0.0, 0.0])

G = matrix([
    [0, -4, -1, -1],
    [-4, 0, -1, -1], 
    [2, 1, 4, 1]
], (3,4), 'd')


h = matrix([-1.0, -1.0, -1.0])
sol = solvers.qp(Q, p, G, h)

print(sol['x'])







# G = matrix([
#     [-y[0]*x1[0], -y[0]*x1[1], -y[0]*x1[2], -y[0]], 
#     [-y[1]*x2[0], -y[1]*x2[1], -y[1]*x2[2], -y[1]],  
#    [-y[2]*x3[0] , -y[2]*x3[1], -y[2]*x3[2], -y[2]]   
# ], (3,4), 'd')



# Get the parameters from the solution above
w = [sol['x'][0], sol['x'][1], sol['x'][2]]
b = sol['x'][3]

xnew = [3, 1, 0]
#f(x) = w^T * x + b
decision = sum(w[i] * xnew[i] for i in range(len(w))) + b

# Classify based on the sign of the decision function
ynew = 1 if decision >= 0 else -1

print(f"Decision value (f(x) = w^T * x + b): {decision}")
print(f"ynew for xnew {xnew}: {ynew}")
