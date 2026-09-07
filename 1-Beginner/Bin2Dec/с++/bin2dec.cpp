#include <iostream>
#include <cmath>


bool checker (int inter_text) {
    bool status = true;
    if (inter_text / (int)pow(10, 8) < 2) {
        for (int i = 1; i < 9; ++i) {
            int microzone;
            microzone = inter_text % 10;
            inter_text = inter_text / 10;

            if (microzone < 0 || microzone > 1) {
                status = false;
                break;
            }
        }
    }
    else {
        status = false;
    }

    return status;
}

int bin2dec (int numb) {
    int numdec = 0;

    for (int i = 0; i < 8; ++i) {
        int zone;
        zone = (numb % (int)(pow(10, (i + 1)))) / (int)pow(10,(i));
        numdec += zone * (int)(pow(2, i));
    }


    return numdec;
}

int main() {
    std :: cout << "your bin number: \n";
    int bin_num;
    std :: cin >> bin_num;

    if (checker(bin_num)){
        std :: cout << "your dec number: " << bin2dec(bin_num);
    }

    else{
        std :: cout << "have an error\n";
    }


    return 0;
}
