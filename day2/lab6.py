#you jog first mile at 7mph; then run next two at 15mph; before jogging the last
#will this be quicker or slower than the bus
distance=4
speed1=25
time=(4/speed1)*60
total_time=time+(10*2)
speed2=7
time1=(1/speed2)*60
speed3=15
time2=(2/speed3)*60
speed4=7
time3=(1/speed4)*60
totaltime1=time1+time2+time3
print("the total time to reach university by bus is:", total_time)
print("the total time to reach university by walking is:", totaltime1)
if totaltime1>total_time:
    print("walking is faster to reach to university")
else:
    print("going by bus is faster to reach to university")