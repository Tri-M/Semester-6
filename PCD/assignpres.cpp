#include <iostream>
#include <stack>
#include <string>
#include <unordered_map>
#include <vector>
#include<bits/stdc++>

using namespace std;

const vector<vector<string>> PRODUCTIONS = {
    {"E", "T", "E'"},
    {"E'", "+", "T", "E'", {":=", "temp"}},
    {"E'", "-", "T", "E'", {":=", "temp"}},
    {"E'", "epsilon"},
    {"T", "F", "T'"},
    {"T'", "*", "F", "T'", {":=", "temp"}},
    {"T'", "/", "F", "T'", {":=", "temp"}},
    {"T'", "epsilon"},
    {"F", "(", "E", ")", {":=", "temp"}},
    {"F", "id", {":=", "id"}}
};

// Define the parsing table
const unordered_map<string, unordered_map<string, int>> PARSING_TABLE = {
    {"E", {
        {"(", 0},
        {"id", 0}
    }},
    {"E'", {
        {"+", 1},
        {"-", 2},
        {")", 3},
        {"$", 3}
    }},
    {"T", {
        {"(", 4},
        {"id", 4}
    }},
    {"T'", {
        {"*", 5},
        {"/", 6},
        {"+", 7},
        {"-", 7},
        {")", 7},
        {"$", 7}
    }},
    {"F", {
        {"(", 8},
        {"id", 9}
    }}
};

// Returns the production rule for the given nonterminal symbol and lookahead symbol
vector<string> get_production_rule(string nonterminal, string lookahead) {
    return PRODUCTIONS[PARSING_TABLE.at(nonterminal).at(lookahead)];
}

string get_production_string(const vector<string>& production) {
    string production_string = "";
    for (const auto& symbol : production) {
        production_string += symbol + " ";
    }
    // Remove the extra space at the end
    if (!production_string.empty()) {
        production_string.pop_back();
    }
    return production_string;
}

// Parse the input string using the given grammar and parsing table
// Parse the input tokens using the given grammar and parsing table
bool parse_input(const vector<string>& tokens) {
    stack<string> stk;
    stk.push("$");
    stk.push("E");
    int temp_counter = 0;
    size_t pos = 0;
    while (!stk.empty() && pos <= tokens.size()) {
        string top = stk.top();
        stk.pop();
        string lookahead = pos < tokens.size() ? tokens[pos] : "$";
        if (top == lookahead) {
            pos++;
        } else if (PARSING_TABLE.find(top) != PARSING_TABLE.end() && PARSING_TABLE.at(top).find(lookahead) != PARSING_TABLE.at(top).end()) {
            vector<string> production = get_production_rule(top, lookahead);
            if (top == "E'") {
                if (production[1] == "+") {
                    cout << "t" << ++temp_counter << " = ";
                    cout << production[0] << " + ";
                    cout << production[2] << endl;
                    cout << "E' = t" << temp_counter << endl;
                } else if (production[1] == "-") {
                    cout << "t" << ++temp_counter << " = ";
                    cout << production[0] << " - ";
                    cout << production[2] << endl;
                    cout << "E' = t" << temp_counter << endl;
                } else {
                    cout << "E' = epsilon" << endl;
                }
            } else if (top == "T'") {
                if (production[1] == "*") {
                    cout << "t" << ++temp_counter << " = ";
                    cout << production[0] << " * ";
                    cout << production[2] << endl;
                    cout << "T' = t" << temp_counter << endl;
                } else if (production[1] == "/") {
                    cout << "t" << ++temp_counter << " = ";
                    cout << production[0] << " / ";
                    cout << production[2] << endl;
                    cout << "T' = t" << temp_counter << endl;
                } else {
                    cout << "T' = epsilon" << endl;
                }
            }
            for (int i = production.size() - 1; i > 0; i--) {
                if (production[i] != "epsilon") {
                    stk.push(production[i]);
                }
            }
            cout << get_production_string(production) << endl;
        } else {
            return false;
        }
    }
    return pos == tokens.size() + 1;
}

// Generate three-address code for the given production
string  generate_three_address_code(const vector<string>& production, int& temp_var_counter, const string& marker) {
    string code = "";
    string nonterminal = production[0];
    if (nonterminal == "E") {
        // E -> T E'
        string t1 = marker + to_string(temp_var_counter++);
        code += generate_three_address_code({"T", t1, "E'"}, temp_var_counter, marker);
    } else if (nonterminal == "E'") {
        // E' -> + T E' | - T E' | epsilon
        if (production.size() > 1) {
            string t1 = marker + to_string(temp_var_counter++);
            string t2 = marker + to_string(temp_var_counter++);
            code += generate_three_address_code({"T", t1, t2}, temp_var_counter, marker);
            string t3 = marker + to_string(temp_var_counter++);
            code += t3 + " := " + t1 + " " + production[1] + " " + t2 + "\n";
            string t4 = marker + to_string(temp_var_counter++);
            code += generate_three_address_code({"E'", t4}, temp_var_counter, marker);
            code += t4 + " := " + t3 + "\n";
        }
    } else if (nonterminal == "T") {
        // T -> F T'
        string t1 = marker + to_string(temp_var_counter++);
        code += generate_three_address_code({"F", t1, "T'"}, temp_var_counter, marker);
    } else if (nonterminal == "T'") {
        // T' -> * F T' | / F T' | epsilon
        if (production.size() > 1) {
            string t1 = marker + to_string(temp_var_counter++);
            string t2 = marker + to_string(temp_var_counter++);
            code += generate_three_address_code({"F", t1, t2}, temp_var_counter, marker);
            string t3 = marker + to_string(temp_var_counter++);
            code += t3 + " := " + t1 + " " + production[1] + " " + t2 + "\n";
            string t4 = marker + to_string(temp_var_counter++);
            code += generate_three_address_code({"T'", t4}, temp_var_counter, marker);
            code += t4 + " := " + t3 + "\n";
        }
    } else if (nonterminal == "F") {
        // F -> ( E ) | id
        if (production[1] == "(") {
            string t1 = marker + to_string(temp_var_counter++);
            code += generate_three_address_code({"E", t1}, temp_var_counter, marker);
            code += production[0] + " := " + t1 + "\n";
        } else {
            code += production[0] + " := " + production[1] + "\n";
        }
    }
    return code;
}

// Generate a new temporary variable name
string generate_temp_variable() {
    static int count = 0;
    string temp_name = "t" + to_string(count);
    count++;
    return temp_name;
}

// Generate three-address code for a given production rule
void generate_code_for_production(const vector<string>& production) {
    static int count = 0;
    string temp_name;
    if (production[0] == "E") {
        temp_name = generate_temp_variable();
        cout << temp_name << " = ";
    }
    if (production[0] == "E'") {
        cout << "goto L" << count << endl;
        cout << "L" << count << ":" << endl;
        count++;
    }
    if (production[0] == "T'") {
        temp_name = generate_temp_variable();
        cout << temp_name << " = ";
    }
    if (production[0] == "F") {
        temp_name = production[1];
    }
    for (int i = 1; i < production.size(); i++) {
        if (production[i] == "+") {
            cout << " + ";
        } else if (production[i] == "-") {
            cout << " - ";
        } else if (production[i] == "*") {
            cout << " * ";
        } else if (production[i] == "/") {
            cout << " / ";
        } else if (production[i] == "(") {
            if (i == 1) {
                cout << production[i];
            } else {
                cout << "(";
            }
        } else if (production[i] == ")") {
            if (i == production.size() - 1) {
                cout << ")" << endl;
            } else {
                cout << ")";
            }
        } else if (production[i] == "id") {
            if (i == 1) {
                cout << temp_name << " = " << production[i];
            } else {
                cout << production[i];
            }
        } else if (production[i] == "epsilon") {
            // Do nothing
        }
    }
}

void generate_code(const string& expression) {
    // Tokenize the input expression
    vector<string> tokens = tokenize(expression);

    // Parse the input expression
    if (!parse_input(tokens)) {
        cout << "Error: Invalid input expression" << endl;
        return;
    }

    // Generate three-address code for the input expression
    int temp_var_counter = 1;
    string marker = "t";
    string code = generate_three_address_code(tokens, temp_var_counter, marker);

    // Output the generated code
    cout << "Three-address code:" << endl;
    cout << code;
}



int main() {
    string input;
    cout << "Enter an arithmetic expression: ";
    getline(cin, input);
    vector<string> tokens = tokenize(input);
    bool success = parse_input(tokens);
    if (success) {
        cout << "Valid expression!" << endl;
        vector<string> code = generate_three_address_code(tokens);
        cout << "Generated three-address code:" << endl;
        for (const string& line : code) {
            cout << line << endl;
        }
    } else {
        cout << "Invalid expression!" << endl;
    }
    return 0;
}
