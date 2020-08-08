#include <stdio.h>

long factorial (int n)
{
  if (n == 0)
  {
    return 1;
  }
  else
  {
    return (n * factorial(n-1));
  }
}

int main(int argc, char const *argv[]) {
  long resultado;
  int n;
  printf("Tip a number below\n");
  do {
  scanf("%d", &n);
  } while(n < 0);

  resultado = factorial(n);
  printf("%d! = %d\n", n, resultado);
  return 0;
}
