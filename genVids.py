import os
import utils

if __name__ == '__main__': 
    f = open("topics.txt", "r");
    topics = f.read().split('\n');
    f.close();
    
    #progress barS
    utils.printProgressBar(0, len(topics), prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i in range(len(topics)):
        os.system(f"python main.py -p \"{topics[i]}\"")
        utils.printProgressBar(i+1, len(topics), prefix = 'Progress:', suffix = 'Complete', length = 50)
    print("Done")


