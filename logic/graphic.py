def remove_graphic(file_name):
    import os
    os.remove(file_name)

def save_graphic(sec ,pulsos, name):
    import matplotlib
    import matplotlib
    matplotlib.use('Agg')
    from matplotlib import pyplot as plt
    import uuid

    def get_x(i):
        return {'+': 1, '-': -1, '0': 0}.get(i)

    x = list(range(len(pulsos) + 1))
    y = list(map(get_x, pulsos))
    y += [y[-1]]

    plt.clf()
    plt.cla()
    plt.plot(x, y, drawstyle='steps-post', linewidth=3)
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.title(name)
    plt.grid(True)
    plt.yticks([-1, 0, 1])

    for i in range(len(sec)):
        text_x = x[i]

        if len(sec) < len(x) - 1:
            text_x += x[i+1] - .5

        plt.text(text_x + 0.5, max(y) + .05, str(sec[i]), ha='center', va='center')

    if len(sec) < len(x) - 1:
        plt.xticks([int(i) for i in range(len(x)) if i % 2 == 0])

    else:
        plt.xticks([int(i) for i in range(len(x))])
        
    
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False) 

    def random_name():
        return str(uuid.uuid4())
    
    file_name = 'static/' + random_name() + '.png'

    plt.savefig(file_name)

    return file_name

if __name__ == '__main__':
    pass
