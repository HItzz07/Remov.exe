import os
base_target_folder = r'H:\Progr\Tries\EXE' + '\\'
source_folder = r'H:\Progr\Tries' + '\\'

#You can edit base_target_folder and source_folder as per your file system
#This works for windows , you can change '\\' and '\' as per linux usage . 

def move_files(source_folder , base_target_folder):
    try:
        for path , dir , files in os.walk(source_folder):
            if files:
                for file in files:
                    s1 = file[-3:]
                    if s1 == "exe":
                        if not os.path.isfile(base_target_folder + file):  # if this file from this folder does not exists in target folder , then move it 
                            os.rename(path + '\\' + file , base_target_folder + file)
        print('All Files moved')
    except Exception as e:
        print(e);    

move_files(source_folder , base_target_folder)

#print(target_folder)
#print(source_folder)


182.65.138.165
14.131.255.255
14.131.255.253
47.29.213.79
14.131.255.252
14.131.255.251
14.131.255.250
14.1.99.255