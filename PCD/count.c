#include<stdio.h>
#include<conio.h>
int main()
{
char str[100];
int i,alphabets=0,digits=0,other=0;
printf("Enter the string:");
gets(str);
for(i=0;str[i]!='\0';i++)
{
if((str[i]>='a'&&str[i]<='z')||(str[i]>='A'&&str[i]<='Z'))
alphabets++;
else if(str[i]>='0'&&str[i]<='9')
digits++;
else
other++;
}
printf("Alphabets=%d",alphabets);
printf("Digits=%d",digits);
printf("Other=%d",other);
getch();
}
