import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def _generate_counter(df_treat, counterfa):
    """
    Combine estimated counterfactual outcomes 
    with previous true outcomes for the treated 
    unit.
    """
    t_complete = df_treat.shape[0]
    t_replace = counterfa.shape[0]
    untreat = df_treat[:t_complete - t_replace]
    np_syn = np.concatenate((untreat.values, counterfa.reshape(-1,1)), axis=0)
    df_syn = pd.DataFrame(np_syn)
    
    return df_syn

def plot_df(df, title, df_treat, counterfa, save_fig=False, case=None):
    """
    This function is used to plot example panel data for both control units 
    and treated unit, and furthermore the counterfactual outcomes estimated
    by a base learner.
    
    Arguments:
        df (pd.DataFrame): Control units data of one data draw.
        title (string): Graph title.
        df_treat (pd.DataFrame): Treated unit data of one data draw.
        counterfa (np.ndarray): Counterfatual outcomes with previous
                        outcomes of treated unit.
        save_fig (boolean): If True, save the figure to output/figures 
                directory;if False, only demonstrate plot.
        case (string): Only used when save_fig=True, default by None. This
                argument will give the saved figure a name labeled by
                it.
    Return:
        Plot the figure and one can store it in output/figures directory.
    """
    # Combination counterfactual outcomes and previous true outcomes.
    df_counterfa = _generate_counter(df_treat, counterfa)
    
    # Create plots on the axis.
    ax = df.iloc[2:,:].T.plot(figsize=(8, 6), color='grey')
    ax.plot(df.iloc[0:2,:].T, color='red', lw=2)
    ax.plot(df_treat, color='black', lw=2, label='Treated unit')
    ax.plot(df_counterfa, color='black', ls='--', label='Counterfactual')
    ax.set_xlabel('Time', fontsize=16)
    ax.set_ylabel('Outcome', fontsize=16)
    ax.set_title('{}'.format(title), fontsize=18)
    
    # Create legends.
    lines = [Line2D([0], [0], color='k', linewidth=3), Line2D([0], [0], color='k', linewidth=3, ls='--')]
    labels = ['Treated unit', 'Counterfactual']
    ax.legend(lines, labels, loc='lower right', fontsize=12)
    
    # Save figure.
    if save_fig:
        if type(case) == str:
            fig = plt.gcf()
            fig.savefig(f'output/figures/fig_{case}.png')
        else:
            print('Image saving failed: please specify the name!')