from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ortools.sat.python import cp_model


def AustraliaMapColoring(color=3):
    # 创建模型
    model = cp_model.CpModel()

    # 创建变量
    WA = model.NewIntVar(0, color - 1, 'WA')
    NT = model.NewIntVar(0, color - 1, 'NT')
    SA = model.NewIntVar(0, color - 1, 'SA')
    Q = model.NewIntVar(0, color - 1, 'Q')
    NSW = model.NewIntVar(0, color - 1, 'NSW')
    V = model.NewIntVar(0, color - 1, 'V')
    T = model.NewIntVar(0, color - 1, 'T')

    # 添加约束
    model.Add(WA != NT)
    model.Add(WA != SA)
    model.Add(SA != NT)
    model.Add(Q != NT)
    model.Add(SA != Q)
    model.Add(SA != NSW)
    model.Add(SA != V)
    model.Add(Q != NSW)
    model.Add(NSW != V)

    # 求解
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.MODEL_SAT:
        print('WA = %i' % solver.Value(WA))
        print('NT = %i' % solver.Value(NT))
        print('SA = %i' % solver.Value(SA))
        print('Q = %i' % solver.Value(Q))
        print('NSW = %i' % solver.Value(NSW))
        print('V = %i' % solver.Value(V))
        print('T = %i' % solver.Value(T))
    else:
        print("No feasible solution")


if __name__ == '__main__':
    AustraliaMapColoring()
