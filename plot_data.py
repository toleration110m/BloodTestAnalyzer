import matplotlib.pyplot as plt


def plot_data_col(data_list, col_index):
    x_data = []
    y_data = []
    upper_limit = []
    lower_limit = []

    for index, data in enumerate(data_list):
        if index:
            if data[col_index] is not None:
                x_data.append(data[0])
                y_data.append(data[col_index])
                lower_limit.append(data[col_index - 2])
                upper_limit.append(data[col_index - 1])

    # x_data = pd.to_datetime(x_data)

    # Enable interactive mode
    plt.ion()

    # define here the dimension of your figure
    fig = plt.figure()
    plt.plot(x_data, y_data, 'b*-')
    plt.plot(x_data, lower_limit, 'r--')
    plt.plot(x_data, upper_limit, 'r--')
    plt.xlabel('Date')
    plt.title(data_list[0][col_index])
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.pause(1)

    return fig
