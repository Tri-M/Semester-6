%{
#include <stdio.h>
%}

%%
[a-z]+ {
    int i, len = strlen(yytext);
    for (i = 0; i < len - 1; i++) {
        if (yytext[i] > yytext[i+1]) {
            /* not in ascending order */
            return;
        }
    }
    /* in ascending order */
    printf("accepted: %s\n", yytext);
}
[ \t\n]+ ; /* ignore whitespace */
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

    return 0;
}


#run as
#lex program.lex
#gcc -o program lex.yy.c
#./program input.txt

