import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from matplotlib.colorbar import ColorbarBase
from matplotlib import patheffects

# Function to convert total cases into a readable format
def format_cases(number):
    if number >= 1e9:
        return f'{number / 1e9:.1f}B'
    elif number >= 1e6:
        return f'{number / 1e6:.1f}M'
    elif number >= 1e3:
        return f'{number / 1e3:.1f}K'
    else:
        return str(number)

# Function to add a text outline for better visibility on varied backgrounds
def add_text_outline(ax, text, xy, fontsize, color, outline_width, outline_color):
    """Add text with an outline to an axis."""
    # Add the text with the outline color
    ax.annotate(text, xy=xy, fontsize=fontsize, fontweight='bold', color=outline_color,
                va='center', ha='center', path_effects=[
                    patheffects.withStroke(linewidth=outline_width, foreground=outline_color)])
    # Add the text with the original color on top
    ax.annotate(text, xy=xy, fontsize=fontsize, fontweight='bold', color=color,
                va='center', ha='center')

# Function to create a legend with human-readable format ('M' for millions, 'B' for billions)
def create_readable_legend(fig, ax, data_column, cmap, title, vmin, vmax):
    # Create a normalization object with the data range
    norm = Normalize(vmin=vmin, vmax=vmax)

    # Create a scalar mappable object with the normalization and colormap
    sm = ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    # Define the number of ticks in the colorbar and create the tick labels
    num_ticks = 5
    ticks = np.linspace(vmin, vmax, num_ticks)
    tick_labels = [format_cases(tick) for tick in ticks]

    # Create the colorbar with the scalar mappable object
    cbar = fig.colorbar(sm, ax=ax, orientation='horizontal', fraction=0.036, pad=0.04, 
                        ticks=ticks, aspect=30)
    cbar.set_label(title)
    cbar.ax.set_xticklabels(tick_labels)