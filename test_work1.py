from work1 import weight_lifting

def test_work1():
    result = weight_lifting('male',55)
    assert result == '您已获得男子组参赛资格！'