%{
#include <stdio.h>
#include <string.h>
%}

%%
[a-zA-Z]+ {
    char word[50];
    strcpy(word, yytext);
    int length = strlen(word);
    char first = word[0];
    if (strchr("aeiouAEIOU", first) != NULL) {
        printf("%s%s", word, "ay");
    } else {
        for (int i = 1; i < length; i++) {
            printf("%c", word[i]);
        }
        printf("%cay", first);
    }
    printf(" ");
}

%%
int main() {
    yylex();
    return 0;
}
