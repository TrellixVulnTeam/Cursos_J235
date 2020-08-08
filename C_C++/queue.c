#include <stdio.h>
#define SIZE 5

//Code 2 functions → dequeue - enqueue

int values[SIZE], front = -1, rear = -1;

void enQueue (int value)
{
  //Before adding I check if there is space
  //Check position of rear. It gotta be < SIZE
  if(rear == SIZE - 1)
  {
    printf("Queue is full\n");
  }
  else
  {
    //If is the first element → front = 0
    if (front == -1)
    {
      front = 0;
    }
    rear++;
    //Giving value to position of rear in array
    values[rear] = value;
    printf("Element %d has been succesfully added\n", value);
  }
}

//This doesn't need an input because it is the LIFO criterion
//wich decides what member is going out
void deQueue ()
{
  //Verifying there are elements
  if (front == -1)
  {
    printf("Queue is empty. Please enter at least one element\n");
  }
  else
  {
      for(int i=0; i <= rear; i++)
      {
        values[i] = values[i+1];
      }
      rear--;
  }
}


void printQueue ()
{
  for (int i = 0; i <= rear; i++)
  {
    int auxval;
    auxval = values[i];
    printf("%d\n", auxval);
  }
}

int main(int argc, char const *argv[]) {

  enQueue(1);
  enQueue(2);
  enQueue(3);
  enQueue(4);
  enQueue(5);

  deQueue();
  deQueue();

  enQueue(9);

  printQueue();

  return 0;
}
