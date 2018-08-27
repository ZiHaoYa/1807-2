z  = 1
while z <10:
	lie = 1
	while lie < z+1:
		h = z*lie
		print("%d*%d=%d"%(lie,z,h),end="\t")
		lie+=1
	print("")
	z+=1            
