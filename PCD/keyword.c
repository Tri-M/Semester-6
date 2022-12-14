#include<stdio.h>
#include<string.h>
int main()
{
    char keywords[32][15]={
      "auto","double","int","struct","break","else","long",
      "switch","case","enum","register","typedef","char",
      "extern","return","union","const","float","short",
      "unsigned","continue","for","signed","void","default",
      "goto","sizeof","volatile","do","if","static","while"
   } ;
   char str[50];
   printf("Enter your text :");
   gets(str);
   int flag=0;
   for(int i=0;i<32;i++)
   {
    if(strcmp(keywords[i],str)==0)
    {
        flag=1;
    }
   }
   if(flag==1)
   
    printf("\nIt is a keyword");
   
   else
    printf("\nNot a keyword.");
   

}