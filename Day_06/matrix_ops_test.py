import pytest
from matrix_ops import Matrix


def test_cell():
    matrix = Matrix([[1,2,3],[4,5,6]])
    assert matrix.cell((0,0)) == 1
    assert matrix.cell((1,1)) == 5
    assert matrix.cell((-1,0)) == None
    assert matrix.cell((99,99)) == None


def test_rng():
    matrix_1 = []
    for y in range(20):
        row = []
        for x in range(20):
            row.append(x + 19*y)
        matrix_1.append(row)
    matrix = Matrix(matrix_1)
    assert matrix.cell((0,0)) == 0
    assert matrix.cell((19,19)) == 19*19 + 19
    
    assert matrix.rng((0,0),(0,0)) == [0]
    assert matrix.rng((-2,0),(1,0)) == [None, None,0,1]
    assert matrix.rng((0,0),(5,0)) == [0,1,2,3,4,5]
    assert matrix.rng((0,0),(0,5)) == [0, 19, 38, 57, 76, 95]
    assert matrix.rng((0,-1),(0,5)) == [None, 0, 19, 38, 57, 76, 95]

def test_prt():
    matrix = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    assert matrix.prt() == "123\n456\n789"


def test_prt_p():
    matrix = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    assert matrix.prt_p((1,1)) == "123\n4*6\n789"

