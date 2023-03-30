%{
#include <stdio.h>
int vowel_count = 0;
%}

%%
[aeiou] { vowel_count++; } 
.*a.*e.*i.*o.*u.*
    printf("accepted: %s\n", yytext);
}
[ \t\n]+ ; 
. ; /* ignore other characters */
%%

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s filename\n", argv[0]);
        return 1;
    }

    yyin = fopen(argv[1], "r");
    if (yyin == NULL) {
        printf("Error opening file %s\n", argv[1]);
        return 1;
    }

    yylex();

    fclose(yyin);

    printf("Total vowels: %d\n", vowel_count);

    return 0;
}
