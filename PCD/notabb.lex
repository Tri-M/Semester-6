%{
#include <stdio.h>
#include <stdbool.h>
%}

%%
a*b* {
    int i, len = strlen(yytext);
    bool has_abb = false;
    for (i = 0; i < len - 2; i++) {
        if (yytext[i] == 'a' && yytext[i+1] == 'b' && yytext[i+2] == 'b') {
            has_abb = true;
            break;
        }
    }
    if (!has_abb) {
        printf("accepted: %s\n", yytext);
    }
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
