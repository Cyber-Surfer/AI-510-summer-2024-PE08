#train svm classifier
from sklearn import svm
#train data 10 is mappend to prediction 1
#train data 100 is mappend to prediction 0
train_data = [[10], [100]]
train_target = [1, 0]
clf = svm.SVC()
clf.fit(train_data, train_target)

#save trained classifier as joblib file for server to use
import joblib
joblib.dump(clf, "binary_clf.joblib")


