'''
Visualization tools for MobileSensorData project
'''

import os
import numpy as np
import pandas as pd

from sklearn.decomposition import PCA

import plotly.graph_objects as go
import plotly.express as px

sensor_names = {
    'accm': 'Accelerometer',
    'gyrm': 'Gyroscope',
    'magm': 'Magnetometer',
    'grvm': 'Gravity Sensor',
    'lacm': 'Linear acceleration',
    'rotm': 'Rotation sensor',
}

sensor_colors = {
    'accm': 'b',
    'gyrm': 'g',
    'magm': 'r',
    'grvm': 'c',
    'lacm': 'm',
    'rotm': 'y',
}


def get_games(path):
    '''Get list of all games in the directory

    Parameters:
    - `path`: path to the directory

    Output:
    - `games`: list of games
    '''

    files = os.listdir(path)
    games = list(set([file[:-8] for file in files]))
    return games


def plot_time_sampling_stats(path, games=None, delimiter=',', decimal='.'):
    '''Plot sample length distribution

    Parameters:
    - `path': path to a folder containing .csv data of games
    - `games`: list of games that would be combined

    Notes:
    This function combines all games' data (only `time` column)
    into one pd.Dataframe.
    '''

    if games is None:
        print('No games was entered. '
              'All data will be processed.')
        games = get_games(path)

    game_data = pd.DataFrame()

    for game in games:
        for sensor in sensor_names:
            filename = path + game + sensor + '.csv'

            data = pd.read_csv(filename, delimiter=delimiter, decimal=decimal)
            time = data['time'].values
            samples = np.zeros([time.shape[0] - 1])
            for i in range(time.shape[0] - 1):
                samples[i] = time[i + 1] - time[i]

            game_data = game_data.append(pd.DataFrame({'time_samples': samples,
                                                       'sensor': [sensor_names[sensor]] * (time.shape[0] - 1),
                                                       'game': [game] * (time.shape[0] - 1)}),
                                         ignore_index=True)

    fig = px.histogram(game_data, x="time_samples",
                       color="sensor",
                       histnorm='percent',
                       template='plotly_white',
                       barmode='overlay')

    fig.for_each_trace(
        lambda trace: trace.update(name=trace.name.replace("=", ": ")),
    )

    fig.layout.yaxis.title.text = 'Count'
    fig.layout.xaxis.title.text = 'Time samples'
    fig.layout.height = 500

    fig.show()


def plot_game(path, game, sensors, delimiter=',', decimal='.'):
    '''Plot game data

    Parameters:
    - `path': path to a folder containing .csv data of games
    - `game`: name of game to be plotted
    - `sensors`: list of sensors
    - `delimiter`: csv-file delimiter
    - `decimal`: csv-file decimal delimiter
    '''

    for sensor in sensors:
        filename = path + game + sensor + '.csv'
        data = pd.read_csv(filename, delimiter=delimiter, decimal=decimal)

        fig = go.Figure()
        fig.add_scatter(x=data['time'], y=data['X_value'], mode='lines', name='X_value')
        fig.add_scatter(x=data['time'], y=data['Y_value'], mode='lines', name='Y_value')
        fig.add_scatter(x=data['time'], y=data['Z_value'], mode='lines', name='Z_value')

        fig.for_each_trace(
            lambda trace: trace.update(name=trace.name.replace("_value", "")),
        )

        fig.layout.template = 'plotly_white'

        fig.show()


def plot_phase_track(track, color=None):
    '''Plot given phase trajctory

    Parameters:
    - `track`: 3D or 2D phase trajectory
    '''

    fig = go.Figure()

    if track.shape[-1] == 2:
        fig.add_scatter(x=track[:, 0], y=track[:, 1],
                        marker_color=color,
                        mode='lines',
                        name='Phase track')

        fig.add_trace(go.Scatter(x=[track[0, 0]],
                                 y=[track[0, 1]],
                                 mode='markers',
                                 marker_size=10,
                                 marker_color='rgba(255, 10, 0, .7)',
                                 name='Start point'))

        fig.add_trace(go.Scatter(x=[track[-1, 0]],
                                 y=[track[-1, 1]],
                                 mode='markers',
                                 marker_size=10,
                                 marker_color='rgba(10, 250, 250, .7)',
                                 name='End point'))

    elif track.shape[-1] == 3:
        fig.add_scatter3d(x=track[:, 0], y=track[:, 1], z=track[:, 2],
                          marker_color=color,
                          mode='lines',
                          name='Phase track')

        fig.add_trace(go.Scatter3d(x=[track[0, 0]],
                                   y=[track[0, 1]],
                                   z=[track[0, 2]],
                                   mode='markers',
                                   marker_size=10,
                                   marker_color='rgba(255, 10, 0, .7)',
                                   name='Start point'))

        fig.add_trace(go.Scatter3d(x=[track[-1, 0]],
                                   y=[track[-1, 1]],
                                   z=[track[-1, 2]],
                                   mode='markers',
                                   marker_size=10,
                                   marker_color='rgba(10, 250, 250, .7)',
                                   name='End point'))

    else:
        raise ValueError('Check dimensionality of phase track')
        return

    fig.layout.template = 'plotly_white'
    fig.show()


def phase_track(series, l, n_components, plot_correlation_matrix=False):
    '''Get phase trajectory projection of series.

    Parameters:
    - `series`: 2Darray of shape [duration, 1]
    - `l`: dimensionality of feature space.
    - `n_components`: Number of components to keep
    while applying PCA to resulting trajectory.

    Output:
    - projection: projection of phase trajectory
    on the principal components.
    - basis: principal axes in feature space.
    '''

    phase = to_phase_space(series, l)

    if plot_correlation_matrix:
        plot_correlation(phase)

    model = PCA(n_components=n_components)
    projection = model.fit_transform(phase)
    basis = model.components_
    print('Explained variation'
          ' for {} principal components: {}'.format(n_components,
                                                    model.explained_variance_ratio_))
    print('Cumulative explained variation'
          'for {} principal components: {}\n'.format(n_components,
                                                     np.sum(model.explained_variance_ratio_)))
    return projection, basis


def plot_correlation(phase_track):
    '''Plot correlation matrix

    Parameters:
    - `phase_track`: phase trajectory
    '''

    fig = go.Figure(data=go.Heatmap(z=np.corrcoef(phase_track.T), colorscale='Viridis'))
    fig.update_layout(width=700, height=700, yaxis = dict({'autorange': 'reversed'}))
    fig.show()

def to_phase_space(series, l):
    '''Get phase trajectory of series.

    Parameters:
    - `series`: 2Darray of shape [duration, 1]
    - `l`: dimensionality of feature space.

    Output:
    - `phase`: phase trajectory
    '''

    phase = np.zeros([series.shape[0] - l, l])

    for i in range(0, series.shape[0] - l):
        phase[i] = np.squeeze(series[i:i + l, 0])
    return phase
