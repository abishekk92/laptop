from scipy import stats
from pylab import plot,show
train_data=map(lambda x:map(lambda y:float(y),x.strip().split(',')),open('train.txt','r').readlines())
charged_for,lasted_for=[],[]
for time in train_data:
	charged_for.append(time[0])
	lasted_for.append(time[1])
slope,intercept,r,p,err=stats.linregress(charged_for,lasted_for)
charged=float(raw_input())
will_last=intercept+slope*charged
print will_last

