import pandas as pd
import random


def mean(data):
    print(data.mean())


def std(data):
    print(data.std())


def minimum(data):
    print(data.min())


def maximum(data):
    print(data.max())


def load_data():
    df = pd.DataFrame()
    df['height'] = [72.1, 69.8, 63.2, 64.7]
    df['weight'] = [198, 204, 164, 238]
    return df


def get_user_input(prompt='Type a command: '):
    command = random.choice(['mean', 'std', 'minimum', 'maximum'])
    print(prompt)
    print('> {}'.format(command))
    return command


def build_a_command_line_app():
    # Add the missing function references to the function map
    function_map = {
        'mean': mean,
        'std': std,
        'minimum': minimum,
        'maximum': maximum
    }

    data = load_data()
    print(data)

    func_name = get_user_input()

    # Call the chosen function and pass "data" as an argument
    function_map[func_name](data)


build_a_command_line_app()
