""" import pandas as pd

tr = pd.read_csv("data/train.csv") """
""" res = tr.isnull().sum()

print(tr)
print(res) """

""" 
res = pd.crosstab(tr["Embarked"], tr["Survived"])
print(res)

res.columns = res.columns.map({0:"Dead", 1:"Alive"})
print (res)

res = pd.crosstab(tr["Age"], tr["Survived"])
print(res)

res.columns = res.columns.map({0:"Dead", 1:"Alive"})
print (res)

res = pd.crosstab(tr["Pclass"], tr["Survived"])
print(res)

res = pd.crosstab(tr["Sex"], tr["Survived"])
print(res)

tr["Title"] = tr.Name.str.extract(" ([A-Za-z]+)\.")
res = tr["Title"].value_counts()
print(res)

tr["Title"] = tr["Title"].replace(["Capt", "Col", "Countess", "Don","Dona", "Dr", "Jonkheer", "Lady","Major", "Rev", "Sir"], "Other")
tr["Title"] = tr["Title"].replace("Mlle", "Miss")
tr["Title"] = tr["Title"].replace("Mme", "Mrs")
tr["Title"] = tr["Title"].replace("Ms", "Miss")

res = tr["Title"].value_counts()
print(res)


print(tr["Age"].isnull().sum())
print(tr["Age"].isnull())


meanAge = tr[["Title", "Age"]].groupby(["Title"]).mean()
print(meanAge)


for index, row in meanAge.iterrows():
    nullIndex = tr[(tr.Title == index) & (tr.Age.isnull())].index
    # print(nullIndex, index, row[0])
    tr.loc[nullIndex, "Age"] = row[0] """

""" print(tr)
print(tr["Age"].head(20))
print(tr["Age"].isnull().sum()) """

""" tr["AgeCate"] = pd.qcut(tr.Age, 8, labels=range(1, 9))
print(tr.head())
print(tr.dtypes)

tr.AgeCate = tr.AgeCate.astype(int)
print(tr.head())
print(tr.dtypes)


tr["CabinCate"] = tr["Cabin"].str.slice(start=0, stop=1)
#print(tr["CabinCate"].value_counts())
print(tr)


tr["CabinCate"] = tr["CabinCate"].map({ "N": 0, "C": 1, "B": 2, "D": 3, "E": 4, "A": 5, "F": 6, "G": 7, "T": 8 })
 """
#print(tr.dtypes)
#print(tr)
#print(tr["CabinCate"].value_counts())


""" res = pd.crosstab(tr["CabinCate"], tr["Survived"])
print(res)


print(tr.Fare)

tr["FareCate"] = pd.qcut(tr.Fare, 8, labels=range(1, 9))
tr.FareCate = tr.FareCate.astype(int)
print(tr["FareCate"].value_counts())

res = pd.crosstab(tr["FareCate"], tr["Survived"])
print(res) """


""" 
df = pd.read_csv("./data/Iris.csv", index_col="Id")
print(df.head())

df.rename(columns={
    "SepalLengthCm": "꽃받침길이",
    "SepalWidthCm": "꽃받침너비",
    "PetalLengthCm": "꽃잎길이",
    "PetalWidthCm": "꽃잎너비", 
    "Species": "품종"},
    inplace=True
)
print(df.head())


res = df.iloc[:, [0, 1, 4]]
print(res)

df["품종"] = df["품종"].str[5:]
print(df)

res = df.groupby("품종").mean()
print(res)

res = df["품종"].value_counts()
print(res)
 """

""" import matplotlib.pyplot as plt """

""" 
value = [1, 2, 3, 4]
res = plt.plot(value)
plt.show()
"""

x_value = [2, 3, 6, 7, 10 ]
y_value = [1, 4, 5, 8, 9]

""" plt.plot(x_value, y_value)
plt.plot([2,3,6,7,10],[1,4,5,8,9])
plt.show()

dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
plt.plot("x_data", "y_data", data=dic_val)
plt.show()
 """
 
""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
plt.plot("x_data", "y_data", data=dic_val)
plt.xlabel("x_data",labelpad=15)
plt.ylabel("y_data",labelped=50)
plt.show()

plt.xlabel("x_data", labelped=10,loc="right")
plt.ylabel("y_data", labelped=15,loc="top")

plt.xlabel("x_data",labelped=20, loc="left")
plt.ylabel("y_data",labelped=10, loc="bottom")
 """

""" 
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val)
plt.plot("x1_data", "y1_data", data=dic1_val)
plt.xlabel("x_data")
plt.ylabel("y_data")
plt.show()
 """


""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y2_data": [2,4,6,8,10]}


plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
plt.plot("x1_data", "y1_data", data=dic1_val, label="value")
plt.xlabel("x_data")
plt.ylabel("y_data")

plt.legend()
plt.legend(loc=(1, 1)) """
""" plt.legend(loc=(0.5, 0.5))
plt.legend(loc=(0.3, 0.3))
plt.legend(loc="best")
plt.legend(loc="lower right")
plt.legend(loc="upper right")
plt.legend(loc="lower left")
plt.legend(loc="upper left") """

""" plt.legend(ncol=1)
plt.legend(ncol=2) """

#plt.legend(ncol=2, fontsize=10)

#plt.legend(ncol=2, fontsize=10, frameon=True)
#plt.legend(ncol=2, fontsize=10, frameon=False)

#plt.legend(ncol=2, fontsize=10, shadow=True)


""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)
plt.xlabel("x_data")
plt.ylabel("y_data")

#plt.xlim()
#plt.ylim()

x_min, x_max = plt.xlim()
y_min, y_max = plt.ylim()
print(x_min, x_max)
print(y_min, y_max)

plt.xlim(x_min - 0.6, x_max)
plt.ylim(y_min - 0.6, y_max)

plt.xlim([0, 10])
plt.ylim([0, 10])

plt.xlim([0, 50])
plt.ylim([0, 50])

#        x.min, x.max, y.min, y.max
plt.axis([0, 10, 0, 10])
plt.axis([-5, 10, -5, 10])
plt.axis([0, 20, 0, 50])

x_min,y_min,x_max,y_max = plt.axis()
print(x_min,y_min,x_max,y_max)

plt.axis("square")
plt.axis("scaled")
plt.axis("tight")
plt.axis("off")
plt.axis("auto")

plt.show() """


""" plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], "--", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], ";"," ." , label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")

plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="solid", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashed", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dotted", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashdot", label="PData(km)")

plt.show()
 """