import matplotlib
import matplotlib.pyplot as plt

def basic(columns=1):
    WIDTH= 14.4/columns
    HEIGHT= 8.9/columns

    #=======Font setup=======#
    plt.rc('font', family='Arial')
    plt.rc('font', size=15)
    plt.rc('xtick', labelsize=16)
    plt.rc('ytick', labelsize=16)
    # plt.rc('text', usetex= True)
    plt.rc('figure', figsize=(WIDTH, HEIGHT) ,titleweight='bold',titlesize=20)
    plt.rc('figure', autolayout=True,titlesize=20)
    plt.rc('axes', labelweight='bold',labelsize=16, titlesize=20)


    #=======Line2D===========#
    plt.rc('lines', linewidth=2)
    plt.rc('lines', markersize=6)
    plt.rc('legend', fontsize=14)
    plt.rc('mathtext', fontset='stix')
    plt.rc('mathtext', it= 'Arial:italic')
    plt.rc('mathtext', rm= 'Arial')


def custom_lineplot(ax, x, y, error, xlims, ylims, color='red'):
    """Customized line plot with error bars."""

    ax.errorbar(x, y, yerr=error, color=color, ls='--', marker='o', capsize=5, capthick=1, ecolor='black')

    ax.set_xlim(xlims)
    ax.set_ylim(ylims)

    return ax

def custom_scatterplot(ax, x, y, error, xlims, ylims, color='green', markerscale=100):
    """Customized scatter plot where marker size is proportional to error measure."""

    markersize = error * markerscale

    ax.scatter(x, y, color=color, marker='o', s=markersize, alpha=0.5)

    ax.set_xlim(xlims)
    ax.set_ylim(ylims)

    return ax

def custom_barchart(ax, x, y, error, xlims, ylims, error_kw, color='lightblue', width=0.75):
    """Customized bar chart with positive error bars only."""

    error = [np.zeros(len(error)), error]

    ax.bar(x, y, color=color, width=width, yerr=error, error_kw=error_kw, align='center')

    ax.set_xlim(xlims)
    ax.set_ylim(ylims)

    return ax

def custom_boxplot(ax, x, y, error, xlims, ylims, mediancolor='magenta'):
    """Customized boxplot with solid black lines for box, whiskers, caps, and outliers."""

    medianprops = {'color': mediancolor, 'linewidth': 2}
    boxprops = {'color': 'black', 'linestyle': '-'}
    whiskerprops = {'color': 'black', 'linestyle': '-'}
    capprops = {'color': 'black', 'linestyle': '-'}
    flierprops = {'color': 'black', 'marker': 'x'}

    ax.boxplot(y,
               positions=x,
               medianprops=medianprops,
               boxprops=boxprops,
               whiskerprops=whiskerprops,
               capprops=capprops,
               flierprops=flierprops)

    ax.set_xlim(xlims)
    ax.set_ylim(ylims)

    return ax


def stylize_axes(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.xaxis.set_tick_params(top='off', direction='out', width=1)
    ax.yaxis.set_tick_params(right='off', direction='out', width=1)
