"""

plot_parallel_coordinate
========================

.. autofunction:: optuna.visualization.matplotlib.plot_parallel_coordinate

The following code snippet shows how to plot the high-dimensional parameter relationships.

"""

import optuna


def objective(trial):
    x = trial.suggest_float("x", -100, 100)
    y = trial.suggest_categorical("y", [-1, 0, 1])
    return x**2 + y


sampler = optuna.samplers.TPESampler(seed=10)
study = optuna.create_study(sampler=sampler)
study.optimize(objective, n_trials=10)

optuna.visualization.matplotlib.plot_parallel_coordinate(study, params=["x", "y"])