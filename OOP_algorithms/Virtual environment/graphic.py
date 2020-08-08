from bokeh.plotting import figure, output_file, show

#figure is the space where we can plot
#output_file allow type a name for the output archive
#show allow us to generate a server to print html output

if __name__ == '__main__':
    output_file('Graphic.html')
    fig = figure()

    total = int(input('How many values wish you plot?'))
    x_vals = list(range(total))
    y_vals = []

    for x in x_vals:
        value = int(input('Y value for {x}'))
        y_vals.append(value)

    #for this kind of graphics we need the following methods

    fig.line(x_vals, y_vals, line_width = 2)
    show(fig)
