#uncomment above to load a solution

# lets calculate the **observed** distance between the two animals:

diff_12=an1-an2
dist=np.sqrt(diff_12[:,0]**2+diff_12[:,1]**2)
print(dist)