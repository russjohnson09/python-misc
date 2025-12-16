
#include <stdio.h>
#include <stdlib.h>

// https://www.geeksforgeeks.org/dsa/sin-in-c/
#include <stdio.h>

// /usr/bin/ld: libvgm.so: undefined reference to `sin'
// /usr/bin/ld: libvgm.so: undefined reference to `pow'
#include <math.h>


// /usr/bin/ld: libvgm.so: undefined reference to `DUMMYBUF'
#include "VGMPlay/chips/mamedef.h"
// /mnt/c/Users/russj/dev/python-misc/libs/sound/vgmplay/libs/VGMPlay/chips/opl.h:45:9: error: unknown type name ‘UINT32’
//    45 | typedef UINT32          Bitu;
typedef unsigned int						UINT32;
typedef signed int							INT32;

// create extern stream_sample_t* DUMMYBUF[];
// This is a global stream used for all chips
stream_sample_t* DUMMYBUF[0x02] = {NULL, NULL};

// libs\sound\vgmplay\libs\VGMPlay\chips\adlibemu_opl3.c
// #include "VGMPlay/chips/adlibemu_opl3.c"

// another extern where is the h file for this one??
// libs\sound\vgmplay\libs\VGMPlay\VGMPlay.c
// INT32 CHIP_SAMPLE_RATE;
// UINT8 CHIP_SAMPLING_MODE;

// UNIT32



// /mnt/c/Users/russj/dev/python-misc/libs/sound/vgmplay/libs/VGMPlay/chips/opl.h:45:9: error: unknown type name ‘UINT32’
//    45 | typedef UINT32          Bitu;

// /usr/bin/ld: libvgm.so: undefined reference to `adlib_OPL3_reg_read'
//         run: sudo apt-get install make gcc zlib1g-dev libao-dev libdbus-1-dev  -y

// #define ADLIBEMU(name)			adlib_OPL3_##name
// libs\sound\vgmplay\libs\VGMPlay\chips\adlibemu.h


// DUMMYBUF

// libs\sound\vgmplay\libs\VGMPlay\VGMPlay.c
// extern stream_sample_t* DUMMYBUF[];


int hello_world() {
	printf("hello world\n\n");
}