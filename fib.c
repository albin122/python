#include<stdio.h>
int fibonacci(int n){
if(n==0)
return 0;
else if(n==1)
return 1;
else
return fibonacci(n-1)+fibonacci(n-2);
}
int main()
{
int n,i;
printf("enter the no  terms");
scanf("%d",&n);
printf("the fibonacci series is ");
for(i=0;i<n;i++)
printf("%d\t",fibonacci(i));
return 0;
}
