#include<stdio.h>
#include<string.h>
int main()
{
char str1[30],str2[30];
printf("enter the string");
scanf("%s",str1);
printf("enter the string");
scanf("%s",str2);
if(strcmp(str1,str2)==0)
{
printf("The are equal");
}
else
{
printf("the string is not equal");
}
return 0;
}
