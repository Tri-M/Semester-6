%{
#include <stdio.h>
#include <stdbool.h>
%}

%%
[0-9]+ {
    int i, len = strlen(yytext);
    bool repeated = false;
    for (i = 0; i < len - 1; i++) {
        if (yytext[i] == yytext[i+1]) {
            if (repeated) {
                /* more than one repeated digit */
                return;
            }
            repeated = true;
        }
    }
    /* at most one repeated digit */
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
