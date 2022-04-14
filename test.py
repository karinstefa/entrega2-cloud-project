import os
from sqlalchemy import create_engine
db_string = "postgresql://postgres:cloud1234@database-2.cnjddgnl0ynw.us-east-1.rds.amazonaws.com:5432/db_concursos"
db = create_engine(db_string)
result_set = db.execute("SELECT * FROM Voces")
print(result_set)


cmd = f" ffmpeg -i  https://static-cloud-project.s3.amazonaws.com/files/voz/file_example_OOG_1MG.ogg  -af aresample=async=1:first_pts=0   file_example_OOG_1MG.mp3"
#'aws s3 cp s3://static-cloud-project/files/voz/Cris237098.ogg - | ffmpeg -i - -f matroska - | aws s3 cp - s3://static-cloud-project/files/voz/Cris237098.mp3'

#f" ffmpeg -i  https://static-cloud-project.s3.amazonaws.com/files/voz/Rene895714.ogg  -af aresample=async=1:first_pts=0  Rene895714.mp3"

#'aws s3 cp https://static-cloud-project.s3.amazonaws.com/files/voz/Rene895714.ogg - | ffmpeg -i - -f matroska - | aws s3 cp - https://static-cloud-project.s3.amazonaws.com/files/voz/Rene895714.mp3'

os.system(cmd)


#%%
import boto3
from s3streaming import s3_open

#%%


with s3_open('s3://bucket/key', boto_session=boto3.session.Session()) as f:
    for next_line in f:
        print(next_line)