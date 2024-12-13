FROM python 
# using python image from docker hub 
WORKDIR /ashucode 
# creating and changing folder in docker image
COPY automate01.py /ashucode/
CMD [ "python" , "automate01.py" ]
# run the python code while creating container