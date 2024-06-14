# Report on real estate price prediction
## Source data and statistics 
***Project goal***: to develop a price prediction model that can estimate the value of a flats (rent) using historical data, including past flats prices and their specifications.

**We have a  dataset containing various columns of information related to real estate properties. These columns include:**

1. Last Price: The most recent price at which the property was listed or sold.
2. Floor: The floor number on which the property is located.
3. Open plan: Whether the property has an open plan or not. 
4. Rooms: The number of rooms available in the property.
5. Studio: Whether the property is a studio or not. 
6. Area: The total area or size of the property.
7. Kitchen Area: The area specifically designated for the kitchen within the property.
8. Living Area: The area intended for living spaces such as the living room, bedrooms, etc.
9. Agent Fee: The fee charged by the agent or agency involved in the property transaction.
10. Renovation: Indicates whether the property has undergone any recent renovations or improvements.
11. Offer type: Indicates whether the property is for sale or rent.
12. Building ID: An identifier associated with the specific building or property.

The data is from [Yandex.Realty](https://realty.yandex.ru) containing real estate listings for apartments in St. Petersburg and Leningrad Oblast from 2016 till the middle of August 2018. The dataset has a mix of data types, including integers, floating-point numbers, booleans, and strings.

**[lab1_1_EDA_real_estate_data_done.ipynb](/lab1_1_EDA_real_estate_data_done.ipynb) contains the preprocesing and EDA of our dataset.**
There were calculated median and mean prices, and the data was cleaned from outliers.
![mean and meadian comparison](/image.png)

### Data Visualization
**[lab1_2_visualization_done.ipynb](/lab1_2_visualization_done.ipynb) contains analysis of our dataset with visualization techniques.**

For building model in the next steps highly correlated features should be deleted to avoid multicollinearity.
![cor matrix](/Screenshot_32.jpg) 

## Model Information
**[lab2_building_model_done.ipynb](/lab2_building_model_done.ipynb) contains the proccess of building models**


***Features of our data set***: open_plan, rooms, area, renovation  
***Target of our data set***: last_price

After preprocessing  the data was divided to train and test.
![train test](/Screenshot_34.jpg) 

The models were developed using the scikit-learn library. Following models were developed: DecisionTreeRegressor, Random Forest, CatBoostRegressor and GradientBoostingRegressor. 

The best results were demonstrated by the DecisionTreeRegressor model. 
* **Model Type:** DecisionTreeRegressor
* **Hyperparameters:** Hyperparameters were tuned using Grid Search with Cross-Validation (GridSearchCV). The parameter grid included:

  - splitter: ['best', 'random']
  - random_state: [42]
  - max_depth: range(1, 40)
    
  ***Best hyperparams***: {'max_depth': 4, 'random_state': 42, 'splitter': 'best'}

The performance of the models was evaluated using three metrics:

![metrics dtr](/Screenshot_35.jpg)  

## SSH connection

I connected to my virtual machine using following username and IP:

```	
ssh otradnova8@51.250.17.124
```	

## Instructions on Virtual environment
How to create and activate virtual environment:
```
python3 -m venv env
source env/bin/activate 
```
All installed packages for the project you can find in the file requirements.txt. You can also download all the necessary libraries and packages for the project using the following command:
```
pip install -r requirements.txt
```
Run the app using 
```
python app.py
```
## Dockerfile

### Dockerfile Content
```
FROM ubuntu:20.04
MAINTAINER Evgeniia Otradnova
RUN apt-get update -y
COPY . /opt/gsom_predictor
WORKDIR /opt/gsom_predictor
RUN apt install -y python3-pip
RUN pip3 install -r requirements.txt
CMD python3 app.py
```

This Dockerfile creates a Docker image that:

* Uses Ubuntu 20.04 as the base image.
* Updates the package list.
* Copies the current directory's contents into /opt/gsom_predictor inside the image.
* Sets /opt/gsom_predictor as the working directory.
* Installs python3-pip for managing Python packages.
* Installs the necessary Python packages listed in requirements.txt.
* Runs the Python application app.py when the container starts.

**Information about remote machine:**
```	
app.run(debug = True, port = 7778, host = '0.0.0.0')
```	
In order to run virtual machine port we should use this code after:
```	
sudo apt install ufw
sudo ufw allow 7778 
```	

## How to run the App using Docker 
```
docker run --network host -it yevheniiaotr/gsom_predictor:v.0.1 /bin/bash
docker run --network host -d yevheniiaotr/gsom_predictor:v.0.1 
docker ps 
```
## Checking the results with PostMan
We have to use the GET method: 

![metrics dtr](/Screenshot_36.jpg) 

![metrics dtr](/Screenshot_37.jpg) 