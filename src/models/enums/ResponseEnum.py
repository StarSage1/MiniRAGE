from enum import Enum
class ResponseSignal(Enum):
    File_Validated_Success="File_Validated_Successfully"
    File_Type_Not_Supported="File_Type_Not_Supported"
    File_Size_Exceeded="File_Size_exceeded"
    File_Uploaded_Success="Succeded"
    File_Uploaded_Fail="File_upload_failed"