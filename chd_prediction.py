import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class PatientData:
    def __init__(self, input_data)
        self.input_data = input_data
        self.data = pd.read_csv('framingham.csv')
        
        
def read_data():
    data=pd.read_csv('framingham.csv')
    print(data)

def main():
    read_data()

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
    parser = argparse.ArgumentParser(description='TODO CHD dewsc')
    parser.add_argument('show_data')
    
