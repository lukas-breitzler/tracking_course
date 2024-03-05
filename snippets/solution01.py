#Or plot them separately 

fig,axes =plt.subplots(1,2, sharex=True, sharey=True) #create two subplots side by side

axes[0].scatter(an1[:,0], an1[:,1], s=0.01, alpha=0.5, color='g') #plot the first animal in green
axes[0].set_aspect('equal') #set axes to equal scale
axes[1].scatter(an2[:,0], an2[:,1], s=0.01, alpha=0.5, color='r') #plot the second animal in red
axes[1].set_aspect('equal')
