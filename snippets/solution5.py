#uncomment above to load a solution

#first, transform relative positions to polar
relativePos_pol=cart2pol(relativePos[:,0],relativePos[:,1])
print('Polar coordinates: ',relativePos_pol)

#now do the rotation.
#hint: you have to combine the polar coordinates with the headings.
#but there is a catch: the vectors don't have the same length. remember why?
#just drop the last position. to use all of a vector except the last entry, use this index: v[:-1]

relativePos_pol_rot=relativePos_pol[0][:-1]-headingss
print('Polar coordinates rotated: ', relativePos_pol_rot)