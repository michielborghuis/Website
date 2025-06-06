import numpy as np
import csv
import matplotlib.pyplot as plt


def get_data():
    with open('verkeerssimulatie-rechteweg-snelheden.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        t = []
        v1 = []
        v2 = []
        v3 = []
        for row in reader:
            t.append(float(row[0]))
            v1.append(float(row[1]))
            v2.append(float(row[2]))
            v3.append(float(row[3]))
        print(np.array(t))
        print(np.array(v1))
        print(np.array(v2))
        print(np.array(v3))
        return (np.array(t), np.array(v1), np.array(v2), np.array(v3))


def plot_data(ys, xss, xrange, yrange):
    """Optionele argumenten xrange en yrange om ingezoomde plot te maken op de botsing"""
    for xs in xss:
        plt.plot(xs, ys)
    plt.xlim(xrange)
    plt.ylim(yrange)
    plt.ylabel("Speed")
    plt.xlabel("Times")
    plt.show()


def bereken_posities(times, speeds):

    posities = []
    for i in range(len(times) - 1):
        posities.append(speeds[i] * times[i])
    return posities


#         posities.append((speeds[i](times[i+1]-times[i]))+positie)
#         positie += (speeds[i](times[i+1]-times[i]))

def vind_botsing(t, car1, car2, car3):
    """ Geeft een vijf-tupel terug met de tijd van de botsing, de eerste auto (1,2 of 3),
        de positie van de eerste auto, de tweede auto en de positie daarvan."""
    for i in range(len(t) - 1):
        if car1[i] == car2[i]:
            return (t[i], 1, car1[i], 2, car2[i])
        elif car1[i] == car3[i]:
            return (t[i], 1, car1[i], 3, car3[i])
        elif car2[i] == car3[i]:
            return (t[i], 2, car2[i], 3, car3[i])
    return None  # (botsing_t, botsing_a, botsing_a_pos, botsing_b, botsing_b_pos)


def main():
    t, v1, v2, v3 = get_data()
    x1 = bereken_posities(t, v1)
    x2 = bereken_posities(t, v2)
    x3 = bereken_posities(t, v3)
    plot_data(np.delete(t, 0), [x1, x2, x3], (0, 13), (0, 13))


main()