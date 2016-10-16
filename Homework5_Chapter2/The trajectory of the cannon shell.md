#The 5th homework of computational physics
##Problem:  
EXERCISES 2.7 (Page 31)  
EXERCISES 2.9 (Page 31)  
EXERCISES 2.10 (Page 31)  
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
