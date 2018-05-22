import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

colors = ['#EE3224', '#F78F1E', '#FFC222', '#76D7C4', '#5DADE2', '#D2B4DE']

def barplot_group(df, xval, yval, groupval, title = "", ylabel = ""):
    
    #Position and size of the bars
    firstGroup = df[groupval][0]
    pos = list(range(len(df[(df[groupval]==firstGroup)])))
    width = 0.20


    fig, ax = plt.subplots(figsize=(10,5))

    groups = df[groupval].unique()
    i=0
    for g in groups:
        plt.bar([p + width*i for p in pos], df[(df[groupval]==g)][yval], width, alpha=0.5, color=colors[i]) 
        i = i + 1

    # Set the y axis label
    ax.set_ylabel(ylabel)

    # Set the chart's title
    ax.set_title(title)

    # Set the position of the x ticks
    ax.set_xticks([p + 1.5 * width for p in pos])

    # Set the labels for the x ticks
    ax.set_xticklabels(df[xval].unique())

    # Setting the x-axis and y-axis limits
    plt.xlim(min(pos)-width, max(pos)+width*4)
    plt.ylim([0, max(df[yval])*2])

    # Adding the legend and showing the plot
    plt.legend(df[groupval].unique(), loc='upper left')
    plt.grid()
    plt.show()