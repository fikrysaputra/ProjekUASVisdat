from bokeh.plotting import figure, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, HoverTool, CustomJS, RangeSlider
from bokeh.models.widgets import Select, DateRangeSlider

def newCaseFigure(source, dropdown, dateSlider):

    # list tools
    TOOLS = "pan, reset, crosshair, wheel_zoom"

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
                           x_axis_label="Date", y_axis_label="New Case", x_axis_type="datetime", tools=TOOLS)

    # It adds the hover tool to the figure.
    figureNewCase.add_tools(HOVER)

    # It plots the line graph of the data in the source.
    figureNewCase.line('Date', 'NewCases',
                       source=source, line_color="red")
    
    figureNewCase.ygrid.band_fill_color = "#B7B7B7"
    figureNewCase.ygrid.band_fill_alpha = 0.1
    figureNewCase.xgrid.bounds = (2, 4)
    
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
    TOOLS = "pan, reset, crosshair, wheel_zoom"

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
                             x_axis_label="Date", y_axis_label="Death", x_axis_type="datetime", tools=TOOLS)

    # It adds the hover tool to the figure.
    figureNewDeaths.add_tools(HOVER)

    # It plots the line graph of the data in the source.
    figureNewDeaths.line('Date', 'NewDeaths',
                         source=source, line_color="#000000")

    figureNewDeaths.ygrid.band_fill_color = "#B7B7B7"
    figureNewDeaths.ygrid.band_fill_alpha = 0.1
    figureNewDeaths.xgrid.bounds = (2, 4)
    
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
    TOOLS = "pan, reset, crosshair, wheel_zoom"

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
                                x_axis_label="Date", y_axis_label="Recovered", x_axis_type="datetime", tools=TOOLS)

    # It adds the hover tool to the figure.
    figureNewRecovered.add_tools(HOVER)

    # It plots the line graph of the data in the source.
    figureNewRecovered.line('Date', 'NewRecovered',
                            source=source, line_color="green")
                            
    figureNewRecovered.ygrid.band_fill_color = "#B7B7B7"
    figureNewRecovered.ygrid.band_fill_alpha = 0.1
    figureNewRecovered.xgrid.bounds = (2, 4)
    
    # A callback function. It is called when the value of the date range slider is changed.
    callback = CustomJS(args=dict(p=figureNewRecovered), code="""
        console.log(p)
        p.x_range.start = cb_obj.value[0]
        p.x_range.end = cb_obj.value[1]
        p.x_range.change.emit()
        """)

    dateSlider.js_on_change('value_throttled', callback)

    return column(figureNewRecovered, dropdown, dateSlider)

def anggotaKelompok():

    x = ['Alif Adwitiya Pratama', 'Aliza Rizka Firdani', 'Muhamad Fikry Saputra'],
    y1 = [3]
    y2 = [2]
    y3 = [1]
    TOOLS = "pan, reset, crosshair, wheel_zoom"

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
    
    # create a new plot with a title and axis labels
    p = figure(title="Anggota Kelompok", plot_height=500, plot_width=500, x_axis_label='x', y_axis_label='y', tools=TOOLS)
    p.add_tools(HOVER)
    
    # add a line renderer with legend and line thickness to the plot
    p.circle(x, y1, legend_label="Alif Adwitiya Pratama - 1301190465", color="blue", line_width=2)
    p.circle(x, y2, legend_label="Aliza Rizka Firdani - 1301190297", color="red", line_width=2)
    p.circle(x, y3, legend_label="Muhamad Fikry Saputra - 1301194300", color="green", line_width=2)
    
    p.background_fill_color = (204, 255, 255)
    p.border_fill_color = (102, 204, 255)
    p.outline_line_color = (0, 0, 255)
    
    return p
