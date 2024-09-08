import os
import json
import re

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
        self.filenames = os.listdir(dirname)
        self.filecount = 0  # Used for count the loaded files
        self.ifile = open(os.path.join(self.dirname, self.filenames[self.filecount]), 'r')
 
    def __iter__(self):
        for filename in self.filenames:
            print("Reading text from file:" + filename)
            ifile = open(os.path.join(self.dirname, filename), 'r')        
            for i, line in enumerate(ifile):
                try:
                    data = json.loads(line)
                except:
                    print("Read current file done.")
                    break
                text = data["text"]
                yield re.sub('[^A-Za-z]+', ' ', text).strip().lower().split()
 
    def get_a_sentence(self):
        try:
            line = self.ifile.readline()
            data = json.loads(line)
            text = data["text"]
            #print(text.split())
            return text.split()
        except:
            self.filecount += 1
            if self.filecount >= len(self.filenames):
                return 0
            else:
                self.ifile = open(os.path.join(self.dirname, self.filenames[self.filecount]), 'r')
                return self.get_a_sentence()