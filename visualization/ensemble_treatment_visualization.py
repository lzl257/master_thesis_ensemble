import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def _autolabel(rects, ax):
    """For visualization 4: 
    Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def mse_comparison(mse_ate_en, mse_ate_syn, mse_ate_lasso, mse_ate_mc, mse_ate_mdd):
    """For visualization 4."""
    x = np.arange(mse_ate_en.shape[0])
    width = 0.15
    fig, ax = plt.subplots(figsize=(15, 7))
    rect1 = ax.bar((x+1) - width, np.around(mse_ate_en, decimals=2), width, label='Ensemble', align='center')
    rect2 = ax.bar((x+1), np.around(mse_ate_syn, decimals=2), width, label='Synthetic Control', align='center')
    rect3 = ax.bar((x+1) + width, np.around(mse_ate_lasso, decimals=2), width, label='Lasso', align='center')
    rect4 = ax.bar((x+1) + 2*width, np.around(mse_ate_mc, decimals=2), width, label='Matrix Completion',align='center')
    rect5 = ax.bar((x+1) + 3*width, np.around(mse_ate_mdd, decimals=2), width, label='Matching DID',align='center')

    _autolabel(rect1, ax)
    _autolabel(rect2, ax)
    _autolabel(rect3, ax)
    _autolabel(rect4, ax)
    _autolabel(rect5, ax)

    ax.set_xticks(x + 1)
    ax.set_title('MSE Comparison of Estimated Treatment Effect for Each Treatment Period', fontsize=18)
    ax.set_xlabel('Treatment Periods', fontsize=16)
    ax.set_ylabel('MSE', fontsize=16)

    ax.legend(loc='upper left')

    fig.savefig('output/figures/treatment_effects.png')

def ensemble_comparison(stacking_bias, stacking_var,
               boosting_bias, boosting_var,
               bagging_bias, bagging_var,
               T, T0, nonnegative, senario):
    """For visualization 3."""
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(16, 8))
    x_axis = np.arange(1, T - T0 + 1)

    ax1.plot(x_axis, boosting_bias, marker='o', color='orange', label='Boosting')
    ax1.plot(x_axis, bagging_bias, marker='^', color='green', label='Bagging')
    ax1.plot(x_axis, stacking_bias, marker='x', color='blue', label='Stacking')
    ax1.set_xlabel('Treatment Periods', fontsize=16)
    ax1.set_ylabel('Bias^2', fontsize=16)
    ax1.legend(fontsize=14)

    ax2.plot(x_axis, boosting_var, marker='o', color='orange', label='Boosting')
    ax2.plot(x_axis, bagging_var, marker='^', color='green', label='Bagging')
    ax2.plot(x_axis, stacking_var, marker='x', color='blue', label='Stacking')
    ax2.set_xlabel('Treatment Periods', fontsize=16)
    ax2.set_ylabel('Variance', fontsize=16)
    ax2.legend(fontsize=14)

    if nonnegative == True:
        fig.suptitle(f'Senario {senario}', fontsize=16)
    else:
        fig.suptitle(f'Senario {senario} (Without Nonnegative Constraint)', fontsize=18)

    plt.show()

    fig.savefig('output/figures/ensemble_comparison.png')
        
    
class BoxPlot:
    
    """Class for visualization 5.
    
    Attributes:
        estimation_list (list): [estimated array, true treatment effect, model name]
    """
    
    def __init__(self, estimation_dict, T, T0, nonnegative, senario):
        self.estimation_dict = estimation_dict
        self.T = T
        self.T0 = T0
        self.senario = senario
        self.nonnegative = nonnegative
    
    def models_long_table(self):
        models = []
        for model in (self.estimation_dict).values():           
            estimated_array, true_value, model_name = model
            treatment_periods = np.arange(1,self.T - self.T0 + 1)
            df_hat = pd.DataFrame(estimated_array, columns=treatment_periods)
            df_long = pd.melt(df_hat, value_vars=treatment_periods, var_name='treat_period', value_name='tau_hat')
            df_long['se'] = (df_long['tau_hat'] - true_value) ** 2
            df_long['model']=model_name
            
            models.append(df_long)

        self.models = models
    
    def stack_tables(self):
        self.models_long_table()
        table_list = self.models
        len_table = len(table_list)

        if len_table == 0:
            return print('There is no table for concatenation!')

        list_for_concat = []
        for i in np.arange(len_table):
            list_for_concat.append(table_list[i])
            df_for_box = pd.concat(list_for_concat).reset_index()

        return df_for_box
        
    def plot(self, df_for_box):
        # Use seaborn and matplotlib to visualize
        fig, ax = plt.subplots(figsize=(15, 7))
        sns.boxplot(x='treat_period', y='se', hue='model', data=df_for_box, ax=ax, showmeans=True,
                   meanprops={'marker':'D','markerfacecolor':'b', 'markeredgecolor':'b'})

        ax.set_ylim(-0.5, 11)
        ax.set_xlabel('Treatment Periods', fontsize=16)
        ax.set_ylabel('Squared Error of Estimated Treatment Effect', fontsize=16)

        if self.nonnegative == True:
            ax.set_title(f'Senario {self.senario}', fontsize=18)
        else:
            ax.set_title(f'Senario {self.senario} (Without Nonnegative Constraint)', fontsize=18)

        ax.legend(loc='upper left')

        fig.savefig('output/figures/treatment_effects_boxplot.png')

        plt.show()