#uncomment above to load a solution
 
# As always, let's first take a look where the animals went
# for example by using an x,y, scatter plot
# you can plot the two animals on top of each other in different colors for example.
 
plt.scatter(an1[:,0],an1[:,1],color='g',s=0.01)
plt.scatter(an2[:,0],an2[:,1],color='r',s=0.01)
 
plt.figure()
 
#or plot them separately
 
fig,axes =plt.subplots(1,2, sharex=True, sharey=True) #create two subplots side by side
 
axes[0].scatter(an1[:,0],an1[:,1],color='g',s=0.01, alpha = 1) #plot the first animal in green
axes[0].set_aspect('equal') #set axes to equal scale
axes[1].scatter(an2[:,0],an2[:,1],color='r',s=0.01, alpha = 1)
axes[1].set_aspect('equal')
