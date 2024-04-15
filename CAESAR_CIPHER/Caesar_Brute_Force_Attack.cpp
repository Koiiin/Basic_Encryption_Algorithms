#include <iostream>
#include <string>

using namespace std;

string caesar_decrypt(string ciphertext, int key) {
  string plaintext = "";
  for (char c : ciphertext) {
    int ascii_value = c - 'A';
    int new_ascii_value = (ascii_value - key + 26) % 26;
    char new_char = (char)(new_ascii_value + 'A');
    plaintext += new_char;
  }
  return plaintext;
}

int main() {
  string ciphertext;
  getline(cin, ciphertext);
  for (int key = 0; key < 26; key++) {
    string plaintext = caesar_decrypt(ciphertext, key);
    cout << "Key " << key << ": " << plaintext << endl;
  }
  return 0;
}
