import matplotlib.pyplot as plt

count = [11,15,21,17,21,21,12,15,13,18,13,19,14,12,18,13,16,21,20,22,21,18,15,8,12,6,20,28]
plt.figure(figsize = (10,10))
x = [x for x in range(1,29)]
for i in range(0,28):
    plt.annotate(count[i], xy = (x[i],count[i]+0.5),color = 'g')
plt.xlabel("Frames of a single second")
plt.ylabel("Vechicle count per 5 frame")
plt.grid()
plt.plot([i for i in range(1,29)],count,marker='o',color ='r')

plt.bar([i for i in range(1,29)],count,color ='pink')
plt.show()