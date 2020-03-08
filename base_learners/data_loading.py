import os
import pandas as pd


def load_from_folder(path):
    """
    List filenames from the path and load them.
    """    
    data_list = []
    for filename in sorted(os.listdir(path), key=len):
        #print(filename)
        data = pd.read_csv(path + filename)
        data_list.append(data)
    
    return data_list


def load_data(senario):
    """
    Loading data for different senarios.
    Arguments:
        senario (string): Loading data from this senario.
    Return:
        control_list (list): Control units data.
        treat_list (list): Treat unit data with treatment.
        untreat_list (list): Treat units data without treatment.
    """
    path_control = f'src/Senario{senario}/control/'
    path_treat = f'src/Senario{senario}/treat/'
    path_untreat = f'src/Senario{senario}/untreat/'
    
    control_list = load_from_folder(path_control)
    treat_list = load_from_folder(path_treat)
    untreat_list = load_from_folder(path_untreat)
    
    return control_list, treat_list, untreat_list
    
    