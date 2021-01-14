#pandas_datareader is used to directly import finance data from sources via python
from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

startdt=datetime.datetime(2020,9,1)
enddt=datetime.datetime(2020,9,29)

#This would import data from a number of online sources. Currently supports Google Finance, 
#FRED and Kenneth French's data library ec
df=data.DataReader(name="GOOG",data_source="yahoo",start=startdt,end=enddt)


#df.index[df.Close > df.Open]

def inc_dec(c,o):
    if c>o:
        value = "Increase"
    elif c<o:
        value = "Decrease"
    else:
        value = "Equal"
    return value

hour_12=12*60*60*1000

df["Status"]=[inc_dec(c,o) for c,o in zip(df.Close, df.Open)]
df["Middle"]=(df.Open+df.Close)/2
df["Height"]=abs(df.Open-df.Close)

#sizing_mode  
p=figure(plot_width=1000, plot_height=300, x_axis_type="datetime", title = "Finance candlestick", sizing_mode="scale_width")
#p.grid.grid_line_color=None
p.grid.grid_line_alpha=0.3

p.segment(df.index,df.High,df.index,df.Low,color="blue")

#color codes are available in w3 school css color
p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"],
       hour_12,df.Height[df.Status=="Increase"],fill_color="#8FBC8F", line_color="black")

p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"],
       hour_12,df.Height[df.Status=="Decrease"],fill_color="#A52A2A", line_color="black")

script1, div1 = components(p)
cdn_js=CDN.js_files
#cdn_css=CDN.css_files

#output_file("candlestick.html")
#show(p)