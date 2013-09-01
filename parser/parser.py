import glob
import csv

import re

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def regularParser( ):

    testName = "exp"
    filter = "10kHTML"
    basedir = "C:\\Users\\chiang-guerrero.luis\\Documents\\results\\" + testName + "\\20x10k\\"
    results = glob.glob(basedir + "*" + filter +"*csv")

    plotTitle = (results[0].split("\\"))[-1]
    allfiles = list()
    i = 1

    for logfile in results:
    
        temp = []

        with open(logfile, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter='\t')
            for row in spamreader:
                temp.append(row)
    
        allfiles.append(temp)

    xAxis = zip(*allfiles[0])[0]    

    columns = (4,7,8,9)
    plotName = {}
    plotName[4] = "(num_call * curr_rate) vs Avg. Response Rate"
    plotName[7] = "(num_call * curr_rate) vs Response Time (ms)"
    plotName[8] = "(num_call * curr_rate) vs IO KB/s"
    plotName[9] = "(num_call * curr_rate) vs %Error"
 
    plotTitle = plotTitle.replace("_1.csv", "")
    plotTitle = plotTitle + "-" + str(len(results)) + "x"

    pp = PdfPages(basedir + plotTitle + ".pdf")

    for column in columns:

        plt.figure(column)
        plt.title(testName + ": " + plotName[column] + "\n" + plotTitle)

        for data in allfiles:
            tdata = zip(*data)
            plt.plot(xAxis[1::], tdata[column][1::])
    
        plt.savefig(pp, format='pdf')

    pp.close()
 
    plt.show()

def extensiveParser( ):

    testName = "test23"
    basedir = "C:\\Users\\chiang-guerrero.luis\\Documents\\results\\" + testName + "\\"
    results = glob.glob(basedir + "*csv")

    for n,filename in enumerate(results):
        results[n] = re.sub("(?<=HTML)(.+)(?=)", "", (filename.split("\\"))[-1])

    results = set(results)

    for logfile in results:
        filterBasedParserAvgExtraFields(testName, basedir, logfile)


def filterBasedParser(testName, basedir, plotTitle):

    results = glob.glob(basedir + plotTitle +"*csv")

    #plotTitle = (results[0].split("\\"))[-1]
    allfiles = list()
    i = 1

    for logfile in results:
    
        temp = []

        with open(logfile, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter='\t')
            for row in spamreader:
                temp.append(row)
    
        allfiles.append(temp)

    xAxis = zip(*allfiles[0])[0]    

    columns = (4,7,8,9)
    plotName = {}
    plotName[4] = "(num_call * curr_rate) vs Avg. Response Rate/s"
    plotName[7] = "(num_call * curr_rate) vs Response Time (ms)"
    plotName[8] = "(num_call * curr_rate) vs IO mbps"
    plotName[9] = "(num_call * curr_rate) vs %Error"
 
    #plotTitle = plotTitle.replace("_1.csv", "")

    plotTitle = plotTitle + "-" + str(len(results)) + "x"

    pp = PdfPages(basedir + plotTitle + ".pdf")

    for column in columns:
        plt.clf()
        plt.figure(column)
        plt.title(testName + ": " + plotName[column] + "\n" + plotTitle)

        for data in allfiles:
            tdata = zip(*data)
            xAxis = tdata[0] 
            if(column == 8):  
                values = tdata[column][1::]
                values = [float(i) * 0.008 for i in values]
                plt.plot(xAxis[1::], values)
            else:
                plt.plot(xAxis[1::], tdata[column][1::])

        plt.savefig(pp, format='pdf')

    pp.close()
    plt.close()
    #plt.show()

def filterBasedParserAvg(testName, basedir, plotTitle):

    results = glob.glob(basedir + plotTitle +"*csv")

    #plotTitle = (results[0].split("\\"))[-1]
    allfiles = list()
    i = 1

    for logfile in results:
    
        temp = []

        with open(logfile, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter='\t')
            for row in spamreader:
                temp.append(row)
    
        allfiles.append(temp)

    xAxis = zip(*allfiles[0])[0]    

    columns = (4,7,8,9)
    plotName = {}
    plotName[4] = "(num_call * curr_rate) vs Avg. Response Rate/s"
    plotName[7] = "(num_call * curr_rate) vs Response Time (ms)"
    plotName[8] = "(num_call * curr_rate) vs IO mbps"
    plotName[9] = "(num_call * curr_rate) vs %Error"
 
    #plotTitle = plotTitle.replace("_1.csv", "")

    plotTitle = "Avg-" + plotTitle + "-" + str(len(results)) + "x"

    pp = PdfPages(basedir + plotTitle + ".pdf")

    try:
        for column in columns:
            plt.clf()
            plt.figure(column)
            plt.title(testName + ": " + plotName[column] + "\n" + plotTitle)

            L = []
            for data in allfiles:
                tdata = zip(*data)
                xAxis = tdata[0] 
                if(column == 8):  
                    values = tdata[column][1::]
                    values = [float(i) * 0.008 for i in values]
                    #plt.plot(xAxis[1::], values)
                    L.append(values)
                else:
                    #plt.plot(xAxis[1::], tdata[column][1::])
                    L.append( [float(x) for x in tdata[column][1::] ])

            T = zip(*L)
            Lr = []

            for val in T:
                Lr.append( np.mean(val) )
             
            plt.plot(xAxis[1::], Lr)
            plt.savefig(pp, format='pdf')

        pp.close()
        plt.close()
        #plt.show()
    except:
        print "Unexpected error at: ", plotTitle
        pp.close()

def filterBasedParserAvgExtraFields(testName, basedir, plotTitle):

    results = glob.glob(basedir + plotTitle +"*csv")

    #plotTitle = (results[0].split("\\"))[-1]
    allfiles = list()
    i = 1

    for logfile in results:
    
        temp = []

        with open(logfile, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter='\t')
            for row in spamreader:
                temp.append(row)
    
        allfiles.append(temp)

    xAxis = zip(*allfiles[0])[0]    

    columns = (4,8,11,12,13)
    plotName = {}
    plotName[4] = "Total Response Rate/s"
    plotName[8] = "(num_call * curr_rate) vs Avg. Response Rate/s"
    plotName[11] = "(num_call * curr_rate) vs Response Time (ms)"
    plotName[12] = "(num_call * curr_rate) vs IO mbps"
    plotName[13] = "(num_call * curr_rate) vs %Error"
 
    #plotTitle = plotTitle.replace("_1.csv", "")

    plotTitle = "Avg-" + plotTitle + "-" + str(len(results)) + "x"

    pp = PdfPages(basedir + plotTitle + ".pdf")

    try:
        for column in columns:
            plt.clf()
            plt.figure(column)
            plt.title(testName + ": " + plotName[column] + "\n" + plotTitle)

            L = []
            for data in allfiles:
                tdata = zip(*data)
                xAxis = tdata[0] 
                if(column == 12):  
                    values = tdata[column][1::]
                    values = [float(i) * 0.008 for i in values]
                    #plt.plot(xAxis[1::], values)
                    L.append(values)
                else:
                    #plt.plot(xAxis[1::], tdata[column][1::])
                    L.append( [float(x) for x in tdata[column][1::] ])

            T = zip(*L)
            Lr = []

            for val in T:
                Lr.append( np.mean(val) )
             
            plt.plot(xAxis[1::], Lr)
            plt.savefig(pp, format='pdf')

        pp.close()
        plt.close()
        #plt.show()
    except:
        print "Unexpected error at: ", plotTitle
        pp.close()

if __name__ == "__main__":
    extensiveParser()