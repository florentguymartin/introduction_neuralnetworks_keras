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

def distribution0_jam():
    return stats.norm.rvs(loc=25,scale=11)
def distribution0_normal():
    return stats.norm.rvs(loc=70,scale=20)

def distribution0():
    """Distribution 0."""
#     p=0.5
#     bernoulli = stats.bernoulli(p)
    if bernoulli.rvs():
        return distribution0_jam(), 'slow'
    else:
        return distribution0_normal(), 'normal'
    
def distribution1_jam():
    """Distribution of slow traffic."""
#     p=0.5
#     bernoulli = stats.bernoulli(p)
    if bernoulli.rvs():
        return stats.norm.rvs(loc=20,scale=8)
    else:
        return stats.norm.rvs(loc=60,scale=8)
    
def distribution1_normal():
    """Distribution of normal traffic."""
#     p=0.5
#     bernoulli = stats.bernoulli(p)
    if bernoulli.rvs():
        return stats.norm.rvs(loc=40,scale=8)
    else:
        return stats.norm.rvs(loc=80,scale=8)
    
def distribution1():
    """Distribution 1."""
#     p=0.5
#     bernoulli = stats.bernoulli(p)
    if bernoulli.rvs():
        return distribution1_jam(), 'slow'
    else:
        return distribution1_normal(),'normal'
    
def sample(distribution,n):
    samples= [distribution() for i in range(n)]
    df = pd.DataFrame(samples,columns=['coordinates','traffic'])
    return df

def plot_sample(distribution,n,size_point=4):
    data = sample(distribution,n)
    sns.set_context("talk",font_scale=3)
    palette = sns.color_palette("Set1")
    plt.figure(figsize=(20,13))
    ax=sns.swarmplot(x='coordinates',y='traffic',data=data,size=size_point,palette=palette)
    ax.yaxis.set_label_coords(1.05, 0.5)
    ax.set_xlim(0,100)
    ax.set_ylabel('')
    sns.despine(bottom=True,right=False)
    return None