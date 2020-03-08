import numpy as np

def get_ate(counter, control_data, treat_data, untreat_data, T0):
    sample_size=len(control_data)
    T = control_data[0].shape[1]
    ate_hat = np.zeros((sample_size, T - T0))
    ate = np.zeros((sample_size, T - T0))

    for i in np.arange(sample_size):
        # Treated outcome
        y_one = treat_data[i].values.reshape(-1,)[T0:]

        # Estimated ATE
        y_hat_zero = counter[i]
        tau_hat = y_one - y_hat_zero

        # True ATE
        y_zero = untreat_data[i].values.reshape(-1,)[T0:]
        tau = y_one - y_zero

        ate_hat[i,:] = tau_hat
        ate[i,:] = 20
        
    return ate_hat, ate


def report_ate(pre_ate, control_idx_list=None, output=False):    
    mean_ate = np.mean(np.mean(pre_ate, axis=0))
    std_ate = np.mean(np.std(pre_ate, axis=0))
    sum_treat = np.sum(np.mean(pre_ate, axis=0))

    if output:
        return mean_ate, std_ate, sum_treat
    else:
        print('Mean of ate:', mean_ate)
        print('Standard deviation of ate:', std_ate)
        print('Sum of average treatment effect:', sum_treat)
        if control_idx_list == None:
            print('No available weights for reporting!')
        else:
            ave_number_control = np.mean(control_idx_list)    
            print('Number of controls with weights above 1%:', ave_number_control)


def count_coefs(coefs):
    """
    Count coefs which above 1%.
    """
    number_of_control = []
    for coef in coefs:
        num_control = len(np.where(~(coef < 0.01))[0])
        number_of_control.append(num_control)

    return number_of_control


def tradeoff(pre_ate, true_ate, sample_size, show_mse=False):    
    # Bias
    mean_tau_hat = np.mean(pre_ate, axis=0)
    mean_tau = np.mean(true_ate, axis=0)  # Fixed
    bias_square = (mean_tau - mean_tau_hat) ** 2

    # Variance
    var_tau_hat = np.var(pre_ate, axis=0)

    # Verification: MSE
    mse = np.sum((true_ate - pre_ate) ** 2, axis=0) / sample_size
        
    if show_mse:
        return mse, bias_square, var_tau_hat
    
    else:
        print('Bias^2:\n', bias_square)
        print('\n')
        print('Variance:\n', var_tau_hat)
        print('\n')
        print('Bias^2 + Variance:\n', bias_square + var_tau_hat)
        print('\n')
        print('MSE for verification:\n', mse)