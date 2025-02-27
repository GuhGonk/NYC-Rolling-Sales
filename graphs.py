import pandas as pd
import polars as pl

import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, DateFormatter
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class MatPlot:
    def makePlot(chart, data, x, y, title: str, xticks, xlabel, xrot, ylabel, leg_on: bool, leg_pos=None, leg_outer=None, leg_labels=None, hue=None, palette=None, ax=None, leg_bbox=None):
        match chart:
            case 'line':
                graph = sns.lineplot(
                    data=data,
                    x=x,
                    y=y,
                    hue=hue,
                    palette=palette,
                    marker='o',
                    ax=ax
                )
            case 'bar':
                graph = sns.barplot(
                    data=data,
                    x=x,
                    y=y,
                    hue=hue,
                    palette=palette,
                    ax=ax
                )

        graph.set_title(title)
        graph.set_xlabel(xlabel)
        graph.set_xticks(xticks)
        graph.set_xticklabels(labels=xticks, rotation=xrot)
        graph.set_ylabel(ylabel)
        graph.grid(True, alpha=0.3)

        if leg_on == True:
            if leg_outer == True:
                sns.move_legend(
                    graph, 
                    leg_pos,
                    bbox_to_anchor=leg_bbox,
                    labels=leg_labels
                )
            else:
                sns.move_legend(
                    graph,
                    leg_pos,
                    labels=leg_labels
                )
        
        return graph
    
class Plotly:
    def makeplot()