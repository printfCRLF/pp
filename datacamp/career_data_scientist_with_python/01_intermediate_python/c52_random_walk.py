import numpy as np
import matplotlib.pyplot as plt


def next_step():
    np.random.seed(123)
    random_walk = [0]

    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)

        if dice <= 2:
            step = step - 1
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)

        random_walk.append(step)

    print(random_walk)


def how_low_can_you_go():
    np.random.seed(123)
    random_walk = [0]

    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)

        random_walk.append(step)
    print(random_walk)

    return random_walk


def visualize_the_walk(walk):
    plt.plot(random_walk)
    plt.show()


if __name__ == "__main__":
    # next_step()
    random_walk = how_low_can_you_go()
    visualize_the_walk(random_walk)


