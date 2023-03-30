%{
#include <stdio.h>
%}

%%
0[xX][0-9a-fA-F]+ { printf("hexadecimal number: %s\n", yytext); }
[ \t\n]+ ; /* ignore whitespace */
. { printf("unrecognized character: %s\n", yytext); }
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
