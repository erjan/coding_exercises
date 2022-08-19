
import cProfile
import pstats

def f1():
    s = 0
    for x in range(1000000):
        s += x*x
    return s



def f2():
    s = 0
    for x in range(1000000):
        s += x**2
    return s

if __name__ == '__main__':

    for f in (f1,f2):
        prof = cProfile.Profile()
        prof.enable()
        f()
        prof.disable()

        stats = pstats.Stats(prof)


        print(f"{f.__name__:20s} {stats.total_tt *1e3:.1f} ms")    

