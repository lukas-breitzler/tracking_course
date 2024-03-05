#uncomment above to load a solution

plt.scatter(relativePos_pol_rot_cart[0],relativePos_pol_rot_cart[1],s=0.01,alpha=0.05)
plt.gca().set_aspect('equal')
plt.axhline(0,ls=':',c='gray') #some pretty visual guides
plt.axvline(0,ls=':',c='gray')

plt.figure() #generate a second figure

heatmap, xedges, yedges = np.histogram2d(relativePos_pol_rot_cart[0], relativePos_pol_rot_cart[1], bins=50)
plt.imshow(heatmap)