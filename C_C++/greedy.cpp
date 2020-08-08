#include <iostream>
#include <climits>
#include <string.h>

using namespace std;

int greedyChange(int coinSet[], int n, int debt)
{
  //Validations
  if (debt == 0)
    return 0;

  if (debt < 0)
    return INT_MAX;

  //coins will store coins in use
  int coins = INT_MAX;

  //Traverse the full coinset (or options)
  for (int i = 0; i < n; i++)
  {
    int result = greedyChange(coinSet, n, debt - coinSet[i]);

    if(result != INT_MAX)
      coins = min(coins, result+1);
  }
  return coins;
}

int main(int argc, char const *argv[]) {
  int coinSet[]= {1, 5, 10, 15, 20};
  int n = sizeof(coinSet)/sizeof(coinSet[0]);

  //The amount that client is asking for
  int N = 27;

  cout << "Minimum amount of coins is: " << greedyChange(coinSet, n, N) << endl;

  return 0;
}
