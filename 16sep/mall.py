import pandas as pd
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt  

customer_data = pd.read_csv(r"C:\shaamilshan\16sep\Mall_Customers.csv")

x = customer_data.iloc[:, [3, 4]].values


wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_) 

# sns.set()
# sns.lineplot(x=range(1, 11), y=wcss, color="blue", marker='o')
# plt.title("The Elbow Point Graph")
# plt.xlabel("Number of clusters")
# plt.ylabel("WCSS")
# plt.show()


Clusters = 5
kmeans = KMeans(n_clusters=5,init='k-means++',random_state=0)
y = kmeans.fit_predict(x)
print(y)

plt.figure(figsize=(8,8))
plt.scatter(x[y==0,0],x[y==0,1],s=50,c='blue',label='Cluster 1')
plt.scatter(x[y==1,0],x[y==1,1],s=50,c='green',label='Cluster 2')
plt.scatter(x[y==2,0],x[y==2,1],s=50,c='pink',label='Cluster 3')
plt.scatter(x[y==3,0],x[y==3,1],s=50,c='black',label='Cluster 4')
plt.scatter(x[y==4,0],x[y==4,1],s=50,c='gray',label='Cluster 5')

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,c='red',label='centroids')
plt.title('Customer group')
plt.xlabel('Annual Income')
plt.show()
