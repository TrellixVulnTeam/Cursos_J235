#include <stdio.h>

void swapValues(int *previous1, int *previous2)
{
  int buffer = *previous1;
  *previous1 = *previous2;
  *previous2 = buffer;
}

int partition(int arr[], int low, int high)
{
  int i = (low - 1); //index for smaller element
  int pivot = arr[high];
  int j;

  for (j = low; j < high; j++)
  {
    if (arr[j] <= pivot)
    {
      i++;
      swapValues(&arr[i], &arr[j]);
    }
  }
  swapValues(&arr[i+1], &arr[high]);
  return (i + 1);
}

void quickSort (int arr[], int low, int high)
{
  if(low < high)
  {
    int pi = partition(arr, low, high); //partition index
    quickSort(arr, low, pi-1);
    quickSort(arr, pi+1, high);
  }
}

void printArray (int arr[], int n)
{
  for (int i = 0; i < n; i++)
  {
    printf("%d\n", arr[i]);
  }
}

int main(int argc, char const *argv[]) {
  int arr[] = {10, 7, 8, 9, 1, 5};
  int n = sizeof(arr)/sizeof(arr[0]);

  quickSort(arr, 0, n-1);

  printf("Sorted array is: \n");
  printArray(arr, n);

  return 0;
}
