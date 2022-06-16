import pandas as pd
from figure import *
from bokeh.models.widgets import Tabs, Panel
from bokeh.io import curdoc


# Preprocess
df = pd.read_csv(
    './data/covid_19_indonesia_time_series_all.csv', parse_dates=['Date'])
pd.to_datetime(df['Date'])
df = df[['Date', 'Location', 'New Cases', 'New Deaths', 'New Recovered']].rename(
    columns={'New Cases': 'NewCases', 'New Deaths': 'NewDeaths', 'New Recovered': 'NewRecovered'})
LOCATIONLIST = df.Location.unique().tolist()

# It creates a dropdown menu
dropdown = Select(title="Location:", value=LOCATIONLIST[1],
                  options=LOCATIONLIST)

# A callback function. It is called when the value of the dropdown menu is changed.
def dropdownUpdate(attr, old, new):
    source.data = df[df.Location == dropdown.value]
dropdown.on_change('value', dropdownUpdate)

# It creates a date range slider with the given parameters.
dateSlider = DateRangeSlider(
    title="Date Range:", start=df.Date.min(), end=df.Date.max(), value=(df.Date.min(), df.Date.max())
)

# build source data
source = ColumnDataSource(df[df.Location == LOCATIONLIST[1]])

# It adds the layout to the current document.
l1 = newCaseFigure(source, dropdown, dateSlider)
l2 = newRecoveredFigure(source, dropdown, dateSlider)
l3 = newDeathFigure(source, dropdown, dateSlider)
l4 = anggotaKelompok()

tab1 = Panel(child=l4, title="Anggota")
tab2 = Panel(child=l1, title="New Cases")
tab3 = Panel(child=l2, title="New Recovered")
tab4 = Panel(child=l3, title="New Death")
tabs = Tabs(tabs=[tab1, tab2, tab3, tab4])

curdoc().add_root(tabs)
