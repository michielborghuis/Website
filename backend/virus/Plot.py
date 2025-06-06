import matplotlib.pyplot as plt


class Plot:
    pass


def plot(t, S, E, I, R, D):
    """Plots the graphs of the groups over time (t)."""
    f, ax = plt.subplots(1, 1, figsize=(10, 4))
    ax.plot(t, S, 'g', alpha=0.7, linewidth=2, label='Susceptible')
    ax.plot(t, E, 'y', alpha=0.7, linewidth=2, label='Exposed')
    ax.plot(t, I, 'r', alpha=0.7, linewidth=2, label='Infected')
    ax.plot(t, R, 'c', alpha=0.7, linewidth=2, label='Recovered')
    ax.plot(t, D, 'k', alpha=0.7, linewidth=2, label='Dead')
    ax.set_xlabel('Time (days)')

    legend = ax.legend(borderpad=2.0)
    legend.get_frame().set_alpha(0.5)

    plt.show()
