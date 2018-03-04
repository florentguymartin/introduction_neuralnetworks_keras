import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
sns.set()
import matplotlib.pyplot as plt
import matplotlib

np.random.seed(0)
p=0.5
bernoulli = stats.bernoulli(p)
# Since we use np.random.seed(0), the following will always return the same thing
bernoulli.rvs(10)

def distribution0_jam(scale,mean=25):
    return stats.norm.rvs(loc=mean,scale=scale)

def distribution0_normal(scale,mean=25):
    return stats.norm.rvs(loc=mean,scale=scale)

def distribution0(scale=15,mean1=25,mean2=75):
    """Distribution 0."""
#     p=0.5
#     bernoulli = stats.bernoulli(p)
    if bernoulli.rvs():
        return distribution0_jam(scale,mean1), 'slow'
    else:
        return distribution0_normal(scale,mean2), 'normal'
    
def distribution1_jam(scale1=8,scale2=8):
    """Distribution of slow traffic."""
#     p=0.5
#     bernoulli = stats.bernoulli(p)
    if bernoulli.rvs():
        return stats.norm.rvs(loc=20,scale=scale1)
    else:
        return stats.norm.rvs(loc=60,scale=scale2)
    
def distribution1_normal(scale1=8,scale2=8):
    """Distribution of normal traffic."""
#     p=0.5
#     bernoulli = stats.bernoulli(p)
    if bernoulli.rvs():
        return stats.norm.rvs(loc=40,scale=scale1)
    else:
        return stats.norm.rvs(loc=80,scale=scale2)
    
def distribution1(scale=8):
    """Distribution 1."""
#     p=0.5
#     bernoulli = stats.bernoulli(p)
    if bernoulli.rvs():
        return distribution1_jam(scale,scale), 'slow'
    else:
        return distribution1_normal(scale,scale),'normal'

def raw_sample(distribution,n):
    samples= [distribution() for i in range(n)]
    df = pd.DataFrame(samples,columns=['coordinates','traffic'])
    return df    

def sample(distribution,n,scale=8):
    samples= [distribution(scale) for i in range(n)]
    df = pd.DataFrame(samples,columns=['coordinates','traffic'])
    return df

def plot_traffic(data,size_point=4,x_start=-10,x_end=110):
    sns.set_context("talk",font_scale=3)
    palette = sns.color_palette("Set1")
    fig = plt.figure(figsize=(20,13))
    ax=sns.swarmplot(x='coordinates',y='traffic',data=data,size=size_point,palette=palette)
    ax.yaxis.set_label_coords(1.05, 0.5)
    ax.set_xlim(x_start,x_end)
    ax.set_ylabel('')
    sns.despine(bottom=True,right=False)
    return fig

def plot_sample(distribution,n,size_point=4):
    data = sample(distribution,n)
    plot_traffic(data,size_point=4)
    return None