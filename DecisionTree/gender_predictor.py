from sklearn import tree

#[height, weight, shoe-size]
X = [[170,65,30],[180,75,43],[190,80,50],[150,55,28],[170,68,32],[190,85,45],
[160,59,29],[167,63,37],[169,74,38],[150,45,25],[185,75,40],[155,47,29]]

Y = ['male','male','male','female','male','male','female','male','female','female','male','female']

classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(X, Y)

prediction = classifier.predict([[190, 75, 43]])

print prediction