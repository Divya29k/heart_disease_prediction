import argparse
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split

class PatientData:
    def __init__(self, input_data):
        self.data = pd.read_csv(input_data)
        
        
    def read_data():
        print(self.data)

    def find_counts(self, c):
        print(c)
        print(self.data[c].value_counts())

    def find_corr(self):
        print(self.data.corr())
    
    def plot(self, x, y, hue):
        sns.lmplot(x=x, y=y, hue=hue, data=self.data, fit_reg=False)
        plt.show()

    def drop(self,target_name):
        self.data=self.data.drop(['prevalentStroke'],axis=1)
        self.data=self.data.drop(['prevalentHyp'],axis=1)
        self.data=self.data.drop(['diabetes'],axis=1)
        self.data=self.data.drop(['totChol'],axis=1)
        self.data=self.data.drop(['education'],axis=1)
        self.data=self.data.drop(['currentSmoker'],axis=1)
        self.data=self.data.drop(['cigsPerDay'],axis=1)
        self.data=self.data.drop(['BPMeds'],axis=1)
        self.data=self.data.drop(['male'],axis=1)
        self.data=self.data.drop(['heartRate'],axis=1)
        self.data.dropna(subset = ["age"], inplace=True)
        self.data.dropna(subset = ["sysBP"], inplace=True)
        self.data.dropna(subset = ["diaBP"], inplace=True)
        self.data.dropna(subset = ["BMI"], inplace=True)
        self.data.dropna(subset = ["glucose"], inplace=True)
        self.data.dropna(subset = ["TenYearCHD"], inplace=True)
        X = data.drop(['TenYearCHD'],axis=1)
        y = data['TenYearCHD']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=17)
        print(self.data.info())
        sns.heatmap(self.data.corr())
        plt.show()
        #print(self.data)

        #print(self.data.drop([target_name], axis=1))

    
def main(args):
    pd = PatientData('framingham.csv')
    if args.show_data:
        pd.read_data()
    elif args.count:
        pd.find_counts(args.count)
    elif args.corr:
        pd.find_corr()
    elif args.plot:
        pd.plot(args.x, args.y, args.hue)
    elif args.drop:
        pd.drop(args.target_name)

if __name__ == '__main__':
    '''
    python chd_prediction.py --help

    python chd_prediction.py show_data --input <csv file>
    e.g. python chd_prediction.py show_data --input C:\MLP1\framingham.csv
   
    parser = argparse.ArgumentParser(description='TODO CHD dewsc')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
    parser.add_argument('--show_data', dest='command', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

    args = parser.parse_args()
    main(args.accumulate(args.integers))
    '''
    parser = argparse.ArgumentParser(description='TODO CHD desc')
    parser.add_argument("-sd", "--show_data", action="store_true")
    parser.add_argument("-count",type=str,required=False, help='count')  
    parser.add_argument("-corr",action="store_true",required=False, help='corr') 
    parser.add_argument("-plot",action="store_true",required=False, help='plot')
    parser.add_argument("-x",type=str,required=False, help='x-axis')
    parser.add_argument("-y",type=str,required=False, help='y-axis')  
    parser.add_argument("-hue",type=str,required=False, help='hue')  
    parser.add_argument("-drop",action="store_true",required=False, help='drop')
    parser.add_argument("-target_name",type=str,required=False, help='taget_name')  
    args = parser.parse_args()
    main(args)
    
