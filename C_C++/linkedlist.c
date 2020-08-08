#include <stdio.h>
#include <stdlib.h>

struct Node {
  int data;
  int *next;
};

int main(int argc, char const *argv[]) {

  //Initializing nodes. Accessing to NODE content
  struct Node* node1 = NULL;
  struct Node* node2 = NULL;
  struct Node* node3 = NULL;

  //Allocating dinamically in memory
  node1 = (struct Node*)malloc(sizeof(struct Node));
  node2 = (struct Node*) malloc(sizeof(struct Node));
  node3 = (struct Node*) malloc(sizeof(struct Node));

  node1->data = 3;
  node1->next = node2;

  node2->data = 9;
  node2->next = node3;

  node3->data = 15;
  node3->next = NULL;

return 0;
}
