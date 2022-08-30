import numpy as np
import matplotlib.pyplot as plt


def temp_tranform(temp, c2f=False):
    if c2f:
        res = temp * (9/5) + 32
    else:
        res = (temp - 32) / (9/5)
    return res


# task 2
def s(x):
    return 1 / (1 + np.exp(-x))


# task 3:
def nonlinfit(x, y, d=2):

    xp = np.linspace(np.min(x) - 1, np.max(x) + 1, 100)
    p = np.poly1d(np.polyfit(x, y, d))
    
    return xp, p



def main():
    # task 1:
    print(temp_tranform(30, c2f=True))
    print(temp_tranform(0, c2f=True))
    print(temp_tranform(80, c2f=False))
    
    # task 2
    print(s(0))
    print(s(2))
    print(s(100))
    v = np.arange(-10, 10, .01)
    res = list()
    for val in v:
        out = s(val)
        res.append(out)

    figure = plt.figure(figsize=(9,3))
    plt.plot(v, res)
    plt.savefig('sigmoid.png')
    plt.close()
    # task 3
    x = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
    y = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
    fig = plt.figure(figsize=(5, 4))
    for (i, color) in enumerate(['g', 'b']):
        xp, p = nonlinfit(x, y, d=i+1)
        plt.plot(x, y, 'r*', xp, p(xp), f'-{color}')
    
    plt.tight_layout()
    plt.savefig('nonline_fit.png')



if __name__ == "__main__":
    main()