#include <stdio.h>
#include <string.h>

typedef struct Client {
  char Name[100];
  char CreditCard[50];

} CLIENT;

int main(int argc, char const *argv[]) {
  CLIENT client1 = {0};
  char buffer [100];

  printf ("Tip your name below \n");
  scanf("%s", buffer);
  strcpy(client1.Name, buffer);

  printf ("Tip your card's number below \n");
  scanf("%s", buffer);
  strcpy(client1.CreditCard, buffer);

  printf ("Client's name is: %s. Credit card is %s\n", client1.Name, client1.CreditCard);

  return 0;
}
