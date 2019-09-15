import pandas
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

od = pandas.read_csv('overall_data.csv')

def runplt(minX=-1, minY=-30, maxX=1, maxY=30, size=None):
    plt.figure(figsize=size)
    plt.title('Correlation between EPSSurpriseDollar and DeltaOpen')
    plt.xlabel('EPSSurpriseDollar')
    plt.ylabel('DeltaOpen')
    plt.axis([minX - 1, maxX + 1, minY - 1, maxY + 1])
    return plt

x = od['EPSSurpriseDollar']
y = od['delta_open']

matrix_x = []
for i in range(len(x) - 1):
    matrix_x.append([x[i], y[i]])

model = linear_model.LinearRegression()
model.fit(matrix_x[:100], x[:100])

y_predict = model.predict(matrix_x[100:])
y_test = y[100:len(y) - 1]

print('Coefficients: {}'.format(model.coef_))
print('Mean Squared Error: %.2f' % mean_squared_error(y_test, y_predict))
print('variance score: %.2f' % r2_score(y_test, y_predict))

plt.scatter(x[100:len(x) - 1], y_test, color='black')
plt.plot(x[100:len(x) - 1], y_predict, color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()
