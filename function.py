import pandas as pd


def tprint(data: pd.DataFrame | list[list]):
    if isinstance(data, pd.DataFrame):
        columns = data.columns.tolist()
        rows = data.values.tolist()
    elif isinstance(data, list):
        columns = data[0]
        rows = data[1:]
    else:
        raise ValueError('El argumento debe ser un DataFrame o una lista')
    column_widths = [len(column) for column in columns]
    for row in rows:
        for i, cell in enumerate(row):
            column_widths[i] = max(column_widths[i], len(str(cell)))
    header = '║' + '║'.join(f" {column:{column_widths[i]}} " for i, column in enumerate(columns)) + '║'
    separator = '╠' + '╬'.join('═' * (width + 2) for width in column_widths) + '╣'
    top_separator = '╔' + '╦'.join('═' * (width + 2) for width in column_widths) + '╗'
    bottom_separator = '╚' + '╩'.join('═' * (width + 2) for width in column_widths) + '╝'
    
    print(top_separator)
    print(header)
    print(separator)
    
    for row in rows:
        row_str = '║' + '║'.join(f" {str(cell):{column_widths[i]}} " for i, cell in enumerate(row)) + '║'
        print(row_str)
    print(bottom_separator)


tprint(
    data=[
        ['Column A', 'Column B', 'Column C', 'Column D', 'Column E'],
        [1, 'Data 1', 4.5, True, 'X'],
        [2, 'Data 2', 5.5, False, 'Y'],
        [3, 'Data 3', 6.5, True, 'Z']
    ]
)

df = pd.DataFrame(
    {
        'Column A': [1, 2, 3],
        'Column B': ['Data 1', 'Data 2', 'Data 3'],
        'Column C': [4.5, 5.5, 6.5],
        'Column D': [True, False, True],
        'Column E': ['X', 'Y', 'Z']
    }
)
tprint(data=df)