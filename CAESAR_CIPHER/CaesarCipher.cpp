#include <iostream>
#include <string>

using namespace std;

// Hàm mã hóa văn bản plaintext
string caesarCipherEncrypt(string plaintext, int shift) {
    string ciphertext = "";

    for (int i = 0; i < plaintext.length(); ++i) {
        // Kiểm tra xem ký tự có phải là chữ cái không
        if (isalpha(plaintext[i])) {
            // Tính toán chỉ số mới của ký tự
            char encryptedChar = (isupper(plaintext[i])) ? 
                                    ((plaintext[i] - 'A' + shift) % 26 + 'A') :
                                    ((plaintext[i] - 'a' + shift) % 26 + 'a');
            ciphertext += encryptedChar;
        } else {
            // Nếu không phải là chữ cái, giữ nguyên ký tự
            ciphertext += plaintext[i];
        }
    }

    return ciphertext;
}

int main() {
    int shift;
    string plaintext;

    // Nhập độ dịch chuyển và plaintext
    cin >> shift;
    cin.ignore(); // Loại bỏ ký tự newline còn lại sau khi nhập shift
    getline(cin, plaintext);

    // Mã hóa plaintext và in ra ciphertext
    cout << caesarCipherEncrypt(plaintext, shift);

    return 0;
}
