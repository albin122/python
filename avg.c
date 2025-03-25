#include<stdio.h>
int main()
{
int n,sum=0,i,arr[10];
float avg;
printf("enter the size of array");
scanf("%d",&n);
printf("enter the elements");
for(i=0;i<n;i++)
{
scanf("%d",&arr[i]);
sum+=arr[i];
}
avg=sum/n;
printf("the aveage of number is :%f",avg);
return 0;
}
