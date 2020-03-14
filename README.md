# Estimating Treatment Effects Using Ensemble Methods in Panel Data Context [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/lzl257/master_thesis_ensemble/master?filepath=00%20Select%20one%20senario.ipynb) 

This repository contains the codes I have used for simulation study in my master thesis. There are four main parts in sequence: data generating process --> estimating counterfactual outcomes of base learners --> training metalearner --> visualization and reporting.
Python and R are used for analysis.

## Get started

Usage of this repository is simple. Just click this [link](https://mybinder.org/v2/gh/lzl257/master_thesis_ensemble/master?filepath=00%20Select%20one%20senario.ipynb) or the binder badge beside the title above. Then you can select a senario and <img src="https://latex.codecogs.com/gif.latex?T_0" /> you are interested in. Then click the link below to enter the next notebook. I don't make the other notebooks run automatically because sometimes you can skip the time-consuming notebooks when the outputs are already avaiable. If you want to run one notebook, please follow `Kernel` --> `Restart & Run All` in the navigation bar. 

Since the environment for running code has already been created by [Binder](https://mybinder.readthedocs.io/en/latest/) in a docker, you don't have to install any package by yourself. The repository has already been built for an immediate use. It may takes 10-20 minutes to rebuild if the docker detects there is a new pushed commit.

## Structure of this repository

**Notebooks**

`00 Select one senario.ipynb`: A user interactive notebook where one can select senario and start point of treatment <img src="https://latex.codecogs.com/gif.latex?T_0" />.

`01 Data generating process.ipynb`: Data generating process for all senarios.

`02 Matrix completion without cross-validation.ipynb`: Estimate counterfactual outcomes of treated unit using matrix completion method (MC).

`03 Estimate counterfactual outcomes for each base learner.ipynb`: Estimate counterfactual outcomes using SC, MDD and Lasso.

`04 Matrix completion with cross-validation.ipynb`: (**Time-consuming!**) Estimate pseudo counterfactual outcomes in control group using MC.

`05 Stacking base learners.ipynb`: (**Time-consuming!**) Estimate pseudo counterfactual outcomes in control group using SC, MDD and Lasso.

`06 Visualization and generating report.ipynb`: Generate simulation results.

`07 Varying T0.ipynb`: An experiment where one can adjust the length of pretreatment periods.

`Figure in section 2.3.2.ipynb`: Figure 2.1 in the thesis.

**Source files**

`src`: Contains generated .csv data for senario A, B, C, D. JSON file stores the status selected in notebook 00.

`base_learners`: Stores the functions for loading data and bias-variance decomposition. Also stores the counterfactual outcomes estimated by MC.

`meta_learner/ensemble_mc`: Stores the leave-one-out pseudo counterfactual outcomes for all control units estimated by MC.

`visualization`: Contains all functions and class used for plotting.

`output`: Stores all outputs including figures and reports.

`examples`: An independent directory that stores the outputs used in the thesis.

`binder`: Contains the configuration files for the docker. No need to change.
