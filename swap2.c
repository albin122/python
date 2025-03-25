#include<stdio.h>
#define swap1(a,b) int temp=a;a=b;b=temp;

int main()
{
int a,b;
printf("enter the value of a and b");
scanf("%d%d",&a,&b);
swap1(a,b)
printf("the swaped value is a=%d and b=%d",a,b);
return 0;
}
