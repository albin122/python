#include<stdio.h>
int main()
{
int a[10],i,n,max,min,p1=0,p2=0;
printf("enter the size of array");
scanf("%d",&n);
printf("enter the elements");
	for(i=0;i<n;i++)
	{
	scanf("%d",&a[i]);
	}
	for(i=0;i<n;i++)
	{
	printf("\n elements are:%d\n",a[i]);
	}
	max=a[0];
	min=a[0];
	for(i=1;i<n;i++)
	{
		if(a[i]>max)
		{
		max=a[i];
		p1=i;
		}
		if(a[i]<min)
		{
		min=a[i];
		p2=i;
		}
	}
printf("max is %d at position %d",max,p1);
printf("min is %d at position %d",min,p2);
return 0;
}
