import numpy as np
from scipy.optimize import minimize

m = np.array([10, 20, 50])
s = np.array([2, 10, 20])
rho = np.array([
    [1.0, 0.0, 0.0],
    [0.0, 1.0, -0.6],
    [0.0, -0.6, 1.0]
])

n = len(m)
cov = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        cov[i, j] = rho[i, j] * s[i] * s[j]

def f_risk(w):
    var = np.dot(w.T, np.dot(cov, w))
    return np.sqrt(var)

def f_ret(w):
    return np.sum(m * w)

def f_neg_ret(w):
    return -f_ret(w)

cons_eq = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
bnds = ((0, 1), (0, 1), (0, 1))
w0 = [1/3, 1/3, 1/3]

print(f"{'Завдання:':<65}{'x1, x2, x3':<25}{'m_p (%)':<10}{'sigma_p (%)'}")

res_a = minimize(f_risk, w0, bounds=bnds, constraints=[cons_eq])
wa = res_a.x
print(f"{'а) Збереження капіталу':<65}{f'{wa[0]:.2f}, {wa[1]:.2f}, {wa[2]:.2f}':<25}{f_ret(wa):<10.2f}{res_a.fun:.2f}")

cons_b = [cons_eq, {'type': 'eq', 'fun': lambda w: f_ret(w) - 30}]
res_b = minimize(f_risk, w0, bounds=bnds, constraints=cons_b)
wb = res_b.x
print(f"{'б) Збільшення приросту капіталу при m_c = 30%':<65}{f'{wb[0]:.2f}, {wb[1]:.2f}, {wb[2]:.2f}':<25}{f_ret(wb):<10.2f}{res_b.fun:.2f}")

cons_c = [cons_eq, {'type': 'ineq', 'fun': lambda w: 15 - f_risk(w)}]
res_c = minimize(f_neg_ret, w0, bounds=bnds, constraints=cons_c)
wc = res_c.x
print(f"{'в) Максимального збільшення приросту капіталу при sigma_c = 15%':<65}{f'{wc[0]:.2f}, {wc[1]:.2f}, {wc[2]:.2f}':<25}{f_ret(wc):<10.2f}{f_risk(wc):.2f}")