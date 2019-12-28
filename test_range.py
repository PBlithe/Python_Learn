
def use_range():
    '''python内置range函数'''
    for i in range(5,10):
        print(i,end=' ')

class IterRange(object):

    def __init__(self,start,end):
        self.start = start -1
        self.end = end

    def __next__(self):
        self.start += 1
        if self.start >= self.end:
            raise StopIteration
        return self.start

    def __iter__(self):
        return self

class GenRange(object):
    '''使用生成器来模拟range函数'''
    def __init__(self,start,end):
        self.start = start -1
        self.end = end

    def get_num(self):
        while True:
            if self.start >= self.end -1 :
                break
            self.start += 1
            yield self.start

def get_num(start,end):
    start -= 1
    while True:
        if start >= end -1:
            break
        start += 1
        yield start

if __name__ == '__main__':
    use_range()
    print('\n--------------------')
    iter = IterRange(5,10)
    # print(next(iter),end=' ')
    # print(next(iter),end=' ')
    # print(next(iter),end=' ')
    # print(next(iter),end=' ')
    # print(next(iter),end=' ')
    print(list(iter))
    print(iter)
    print('--------------------')
    gen_f = get_num(5,10)
    print(list(gen_f))
    print(gen_f)
