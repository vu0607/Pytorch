class pheptinh:
    def __init__(self, phepcong, tru, nhan, chia):
        self.cong = phepcong
    def cong(a, b):
        sum = a + b
        return sum
    def tru(a, b):
        hieu = a - b
        return hieu


def tinhtonghieu():
    print('Tong cua a va b la ', pheptinh.cong(2,pheptinh.tru(1,3)))
tinhtonghieu()
     