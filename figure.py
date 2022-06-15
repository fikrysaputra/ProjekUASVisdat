from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, HoverTool, CustomJS
from bokeh.models.widgets import Select, DateRangeSlider


def newCaseFigure(source, dropdown, dateSlider):

    # list tools
    TOOLS = "pan,reset"

    # set hover
    HOVER = HoverTool(
        tooltips=[
            ('Date',   '@Date{%F}'),
            ('New Case', '@NewCases'),
        ],

        formatters={
            '@Date': 'datetime',
        },

        mode='vline'
    )

    # Creating a figure object with the given parameters.
    figureNewCase = figure(title="New Case Covid",
                           plot_height=500, plot_width=900,
                           x_axis_label="Tanggal", y_axis_label="New Case", x_axis_type="datetime", tools=TOOLS)

    # It adds the hover tool to the figure.
    figureNewCase.add_tools(HOVER)

    # It plots the line graph of the data in the source.
    figureNewCase.line('Date', 'NewCases',
                       source=source, line_color="#FF0000")

    # A callback function. It is called when the value of the date range slider is changed.
    callback = CustomJS(args=dict(p=figureNewCase), code="""
        console.log(p)
        p.x_range.start = cb_obj.value[0]
        p.x_range.end = cb_obj.value[1]
        p.x_range.change.emit()
        """)

    dateSlider.js_on_change('value_throttled', callback)

    return column(figureNewCase, dropdown, dateSlider)


def newDeathFigure(source, dropdown, dateSlider):

    # list unique location
    # list tools
    TOOLS = "pan,reset"

    # set hover
    HOVER = HoverTool(
        tooltips=[
            ('Date',   '@Date{%F}'),
            ('New Death', '@NewDeaths'),
        ],

        formatters={
            '@Date': 'datetime',
        },

        mode='vline'
    )

    # Creating a figure object with the given parameters.
    figureNewDeaths = figure(title="New Death",
                             plot_height=500, plot_width=900,
                             x_axis_label="Tanggal", y_axis_label="Death", x_axis_type="datetime", tools=TOOLS)

    # It adds the hover tool to the figure.
    figureNewDeaths.add_tools(HOVER)

    # It plots the line graph of the data in the source.
    figureNewDeaths.line('Date', 'NewDeaths',
                         source=source, line_color="#000000")

    # A callback function. It is called when the value of the date range slider is changed.
    callback = CustomJS(args=dict(p=figureNewDeaths), code="""
        console.log(p)
        p.x_range.start = cb_obj.value[0]
        p.x_range.end = cb_obj.value[1]
        p.x_range.change.emit()
        """)

    dateSlider.js_on_change('value_throttled', callback)

    return column(figureNewDeaths, dropdown, dateSlider)


def newRecoveredFigure(source, dropdown, dateSlider):

    # list tools
    TOOLS = "pan,reset"

    # set hover
    HOVER = HoverTool(
        tooltips=[
            ('Date',   '@Date{%F}'),
            ('New Recovered', '@NewRecovered'),
        ],

        formatters={
            '@Date': 'datetime',
        },

        mode='vline'
    )

    # Creating a figure object with the given parameters.
    figureNewRecovered = figure(title="New Recovered",
                                plot_height=500, plot_width=900,
                                x_axis_label="Tanggal", y_axis_label="Recovered", x_axis_type="datetime", tools=TOOLS)

    # It adds the hover tool to the figure.
    figureNewRecovered.add_tools(HOVER)

    # It plots the line graph of the data in the source.
    figureNewRecovered.line('Date', 'NewRecovered',
                            source=source)

    # A callback function. It is called when the value of the date range slider is changed.
    callback = CustomJS(args=dict(p=figureNewRecovered), code="""
        console.log(p)
        p.x_range.start = cb_obj.value[0]
        p.x_range.end = cb_obj.value[1]
        p.x_range.change.emit()
        """)

    dateSlider.js_on_change('value_throttled', callback)

    return column(figureNewRecovered, dropdown, dateSlider)
