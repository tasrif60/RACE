# RACE
##Self-contained setup guide:
We have two parts of our project. One is model building using data analytics and another is user interaction using python flask and mongodb. However, to run both of our application you need to setup some common environment. So we going to follow step by step assuming we have all the code to run.

**1.	Setup Python:** First step of setting required environment is to install python. 
We would prefer the stable version of the python because we did use the current stable version `3.7.9`. Windows users can easily go 
to the website [Python For Windows](https://www.python.org/downloads/windows) download he installer. For mac and Linux user 
can easily use 
`brew install python` 
command in the terminal to install python. It is very important to setup python version properly. However, creating virtual environment
is also a vital part. 

**2.	Install PyCharm for Web application:** As developers we really like cool 
IDE that makes your life easy. Rather than using other text editor and setup 
all the files by our self, we just gave all the responsibility to PyCharm to s
etup everything for me. It saves time and make the development process faster. 
Not only managing the project, but also it helps you in version controlling. 
There are different version of PyCharm, but we used community edition to serve our purpose.


**3. Install Anaconda for Data Analytics:** Then for data analytics purpose, needed to install anaconda. It s navigator that helps you to create a 
local server and run an virtual environment for Juperter Notebook. However, we used Jupiter Notebook for analyzing our raw data and create a machine learning model
using different algorithms. You can install anaconda for any OS from [Anaconda Site](https://www.anaconda.com/products/individual). 

**4.Install MongoDB and a MongoDB Client:** For the data storage, we used mongodb. It is basically no relational database and we used it to store our csv 
data for our web application. You can download and install windows version from [MongoDB Windows]( https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/). For other os installation go to terminal and just use following command:
`brew install mongodb-community@4.4`
We used this stable version for our project purpose. After completing installation you can start the server typing ` brew services start mongodb-community@4.4 ` on the command line and start working on it in terminal.  
In stead of working in terminal, we used a client named [MongoDB Compass Community Edition]( https://www.mongodb.com/try/download/compass). It made storing our data easy. After installing the compass you can connect it with mongodb using `localhos:27017` where mongo default port `27017`. 
![mongo1](https://github.com/tasrif60/RACE/blob/master/readme_images/mongo1.png)
After connecting the server, create a database named “road_collusion” and then create a collection named ‘collusion_final’. After that import our data [‘mongo_data.csv’](https://www.dropbox.com/s/36nu3yfjeu108js/mongo_data.csv?dl=0) file to the collection using ‘data import’ option. It is worth mentioning that, during import convert all the data type into Number from top dropdown. The csv file was exported from our local database.   
![mongo1](https://github.com/tasrif60/RACE/blob/master/readme_images/mongo2.png)


**5.	Download or Clone repository:** From this repository you can download all files and create your own local repository for the project. 
Make sure folders python version is **3.7.2** otherwise some packages would not work. To make sure python environment you can use `brew install pyenv` to 
install in your pc or you can check [pyenv]( https://github.com/pyenv/pyenv/wiki) site to check more details. However you can use it even if you want to 
run multiple version of python in you machine. For analytics just download the final_model note book from the git repository. In addition to you have download the actual [csv file](https://www.dropbox.com/s/tksbkn4wvek92by/NCDB_1999_to_2017.csv?dl=0) form this link to run the process and get better result. You should have a powerful machine with large memory(minimum 16 GB) to run the whole notebook properly. However, you have to download the `.sav` file from this [link]() to run the prediction from our web application. This file is a bit large as well (about 1.8 GB), so it might take time to download depending on your internet speed. Place this file in your local repository and change the path from the code.
![mongo3](https://github.com/tasrif60/RACE/blob/master/readme_images/pycharm3.png)

**6.	Open the repo and run:** Open the repo with our IDE PyCharm and  give it some time load the full project. 
Then select the virtual environment and runt the using play button on the top right corner. 
![mongo1](https://github.com/tasrif60/RACE/blob/master/readme_images/pycharm1.png)


