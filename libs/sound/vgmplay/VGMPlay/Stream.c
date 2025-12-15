// Stream.c: C Source File for Sound Output
//

// Thanks to nextvolume for NetBSD support
#define _GNU_SOURCE
#include <stdio.h>
#include "stdbool.h"
#include <stdlib.h>

#ifdef WIN32
#include <windows.h>
#ifdef USE_LIBAO
#error "Sorry, but this doesn't work yet!"
#endif // USE_LIBAO
#else
#include <unistd.h>
#include <limits.h>
#include <sys/ioctl.h>
#include <fcntl.h>

#ifdef USE_LIBAO
#include <ao/ao.h>
#else
#ifdef __NetBSD__
#include <sys/audioio.h>
#elif defined(__linux__)
#include <linux/soundcard.h>
#endif // __NETBSD__
#endif // USE_LIBAO

#endif // WIN32

#include "chips/mamedef.h"	// for UINT8 etc.
#include "VGMPlay.h"	// neccessary for VGMPlay_Intf.h
#include "VGMPlay_Intf.h"
#include "Stream.h"

#ifndef WIN32
typedef struct
{
	UINT16 wFormatTag;
	UINT16 nChannels;
	UINT32 nSamplesPerSec;
	UINT32 nAvgBytesPerSec;
	UINT16 nBlockAlign;
	UINT16 wBitsPerSample;
	UINT16 cbSize;
} WAVEFORMATEX;	// from MSDN Help

#define WAVE_FORMAT_PCM	0x0001

#endif

#ifdef WIN32
static DWORD WINAPI WaveOutThread(void* Arg);
static void BufCheck(void);
#else
void WaveOutCallbackFnc(void);
#endif

UINT16 AUDIOBUFFERU = AUDIOBUFFERS;		// used AudioBuffers

WAVEFORMATEX WaveFmt;
extern UINT32 SampleRate;
extern volatile bool PauseThread;
volatile bool StreamPause;
extern bool ThreadPauseEnable;
extern volatile bool ThreadPauseConfrm;

UINT32 BlockLen;
#ifdef WIN32
static HWAVEOUT hWaveOut;
static WAVEHDR WaveHdrOut[AUDIOBUFFERS];
static HANDLE hWaveOutThread;
//static DWORD WaveOutCallbackThrID;
#else
static INT32 hWaveOut;
#endif
static bool WaveOutOpen;
UINT32 BUFFERSIZE;	// Buffer Size in Bytes
UINT32 SMPL_P_BUFFER;
static char BufferOut[AUDIOBUFFERS][BUFSIZE_MAX];
static volatile bool CloseThread;


bool SoundLog;
static FILE* hFile;
UINT32 SndLogLen;

UINT32 BlocksSent;
UINT32 BlocksPlayed;

char SoundLogFile[MAX_PATH];

#ifdef USE_LIBAO
ao_device* dev_ao;
#endif
