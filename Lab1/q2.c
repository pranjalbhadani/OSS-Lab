#include <stdio.h>

int main() {
    int n, i;
    float sum = 0.0, average;

    // Ask for the number of elements
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    int arr[n];

    // Read the elements from the user
    printf("Enter %d integers:\n", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }

    // Calculate the average
    average = sum / n;

    // Display the result
    printf("The average is: %.2f\n", average);

    return 0;
}
