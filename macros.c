#include<stdio.h>
#define PI 3.14
#define Area_of_cricle(r)(PI*r*r)
#define Surface_area_of_sphere(r,h)(2*PI*r*(r+h))
int main(){
float r,h,area,surface_area;
printf("enter the radius of circle and cylinder");
scanf("%f",&r);
printf("enter the height of the cylinder");
scanf("%f",&h);
area=Area_of_cricle(r);
surface_area=Surface_area_of_sphere(r,h);
printf("area of cicle is %f\n",area);
printf("surface area of the cylinder %f",surface_area);
return 0;
}
