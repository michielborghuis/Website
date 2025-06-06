import csv
import matplotlib.pyplot as plt
import numpy as np


def get_data():
    with open('verkeerssimulatie-rechteweg-posities.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        t = []
        v1 = []
        v2 = []
        csvfile.readline()
        for row in reader:
            if len(row) == 3:
                t.append(float(row[0]))
                v1.append(float(row[1]))
                v2.append(float(row[2]))
            elif row[0] == "=======":
                break
            else:
                continue
        return (np.array(t), np.array(v1), np.array(v2))


def plot_data(ys, xss):
    for xs in xss:
        plt.plot(xs, ys)
    plt.ylabel("Speed")
    plt.xlabel("Times")
    plt.show()


def bereken_deltas(times, positions):
    deltas = []
    for x in range(len(times) - 1):

        deltas.append((float(positions[x + 1]) - float(positions[x])) / (float(times[x + 1]) - float(times[x])))
    return np.array(deltas)

def main():
    t,v1,v2 = get_data()
    s1 = bereken_deltas(t,v1)
    s2 = bereken_deltas(t,v2)
    print(s1)
    plot_data(np.delete(t,0), [s1, s2])

print(main())