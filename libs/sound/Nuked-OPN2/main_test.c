// Header file for input output functions
#include <stdio.h>

#include "ym3438.h"


// 

// https://github.com/nukeykt/Nuked-OPN2
// https://github.com/nukeykt/Genesis-Plus-GX

// g++ main_test.c -o prog && ./prog

// g++ main_test.c ./ym3438.c -o prog && ./prog.exe

// https://github.com/nukeykt/Genesis-Plus-GX/commit/dd6165785f321a8dd3d2de89cbe638a70dc6286e


// msys
// cd /c/Users/russj/dev/python-misc/libs/sound/Nuked-OPN2
// g++ main_test.c ./ym3438.c -o prog && ./prog.exe

// https://www.vogons.org/viewtopic.php?t=36417
// https://racketboy.com/forum/viewtopic.php?t=43797


// https://cdn.hackaday.io/files/1736867430981824/DAFM%20GENESIS_user%20manual.pdf

// https://theretroweb.com/chip/documentation/ym3438-67b9ee32befa7843209071.pdf

// https://github.com/AidanHockey5/STM32_VGM_Player_YM2612_SN76489#ym3438-support

// https://www.smspower.org/Music/VGMFileFormat
int main() {
    OPN2_SetChipType(ym3438_mode_ym2612);


    // printf("Hello");
    // printf("Hello the output is %d \n",add(10,15));

    int8_t test = 1;

    ym3438_t chip;

    printf("start:\n\n");
    // printf("address: %d\n", chip.address);
    // printf("busy: %d\n", chip.busy); // whatever happened to be in memory at the time

    OPN2_Reset(&chip);

    // https://github.com/nukeykt/Genesis-Plus-GX/blob/4b5ccd7767ec037dc41864c1167eaa66ca452e6b/libretro/libretro.c#L1215C1-L1216C1

    printf("address: %d\n", chip.address);
    printf("busy: %d\n", chip.busy);
    // printf("type: %d\n", chip.);

    // return


    
    printf("read test pin: %d\n", OPN2_ReadTestPin(&chip));
    printf("read test pin: %d\n", OPN2_ReadTestPin(&chip));
    printf("read test pin: %d\n", OPN2_ReadTestPin(&chip));


    // typedef uint32_t        Bit32u;
    // https://stackoverflow.com/questions/78958016/how-to-tell-gcc-that-a-pointer-is-non-null
    Bit32u port = 0;
    printf("OPN2_Read port %d: %d\n", port, OPN2_Read(&chip, 0));

    port = 1;
    printf("OPN2_Read pin %d: %d\n", port, OPN2_Read(&chip, 0));


// https://github.com/nukeykt/Genesis-Plus-GX/blob/master/core/memz80.c#L257 calls fm_write
// fm_write is set to       fm_write = YM3438_Write;
//   /* synchronize FM chip with CPU */
//   fm_update(cycles);

//   /* write FM register */
//   OPN2_Write(&ym3438, a, v);

    port = 0;
    Bit8u data = 1;
    Bit16s buffer;

    OPN2_Write(&chip, port, data);
        // buffer[0] = chip->mol;
    // buffer[1] = chip->mor;
    OPN2_Clock(&chip, &buffer);  // OPN2_DoRegWrite(&chip);
    printf("OPN2_Read pin %d: %d\n", port, OPN2_Read(&chip, port));

    int i = 0;

    while (i < 100) {
        // printf("OPN2_Read pin %d: %d\n", port, OPN2_Read(&chip, port));

        OPN2_Write(&chip, port, i);

            // buffer[0] = chip->mol;
        // buffer[1] = chip->mor;
        OPN2_Clock(&chip, &buffer);  // OPN2_DoRegWrite(&chip);
        printf("buffer: %d\n", buffer);

        // printf("OPN2_Read pin %d: %d\n", port, OPN2_Read(&chip, port));
        i ++;

    }
    return 0;
}