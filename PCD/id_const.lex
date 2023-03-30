%{
#include <stdio.h>
%}

%%
[a-zA-Z_][a-zA-Z0-9_]* { printf("identifier: %s\n", yytext); }
[0-9]+(\.[0-9]+)?([eE][+-]?[0-9]+)? { printf("numerical constant: %s\n", yytext); }
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
