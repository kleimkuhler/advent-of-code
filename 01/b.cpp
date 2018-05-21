#include <iostream>
#include <string>
#include <vector>

using std::cout;   using std::cin;
using std::endl;   using std::string;

int main()
{
  string s;
  cin >> s;

  int half = s.size() / 2;
  int sum = 0;
  string::size_type j;
  for (string::size_type i = 0; i != s.size(); ++i) {
    // j = cyclical i+1 index
    j = (i + half) % s.size();

    int i_val = s[i] - '0';
    int j_val = s[j] - '0';
    if (i_val == j_val)
      sum += i_val;
  }
  cout << sum << endl;
  return 0;
}
