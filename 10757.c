#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define max(a, b)  ((a > b) ? a : b)

char num1[10000];
char num2[10000];

int main() {
    scanf("%s %s", num1, num2);
    int num1_length = (int)strlen(num1);
    int num2_length = (int)strlen(num2);
    int max_length = max((int)strlen(num1), (int)strlen(num2));

    char* num1_r = (char*)malloc((num1_length + 1) * sizeof(char));
    num1_r[num1_length] = '\0';
    char* num2_r = (char*)malloc((num2_length + 1) * sizeof(char));
    num2_r[num2_length] = '\0';

    for (int i = 0; i < num1_length; i++) { num1_r[i] = num1[num1_length - 1 - i]; }
    for (int i = 0; i < num2_length; i++) { num2_r[i] = num2[num2_length - 1 - i]; }
    
    char* result_r = (char*)malloc((max_length + 2) * sizeof(char));
    result_r[max_length + 1] = '\0';
    
    int up = 0;
    for (int i = 0; i < max_length; i++) {
        int r = up;
        if (num1_length > i) { r += num1_r[i] - '0'; }
        if (num2_length > i) { r += num2_r[i] - '0'; }
        
        if (r != 0) {
            up = r / 10;
            r %= 10;
        }
        result_r[i] = (char)(r + '0');
    }
    if (up != 0) { result_r[max_length] = (char)(up + '0'); }

    char* result = (char*)malloc((max_length + 2) * sizeof(char));
    result[max_length + 1] = '\0';
    for (int i = 0; i < strlen(result_r) + 1; i++) {
            if (up != 0) { result[i] = result_r[max_length - i]; }
            else { result[i] = result_r[max_length - 1 - i]; }
        }

    printf("%s\n", result);
    return 0;
}