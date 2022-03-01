import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go 
df=pd.read_csv("Data.csv")
height_list=df["Height(Inches)"].to_list()
height_mean=statistics.mean(height_list)
height_median=statistics.median(height_list)
height_mode=statistics.mode(height_list)
print("mean,median,mode of height is {},{},{} ".format(height_mean,height_median,height_mode))
height_std_dev=statistics.stdev(height_list)
height_first_std_start,height_first_std_end=height_mean-height_std_dev,height_mean+height_std_dev
height_second_std_start,height_second_std_end=height_mean-(2*height_std_dev),height_mean+(2*height_std_dev)
height_third_std_start,height_third_std_end=height_mean-(3*height_std_dev),height_mean+(3*height_std_dev)

height_list_data_within_first_std=[result for result in height_list if result > height_first_std_start and result<height_first_std_end]
height_list_data_within_second_std=[result for result in height_list if result > height_second_std_start and result<height_second_std_end]
height_list_data_within_third_std=[result for result in height_list if result > height_third_std_start and result<height_third_std_end]

print("{}% of data for height lies within 1 std dev".format(len(height_list_data_within_first_std)*100.0/len(height_list)))
print("{}% of data for height lies within 2 std dev".format(len(height_list_data_within_second_std)*100.0/len(height_list)))
print("{}% of data for height lies within 3 std dev".format(len(height_list_data_within_third_std)*100.0/len(height_list)))

fig=ff.create_distplot([height_list],["Height"],show_hist=False)
fig.add_trace(go.Scatter(x=[height_mean,height_mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[height_first_std_start,height_first_std_start],y=[0,0.17],mode="lines",name="std1"))
fig.add_trace(go.Scatter(x=[height_first_std_end,height_first_std_end],y=[0,0.17],mode="lines",name="std1"))
fig.add_trace(go.Scatter(x=[height_second_std_start,height_second_std_start],y=[0,0.17],mode="lines",name="std2"))
fig.add_trace(go.Scatter(x=[height_second_std_end,height_second_std_end],y=[0,0.17],mode="lines",name="std2"))
fig.add_trace(go.Scatter(x=[height_third_std_start,height_third_std_start],y=[0,0.17],mode="lines",name="std3"))
fig.add_trace(go.Scatter(x=[height_third_std_end,height_third_std_end],y=[0,0.17],mode="lines",name="std3"))
fig.show()