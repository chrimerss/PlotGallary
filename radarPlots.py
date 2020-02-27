# Radar Plots

def radarChart(names, variables,save=False, saveName=None):
    '''
    Args:
    --------------------
    :names - list; containing ticklabels clock-wise from North
    :variables - list of arrays; values to put in the graph
    :save - bool; save graph
    '''
    #create background
    N= len(names)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    fig= plt.figure(figsize=(10,10))
    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    plt.xticks(angles[:-1], names)
    ax.set_rlabel_position(0)
    plt.yticks(np.arange(0,1,0.2), ['%.1f'%i for i in np.arange(0,1,0.2)], color="grey", size=12)
    plt.ylim(0,1)
    colors= ['blue', 'black', 'red']
    #add plots
    n_variables= len(variables)
    labels= ['mesonet', 'SMAP', 'NOAH']
    for n in range(n_variables):
        values= variables[n]
        values= [v.median() for v in values]
        values += values[:1]
        ax.plot(angles, values, linewidth=1, c=colors[n], linestyle='solid', label=labels[n])
        ax.fill(angles, values, colors[n], alpha=0.1,)
    plt.legend()
    if save:
        plt.savefig(saveName)

    return fig,ax

