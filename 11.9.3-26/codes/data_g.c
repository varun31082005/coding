#include <stdio.h>

int main() {
    FILE *file = fopen("data.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    int a = 3;
    int r= 3;
    int start_n = 0;
    int end_n = 4;
    int term =1;
    for (int n = start_n; n < end_n; ++n) {
        int x_n = (term*r) > 0 ? (term*r) : 0;
        term = x_n;
        fprintf(file, "%d %d\n", n, x_n);
    }

    fclose(file);

    return 0;
}
