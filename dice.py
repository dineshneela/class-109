import random
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
dice_result=[]
count=[]
for i in range(0,1000):

    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)
    count.append(i)
mean=sum(dice_result)/len(dice_result)
std_deviation=statistics.stdev(dice_result)
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)
print("median of the data is ",median)
print("mode of the data is ",mode)
print("mean of the data is ",mean)
print("standard devation of data is ",std_deviation)
first_stdev_start,first_stdev_end=mean-std_deviation,mean+std_deviation
second_stdev_start,second_stdev_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_stdev_start,third_stdev_end=mean-(3*std_deviation),mean+(3*std_deviation)
list_of_data_with_in_1_stdev = [result for result in dice_result if result > first_stdev_start and result < first_stdev_end]
list_of_data_with_in_2_stdev = [result for result in dice_result if result > second_stdev_start and result < second_stdev_end]
list_of_data_with_in_3_stdev = [result for result in dice_result if result > third_stdev_start and result < third_stdev_end]
print("{}% of data lies with in 1 standard deviation ".format(len(list_of_data_with_in_1_stdev)*100.0/len(dice_result)))
print("{}% of data lies with in 2 standard deviation ".format(len(list_of_data_with_in_2_stdev)*100.0/len(dice_result)))
print("{}% of data lies with in 3 standard deviation ".format(len(list_of_data_with_in_3_stdev)*100.0/len(dice_result)))
fig=ff.create_distplot([dice_result],["result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.17],mode="lines",name="stdev1"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode="lines",name="stdev1"))
fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.17],mode="lines",name="stdev2"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode="lines",name="stdev2"))
fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.17],mode="lines",name="stdev3"))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.17],mode="lines",name="stdev3"))
fig.show()
