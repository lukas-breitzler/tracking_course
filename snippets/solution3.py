#uncomment above to load a solution
for i in range(5):
    window_size=(i+1)*5

    an1s=moving_average_2d(an1,window_size)
    an2s=moving_average_2d(an2,window_size)

    # Calculate differences in smoothed x and y
    dxs = np.diff(an1s[:,0])
    dys = np.diff(an1s[:,1])
    distancess = np.sqrt(dxs**2 + dys**2)

    plt.plot(distancess[:300],label=window_size)
    
plt.legend()