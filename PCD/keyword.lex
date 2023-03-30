%{
#include <stdio.h>
%}

%%
auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while { printf("keyword: %s\n", yytext); }
[+\-*/=<>!&|^%]|\+\+|\-\- { printf("operator: %s\n", yytext); }
[(){}\[\];,.?:] { printf("punctuation: %s\n", yytext); }
["'].*["'] { printf("string or character constant: %s\n", yytext); }
[0-9]+ { printf("integer constant: %s\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]* { printf("identifier: %s\n", yytext); }
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
