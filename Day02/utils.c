// #include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
// #include <string.h>

int find_max_line_length(char *file_str) {
  FILE *file;
  int c;
  int line_length;
  int max_line_length;

  line_length = 0;
  max_line_length = 0;

  file = fopen(file_str, "r");
  if (!file) {
    perror("Error opening file");
    exit(1);
  }
  while ((c = fgetc(file)) != EOF) {
    line_length++;
    if (c == '\n') {
      if (line_length > max_line_length) {
        max_line_length = line_length;
      }
      line_length = 0;
    }
    if (line_length > max_line_length) {
      max_line_length = line_length;
    }
  }
  return (max_line_length);
}