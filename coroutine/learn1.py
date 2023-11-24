
# 由于GIL的存在，导致Python多线程性能甚至比单线程更糟。（GIL: 全局解释器锁（英语：Global Interpreter Lock，缩写GIL），是计算机程序设计语言解释器用于同步线程的一种机制，它使得任何时刻仅有一个线程在执行。[1]即便在多核心处理器上，使用 GIL 的解释器也只允许同一时间执行一个线程。）

# 于是出现了协程（Coroutine）这么个东西。（协程: 协程，又称微线程，纤程，英文名Coroutine。协程的作用，是在执行函数A时，可以随时中断，去执行函数B，然后中断继续执行函数A（可以自由切换）。但这一过程并不是函数调用（没有调用语句），这一整个过程看似像多线程，然而协程只有一个线程执行.）

# 协程由于由程序主动控制切换，没有线程切换的开销，所以执行效率极高。对于IO密集型任务非常适用，如果是cpu密集型，推荐多进程+协程的方式。

# 在Python3.4之前，官方没有对协程的支持，存在一些三方库的实现，比如gevent和Tornado。3.4之后就内置了asyncio标准库，官方真正实现了协程这一特性。

# 而Python对协程的支持，是通过Generator实现的，协程是遵循某些规则的生成器。因此，我们在了解协程之前，我们先要学习生成器。

# 1. 生成器(Generator)

# 我们这里主要讨论yield和yield from这两个表达式，这两个表达式和协程的实现息息相关。

#   Python2.5中引入yield表达式，参见PEP342
#   Python3.3中增加yield from语法，参见PEP380，
# 方法中包含yield表达式后，Python会将其视作generator对象，不再是普通的方法。
def test():
    print("generator start")
    n = 1
    while True:
        yield_expression_value = yield n
        print("yield_expression_value = %d" % yield_expression_value)
        n += 1





if __name__ == '__main__':
    # ①创建generator对象
    generator = test()
    print(type(generator))

    print("\n---------------\n")

    # ②启动generator
    next_result = generator.__next__()
    print("next_result = %d" % next_result)

    print("\n---------------\n")

    # ③发送值给yield表达式
    send_result = generator.send(666)
    print("send_result = %d" % send_result)
