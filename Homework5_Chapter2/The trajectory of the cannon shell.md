#The 5th homework of computational physics
##Problem:  
EXERCISES 2.7 (Page 31)   
##Abstract  
In last homework, I have already learned the knowledge of the basics of Euler method and used it to solve a simple problem. Now in this Chapter, more complex Ordinary Differential Equations are coming. Again one will discover the power of the method. I will try to use it to calculate the trajectory of the cannon shell. I will try to do exercise 2.7, 2.9 and 2.10 in this homework.  
##Background:  
To solve the ordinary differential equations, Euler method will be used.  

###EXERCISES 2.7  
Using the Newton's second law, we have the following equations:  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2x%7D%7Bdt%5E2%7D%3D%5Cfrac%7BF_x%7D%7Bm%7D%3D%5Cfrac%7BF_%7Bdrag%2Cx%7D%7D%7Bm%7D)  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2y%7D%7Bdt%5E2%7D%3D%5Cfrac%7BF_y%7D%7Bm%7D%3D%5Cfrac%7BF_%7Bdrag%2Cy%7D%7D%7Bm%7D-g%5Capprox%5Cfrac%7BF_%7Bdrag%2Cy%7D%7D%7Bm%7D-9.8m/s%5E2)  
- Considering the motion of a cannon shell without air drag:  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2x%7D%7Bdt%5E2%7D%3D%5Cfrac%7BF_x%7D%7Bm%7D%3D%5Cfrac%7BF_%7Bdrag%2Cx%7D%7D%7Bm%7D%3D0)  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2y%7D%7Bdt%5E2%7D%3D%5Cfrac%7BF_y%7D%7Bm%7D%3D%5Cfrac%7BF_%7Bdrag%2Cy%7D%7D%7Bm%7D-g%3D-g)  
- Then consider the air drag:  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2x%7D%7Bdt%5E2%7D%3D%5Cfrac%7BF_x%7D%7Bm%7D%3D%5Cfrac%7BF_%7Bdrag%2Cx%7D%7D%7Bm%7D%3D-mBvv_x)  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2y%7D%7Bdt%5E2%7D%3D%5Cfrac%7BF_y%7D%7Bm%7D%3D%5Cfrac%7BF_%7Bdrag%2Cy%7D%7D%7Bm%7D-g%3D-mBvv_y-g)  
- Consider the air drag with density correction using Maxwell-Boltzmann statistics:  
![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%5E*%3De%5E%7B%5Cfrac%7B-y%7D%7By_0%7D%7DF_%7Bdrag%7D)  
- Consider the air drag with density correction using adiabatic model:  
![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%5E*%3D%5Cleft%281-%5Cfrac%7Bay%7D%7BT_0%7D%20%5Cright%20%29%5E%7B%5Calpha%7DF_%7Bdrag%7D)  
Then we can begin our progrem next!  


##Realization  

###EXERCISE 2.7  
- Since the equations I solve now is two order ordinary differential equations, I shell use the Euler method as follows:  
![](http://latex.codecogs.com/gif.latex?%5C%5C%20x_%7Bi&plus;1%7D%3Dx_i&plus;v_%7Bx%2Ci%7D%5CDelta%20t%20%5C%5C%20y_%7Bi&plus;1%7D%3Dy_i&plus;v_%7By%2Ci%7D%5CDelta%20t%20%5C%5C%20v_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D-%5Cfrac%7BBvv_x%7D%7Bm%7D%5CDelta%20t%20%5C%5C%20v_%7By%2Ci&plus;1%7D%3Dv_%7By%2Ci%7D-%5Cfrac%7BBvv_y%7D%7Bm%7D%5CDelta%20t-g%5CDelta%20t)  
- Estimate the landing point of the shell and use it to substitute the last point that would have been below ground:  
![](http://latex.codecogs.com/gif.latex?%5C%5C%20r%3D-%5Cfrac%7By_n%7D%7By_%7Bn&plus;1%7D%7D%20%5C%5C%20x_l%3D%5Cfrac%7Bx_n&plus;rx_%7Bn&plus;1%7D%7D%7Br&plus;1%7D%20%5C%5C)  
And the coordinate of the point I estimate is <img src="http://latex.codecogs.com/gif.latex?(x_l,0)" alt="" title="" />  
- Consider the air drag with density correction:    
![](http://latex.codecogs.com/gif.latex?%5C%5C%20x_%7Bi&plus;1%7D%3Dx_i&plus;v_%7Bx%2Ci%7D%5CDelta%20t%20%5C%5C%20y_%7Bi&plus;1%7D%3Dy_i&plus;v_%7By%2Ci%7D%5CDelta%20t%20%5C%5C%20v_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D-%5Cfrac%7BB%5E*vv_x%7D%7Bm%7D%5CDelta%20t%20%5C%5C%20v_%7By%2Ci&plus;1%7D%3Dv_%7By%2Ci%7D-%5Cfrac%7BB%5E*vv_y%7D%7Bm%7D%5CDelta%20t-g%5CDelta%20t)  

1. I creat a class called flying_cannon in python to do the code and realize the functions I mentioned before. I set time step(delta t) as 0.01s and B/m as 4 * 10^-5/m first to draw the trajectory.  
2. Contrast it with the condition without wind drag and draw the trajectory in one picture. 
3. Use the adiabatic model of air density and Maxwell-Boltzmann statistics perspectively to calculate the trajectory.  
4. Consider the variation of the ground temperature and do the calculation again.   

##Plotting

1. The trajectory of the cannon shell with wind drag:  
Initial angle of velocity -> 0.785   
Initial location of cannon shell -> (0, 0)  
time step ->  0.01  
B over m =0.00004 /m  
![](https://github.com/AriaOnTheString/compuational_physics_N2014302290002/blob/master/Homework5_Chapter2/Problem%202.7(1).png)  

2. The trajectory of the cannon shell without wind drag:  
Initial angle of velocity -> 0.785  
Initial location of cannon shell -> (0, 0)  
time step ->  0.01  
B over m =0 /m  
![](https://github.com/AriaOnTheString/compuational_physics_N2014302290002/blob/master/Homework5_Chapter2/Problem%202.7(2).png)  

3. The contruction of the trajectorys with and without wind drag:  
Initial angle of velocity -> 0.785  
Initial location of cannon shell -> (0, 0)  
time step ->  0.01  
B over m =0.00004 /m  
![](https://github.com/AriaOnTheString/compuational_physics_N2014302290002/blob/master/Homework5_Chapter2/Problem%202.7(4).png)  
