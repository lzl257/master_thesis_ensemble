import numpy as np
import matplotlib.pyplot as plt

def overfitting_plot(overfitting, out_best_report):
    dict_len = len(overfitting)
    overfit_for_plot = np.zeros((dict_len,))
    gap_for_plot = np.zeros((dict_len,))
    for i in np.arange(dict_len) + 1:
        overfit_for_plot[i - 1] = overfitting[f'{i}']['total']
        gap_for_plot[i - 1] = out_best_report[f'{i}']['Gap']

    fig, ax = plt.subplots(figsize=(8,8))
    ax.scatter(overfit_for_plot, gap_for_plot)
    ax.set_xlabel('Overfitting', fontsize=16)
    ax.set_ylabel('Bset.Individual.MSE - Best.Ensemble.MSE', fontsize=16)
    ax.set_title('Influence of Overfitting on Ensemble', fontsize=18)
    ax.axhline(y=0, ls='--', color='k')
    ax.axvline(x=0, ls='--', color='k')

    fig.savefig('output/figures/overfitting.png')

def ensemble_gap_plot(out_best_report):
    dict_len = len(out_best_report)
    gap_for_plot = np.zeros((dict_len,))
    for i in np.arange(dict_len) + 1:
        gap_for_plot[i - 1] = out_best_report[f'{i}']['Gap']
    x = np.arange(gap_for_plot.shape[0])

    fig, ax = plt.subplots(figsize=(8,8))
    ax.bar(x + 1, gap_for_plot, width=0.35)
    ax.set_title('Counterfactual Predictions: Individual vs. Ensemble', fontsize=18)
    ax.set_xlabel('Data Draw', fontsize=16)
    ax.set_ylabel('Best.Individual.MSE - Best.Ensemble.MSE', fontsize=16)
    ax.set_xticks(x + 1)
    ax.locator_params(nbins=10)
    ax.axhline(y=0, ls='-', color='k', lw=1)

    fig.savefig('output/figures/direct_predictions.png')