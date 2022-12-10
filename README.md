# gt-modsim-s22-team11
CSE6730/CX4230 ModSim Spring 2022 Group Project (Team 11)

## Team Members
1. Tusheet Sidharth Goli
2. Tushna Eduljee
3. Matthew Dacey-Koo
4. Aarun Srinivas

## Grading Collaborators
1. Rich Vuduc (Professor)
2. Takahiro Furuya (TA)

## Getting Started
### Prerequisites
1. Python 3.5
2. numpy
3. pygame
4. scipy

## Instruction To Run The Simulator
### How To Run The Simulator
1. Environment setup (pip install basic requirements - in requirements.txt)
2. python example.py (to understand our simulation and model on a simple system)
3. python gatech.py (to renders our actual project: a map of Georgia Tech and visualize the traffic flow on this road network)

## Project Description
### Project Abstract
In this project, we model traffic flow at Georgia Tech using campus road networks as they currently stand. This simulation will allow users to adjust various parameters such as traffic flow while putting in place terrain-changing obstacles such as road blockades and intersection shutdowns which alter traffic flow. Previous attempts at charting automobile routes around campus include PassioGO and GT Buses (which both map GT bus routes in real-time). While these help students navigate campus, a key challenge is smoothly navigating all road traffic around campus even under perturbations that change traffic patterns. As such, traffic patterns under perturbation can be observed and used to identify pain points in the campus road networks for city planning in the future. It can help provide statistical analysis to assist with the city road planning by giving insightful information about intersection congestions, placement of traffic lights, stop signs, etc. This insight can be particularly useful in developing re-routing strategies in situations of blockade or road closures for example, on game days, special events, etc. We aim to achieve this using a replica of the GT road map system and use the conceptual model of a  microscopic traffic automaton model (IDM - Intelligent Driver Model) proposed by Treiber et. al. which is a multi-agent system of vehicles that act independently in response to a stimulus from the environment.

### System Description
The system that we modeled includes most of the Georgia Tech campus’ main roads where automobiles such as cars and trucks can drive. This ranges from the intersection between North Avenue and Techwood Drive in the South East to the intersection of Curran Street and 14th Street in the North West. It is important to know that all Georgia Tech bus routes are also contained within this perimeter. These are the roads upon which we visualize all traffic through campus. As our simulation is meant for use in redirecting traffic given perturbations in regular flow (such as intersection blockages or road closures), the system features all of the same road rules as those present in the real world to keep it as realistic as possible. This includes all the same traffic patterns due to features such as one-way streets or limited turning lanes. Our system also includes accurate traffic lights, and important road signs (ie. stoplights, and stop signs) that we obtained through analysis from Google Maps and Waze APIs for all streets within the perimeter.

### Conceptual Model
We firstly constructed a conceptual model of Georgia Tech’s road system by utilizing a series of lane and traffic light objects. The lane object was implemented as a Python class and contains a queue that will be used to keep track of all the cars currently driving on the lane. The traffic light object is also implemented as a Python class and is used to connect lanes coming from different directions together and direct traffic through their intersection. In addition to keeping track of the cars present in the lane, the lane object also contains a variable that can be set to close it off as well as a variable that can be set to determine the direction of traffic in the lane. The capacity of the lane is calculated using the lane’s distance which will be determined upon instantiation and each car’s length that is present on the lane. In a sense, this model of Georgia Tech’s road system which uses lane and traffic light objects functions as a microscopic traffic model, i.e., a multi-agent system with independently acting vehicles where every i-th vehicle follows the (i-1)-th vehicle. This is because the movement of a car is directly dependent on its neighbors. In particular, if one car is located in front of another car, the back car’s speed is dependent on how fast the front car is moving.

For modeling the cars, we utilized the Intelligent Driver Model (IDM) which is a mathematical model for multi-agent vehicle movements developed by Treiber, Hennecke, and Helbing. Before exploring the mathematical models for the vehicle movement, we will define some variables. The speed/velocity equations are the same as the equations from mechanics physics, i.e., the equations of motion. Based on these equations of motion, we can identify the distance between two vehicles as well as the differential velocity between two back-to-back vehicles. The acceleration of the vehicles is also governed by the IDM model proposed by Treiber et. al. This model assumes free roads and free interactions where the dynamics of the vehicle movements are given by the following equations. These equations govern the overall acceleration of the cars as a combined effect of the free movement on the roads as well as interactions between other cars on the road.

That summarizes and dictates the fluent motion of the vehicles on the road and this is the mathematical model we utilized to simulate vehicle movements on the proposed Georgia Tech map system. This map system was made using python pygame where we replicated the Georgia Tech road system to simulate these cars on in.

### Platforms of Development
As our project is specifically focused on Georgia Tech and its road planning system, we want to create a tool that both accurately represents the system and is easy to use for clients without background knowledge of the project. For this, we used python for front-end data visualization as well as for back-end data processing. We found python easy to code the backend, but also utilize the ease and power of pygame to be able to render an interactive and good-looking front end.

Front End: The front end is a pygame built in python. Pygame is a python module designed for writing video games and interactive UI screens. It utilizes the power of being a primary backend language that has the ability to render interactive visual displays and simulations. We created our simulation engine and GT road map system in the form of a pygame that can render cars moving on these roads.

Back End: The backend was also coded in python to work hand in hand with the pygame UI design. We have our mathematical models for our vehicle movements and roads encoded using python and the UI utilizes these models to render a clean simulation of our system.

These platform choices were made because we have experience working with python and pygame from previous classes and past projects. This also enabled a simple and clean coding experience with little to no effort for frontend and backend integrations since it was all in python. Using these platforms of development, we were successfully able to implement our simulation.
