#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_WORDS 1000
#define MAX_LENGTH 100

typedef struct {
    char word[MAX_LENGTH];
    int count;
} WordFreq;

int main() {
    char paragraph[1000];
    WordFreq freq[MAX_WORDS];
    int wordCount = 0;

    for (int i = 0; i < MAX_WORDS; i++) {
        freq[i].count = 0;
    }

    printf("Enter a paragraph:\n");
    fgets(paragraph, sizeof(paragraph), stdin);

    char *token = strtok(paragraph, " .,!?;:\n");
    while (token != NULL) {
        for (int i = 0; token[i]; i++)
            token[i] = tolower(token[i]);

        int found = 0;
        for (int i = 0; i < wordCount; i++) {
            if (strcmp(freq[i].word, token) == 0) {
                freq[i].count++;
                found = 1;
                break;
            }
        }

        if (!found) {
            strcpy(freq[wordCount].word, token);
            freq[wordCount].count = 1;
            wordCount++;
        }

        token = strtok(NULL, " .,!?;:\n");
    }

    printf("\nWord Frequencies:\n");
    for (int i = 0; i < wordCount; i++) {
        printf("%s: %d\n", freq[i].word, freq[i].count);
    }

    return 0;
}
