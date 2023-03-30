%{
#include <stdio.h>
int char_count = 0;
int line_count = 0;
%}

%%
. { char_count++; }
\n { line_count++; }
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

    printf("Number of characters: %d\n", char_count);
    printf("Number of lines: %d\n", line_count);

    fclose(yyin);

    return 0;
}


#run as 
#lex program.lex
#gcc -o program lex.yy.c
#./program input.txt
