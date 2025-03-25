#include<stdio.h>
void sumarray(int arr[],int size);

int main()
{
int size,arr[50];
printf("enter the no of elements");
scanf("%d",&size);
printf("enter the %d elements",size);
for(int i=0;i<size;i++){
scanf("%d",&arr[i]);
}
sumarray(arr,size);
return 0;
}
void sumarray(int arr[],int size)
{
int sum=0,i;
for(int i=0;i<size;i++){
sum=sum+arr[i];
}
printf("the sum is %d",sum);
}
