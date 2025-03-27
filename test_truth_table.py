from truth_table_and import and_1,or_1,not_1,xor_1,nand_1,nor_1,xnor_1
import pytest
@pytest.mark.parametrize("a,b,c",[(0,0,0),(0,1,0),(1,0,0),(1,1,1)])
def test_and(a,b,c):
    assert and_1(a,b)==c

@pytest.mark.parametrize("a,b,c",[(0,0,0),(0,1,1),(1,0,1),(1,1,1)])
def test_or(a,b,c):
    assert or_1(a,b)==c

def test_not():
    assert not_1(0)==1
    assert not_1(1)==0

@pytest.mark.parametrize("a,b,c",[(0,0,1),(0,1,1),(1,0,1),(1,1,0)])
def test_or(a,b,c):
    assert nand_1(a,b)==c

@pytest.mark.parametrize("a,b,c",[(0,0,1),(0,1,0),(1,0,0),(1,1,0)])
def test_or(a,b,c):
    assert nor_1(a,b)==c

@pytest.mark.parametrize("a,b,c",[(0,0,0),(0,1,1),(1,0,1),(1,1,0)])
def test_or(a,b,c):
    assert xor_1(a,b)==c

@pytest.mark.parametrize("a,b,c",[(0,0,1),(0,1,0),(1,0,0),(1,1,1)])
def test_or(a,b,c):
    assert xnor_1(a,b)==c