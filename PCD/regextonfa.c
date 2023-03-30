#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STATES 100


struct state {
  int transitions[256]; // Transitions for all possible characters
  int accepting; // Is this an accepting state?
};


struct nfa {
  int start; // Starting state
  int num_states; // Number of states
  struct state states[MAX_STATES]; // Array of states
};

// Function to construct the NFA from the regular expression
struct nfa construct_nfa(char *regex) {
  struct nfa nfa;
  nfa.start = 0;
  nfa.num_states = 1;

  for (int i = 0; i < strlen(regex); i++) {
    char c = regex[i];
    if (c == 'a') {
      nfa.states[nfa.num_states].transitions[0] = nfa.num_states + 1;
      nfa.states[nfa.num_states].accepting = 0;
      nfa.num_states++;
      nfa.states[nfa.num_states].transitions[0] = -1;
      nfa.states[nfa.num_states].accepting = 1;
      nfa.num_states++;
    }
  }

  return nfa;
}

int main() {
  char regex[100];
  printf("Enter a regular expression: ");
  scanf("%s", regex);

  struct nfa nfa = construct_nfa(regex);
  printf("NFA constructed successfully!\n");
  printf("Number of states: %d\n", nfa.num_states);
  printf("Starting state: %d\n", nfa.start);

  return 0;
}
