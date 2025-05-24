from fastapi import UploadFile
from helpers.config import GetSettings, Settings
from .BaseController import BaseController
from .ProjectController import ProjectController
from models import ResponseSignal
import random, string ,os
import re
class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.scale_size=1048576

    
    def ValidateFile(self, file: UploadFile):

        if file.content_type not in self.app_settings.File_Uploaded_Types:
            return False , ResponseSignal.File_Type_Not_Supported.value
        
        if file.size > self.app_settings.File_Max_Size * self.scale_size:
            return False , ResponseSignal.File_Size_Exceeded.value
        

        return True,ResponseSignal.File_Validated_Success.value
    
    def generate_unique_filepath(self,orig_file_name: str, project_id: str):
        random_key= self.generate_random_string()
        project_path=ProjectController().get_project_path(project_id=project_id)

        cleaned_file_name= self.get_clean_filename(orig_file_name=orig_file_name)

        new_file_path= os.path.join(project_path,random_key+"_"+cleaned_file_name)

        while os.path.exists(new_file_path):
              random_key= self.generate_random_string()
              new_file_path= os.path.join(project_path,random_key+"_"+cleaned_file_name)

        return new_file_path, random_key

    def get_clean_filename(self,orig_file_name: str):
        #remove any sepcial character except _ and .
        cleaned_file_name = re.sub(r'[^\w\._-]', '', orig_file_name.strip())

        #replace any space with _
        cleaned_file_name = cleaned_file_name.replace(' ', '_')

        return cleaned_file_name
