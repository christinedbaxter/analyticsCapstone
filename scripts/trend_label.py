# Function to format the y-axis with 'K', 'M', 'B'
def human_readable_format(x, pos):
    if x >= 1e9:
        return f'{int(x*1e-9)}B'
    elif x >= 1e6:
        return f'{int(x*1e-6)}M'
    elif x >= 1e3:
        return f'{int(x*1e-3)}K'
    return str(x)

# Function to add human-readable labels to the min and max points on the graph
def add_min_max_labels(ax, xs, ys):
    min_val = ys.min()
    max_val = ys.max()
    
    # Add annotation for the minimum value
    min_idx = ys.argmin()
    ax.annotate(f'Min: {human_readable_format(min_val, None)}', 
                xy=(xs[min_idx], min_val), 
                xytext=(15, 15), 
                textcoords='offset points',
                arrowprops=dict(facecolor='black', shrink=0.05),
                ha='left', va='bottom')
    
    # Add annotation for the maximum value
    max_idx = ys.argmax()
    ax.annotate(f'Max: {human_readable_format(max_val, None)}', 
                xy=(xs[max_idx], max_val), 
                xytext=(15, -25), 
                textcoords='offset points',
                arrowprops=dict(facecolor='black', shrink=0.05),
                ha='center', va='top')