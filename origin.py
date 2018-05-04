import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def loadDataset(infile):
    df = pd.read_csv(infile, sep='\t', header=0, dtype=str, na_filter=False)
    return np.array(df).astype(np.float)

if __name__=="__main__":
    data = loadDataset(r"data/testSet.txt")
    for i in range(data.shape[0]):
        plt.text(data[i][0],data[i][1],"*",color='b')
    plt.axis([-7,7,-7,7])
    plt.savefig("./result/origin.png")
    plt.show()

