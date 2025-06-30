import src.file_explorer as file_explorer
import src.data_classes as data_classes
import copy

class PublisherFileData:

    def __init__(self, sub_info_lock, pub_info_lock):
        self.pub_info_lock = pub_info_lock
        self.sub_info_lock = sub_info_lock
        self.path = "/"#home/laser/Documents/TaskManager/src/"

    def gather_file_data(self):
        
        with self.sub_info_lock:
            self.path = copy.deepcopy(data_classes.get_file_path())

        file_info = file_explorer.get_dir_info(self.path)
        #print(file_info)
        with self.pub_info_lock:
            data_classes.set_file_data(copy.deepcopy(file_info))

if __name__ == "__main__":
    a = PublisherFileData(1, 2)
    a.gather_file_data()
