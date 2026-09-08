#include<stdio.h>
#include<math.h>


int checker (int inter_text) {
    int status = 1;
    if (inter_text / (int)pow(10, 8) < 2) {
        for (int i = 1; i < 9; ++i) {
            int microzone;
            microzone = inter_text % 10;
            inter_text = inter_text / 10;

            if (microzone < 0 || microzone > 1) {
                status = 0;
                break;
            }
        }
    }
    else {
        status = 0;
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
    printf("your bin number: \n");
    int bin_num;
    scanf ("%d", &bin_num);

    if (checker(bin_num)){
        printf("your dec number: \n");
        printf ("%d", bin2dec(bin_num));
    }

    else{
        printf ("have an error\n");
    }


    return 0;
}
