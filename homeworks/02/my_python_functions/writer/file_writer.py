import os
import pickle as pkl

class FileWriter:
    
    def __init__(self, path):
        """path - путь до файла"""
        if self._check_path(path):
            self.path_ = path
            self.file = None
        
    def _check_path(self, path):
        return os.path.exists('/'.join(path.split('/')[:-1]))
    
    def print_file(self):
        self.file = open(self.path_);
        for line in self.file:
            print(line)
        self.file.close()
#        self.file = None

    def write(self, some_string):
        if os.path.exists(self.path_):
            self.file = open(self.path_,'a')
        else:
            self.file = open(self.path_,'w')
        self.file.write(some_string)
        self.file.close();
#        self.file = None

  
    def save_yourself(self, file_name):
        if self._check_path(file_name):
            saved = open(file_name, 'wb')
            pkl.dump(self, saved)
#            saved.close()

    @property
    def path(self):
        return self.path_
    @path.getter
    def path(self):
        return self.path_
    @path.setter
    def path(self, path):
        if self._check_path(path)
            self.path_ = path
    @path.deleter
    def path(self):
        self.path_ = None
        
        
    def __enter__(self):
        self.file = open(self.path_, 'a')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb): 
            self.file.close()
            self.file = None
    @classmethod
    def load_file_writer(cls, pickle_file):
        
        if os.path.exists(pickle_file):
            file = open(pickle_file, 'rb')
            obj = pkl.load(file)
            return obj
