import os,shutil
file_type={
    'audio_file':('.mp3','.m4a','.wav','.flac'),
    'video_file':('.mp4','.3gp','.mkv','.flv'),
    'docs_file':('.pdf','.txt','.docx'),
}
def get_file(fileType):
    # for filename in os.listdir():
    #     for item in fileType:
    #          if filename.endswith(item):
    #             print(filename)
#    print([filename for filename in os.listdir() for item in fileType if filename.endswith(item)])
    return [filename for filename in os.listdir() for item in fileType if filename.endswith(item)]


for extention_type,extention_tuple in file_type.items():
    print(f'extention type {extention_type}')
    print(f'extention tuple {extention_tuple}')
    folder_name=extention_type.split('_')[0]+'files'
    print(folder_name)
    folder_path=os.path.join(os.getcwd(),folder_name)
    print(folder_path)
    os.mkdir(folder_path)
   # for tupleFile in file_type.items():
    #     print(get_file(tupleFile))
    for item1 in get_file(extention_tuple):
        print(item1)
        item_path=os.path.join(os.getcwd(),item1)
        item_new_path=os.path.join(folder_path,item1)

        shutil.move(item_path,item_new_path)