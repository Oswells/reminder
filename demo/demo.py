from emailreminder import reminder

email = '1652094603@qq.com'

@reminder(email=email, url='https://www.zjunjie.top/email', language='ch', name='demo1')
def demo1(x):
    return x+x

@reminder(email=email, url='https://www.zjunjie.top/email', language='en', name='demo2')
def demo2(x):
    raise ValueError

if __name__ == "__main__":
    print(demo1(3))
    demo2(4)