#include <stdio.h>
#include <stdlib.h>

void merge (int array[], int left, int m, int right)
{
  int i, j, k;
  int n1 = m - left + 1;
  int n2 = right - m;

  int tempArray1[n1];
  int tempArray2[n2];

  for (i = 0; i < n1; i++)
  {
    tempArray1[i] = array[left + i];
  }
  for (j = 0; j < n2; j++)
  {
    tempArray2[j] = array[m + 1 + j];
  }

  i = 0;
  j = 0;
  k = left;

  while(i < n1 && j < n2)
  {
    if (tempArray1[i] <= tempArray2[j])
    {
      array[k] = tempArray1[i];
      i++;
    } else {
      array[k] = tempArray2[j];
      j++;
    }
    k++;
  }

  while(i < n1) {
    array[k] = tempArray1[i];
    i++;
    k++;
  }
  while(j < n2) {
    array[k] = tempArray2[j];
    j++;
    k++;
  }
}

void mergeSort (int array[], int left, int right)
{
  int m;
  if (left < right)
  {
    m = (left + right)/2;

    mergeSort(array, left, m);
    mergeSort(array, m+1, right);

    merge(array, left, m, right);
  }
}

void printArray(int array[], int right)
{
  int i;
  for(i = 0; i < right; i++)
  {
    printf("%d, ", array[i]);
  }
}

int main(int argc, char const *argv[]) {
  int array[] = {1, 10, 958, 95, 69, 35, 420};

  int sizeArray = sizeof(array)/sizeof(array[0]);

  printf("Array is \n");
  printArray(array, sizeArray);

  mergeSort(array, 0, sizeArray-1);

  printf("After merge sort algorithm\n");
  printArray(array, sizeArray);
  return 0;
}
