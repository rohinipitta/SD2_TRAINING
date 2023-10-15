#include <stdio.h>

int main() {
    int i, j;

    // Loop through the numbers from 1 to 10
    for (i = 1; i <= 10; i++) {
        // Check if the square of the number is in the range [40, 100]
        if (i * i >= 40 && i * i <= 100) {
            // Print the square of the number
            printf("%d \t", i * i);
        }
    }
    
    return 0;
}
