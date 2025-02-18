#include<stdio.h>
int main()
{
int row1,colm1,i,j,row2,colm2,a[10][10],b[10][10],c[10][10];
printf("Enter the no rows and columns of first matrix");
scanf("%d%d",&row1,&colm1);
printf("Enter the no rows and columns of second matrix");
scanf("%d%d",&row2,&colm2);
if(row1!=row2 && colm1!=colm2)
 {
 printf("matrix cannot be added\n");
 return 0;
 }
else{

printf("enter the elements in first matrix");
	for(i=0;i<row1;i++)
	{
	for(j=0;j<colm1;j++)
	{
	scanf("%d",&a[i][j]);
	}
	}
printf("enter the elements in second matrix");
	for(i=0;i<row2;i++)
	{
	for(j=0;j<colm2;j++)
	{
	scanf("%d",&b[i][j]);
	}
	}

	for(i=0;i<row1;i++)
	{
	for(j=0;j<colm1;j++)
	{
	c[i][j]=a[i][j]+b[i][j];
	}
	}
}	
printf("sum of two matrix is\n");
for(i=0;i<row1;i++)
{
for(j=0;j<colm1;j++)
{
printf("  %d  ",c[i][j]);
}
printf("\n");
}


return 0;
}
