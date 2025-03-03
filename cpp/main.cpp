#include <iostream>

/**
 * Booleans are declared false by default 
 */

int main() {
  bool foo;
  std::cout << foo;

  bool bar;
  std::cout << bar;
  
  if (!bar){
    std::cout << "This is a message";
  }

  std::cout << foo + bar;
}
