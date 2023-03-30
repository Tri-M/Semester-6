%{
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
%}

%%
[a-zA-Z]+ {
    int len = strlen(yytext);
    bool has_repeats = false;
    for (int i = 0; i < len; i++) {
        for (int j = i+1; j < len; j++) {
            if (yytext[i] == yytext[j]) {
                has_repeats = true;
                break;
            }
        }
        if (has_repeats) {
            break;
        }
    }
    if (!has_repeats) {
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
