#include<stdio.h>
int factorial(int);
int main()
{
int num;
printf("enter the number");
scanf("%d",&num);
if(num<0)
{
printf("factorial is not defeined for negative number");
}
else{

printf(" factorial of %d is %d",num,factorial (num));
}
return 0;
}
int factorial(int a)
{
int factorial=1,i;
for(i=1;i<=a;i++){
factorial*=i;
}
return factorial;
}

