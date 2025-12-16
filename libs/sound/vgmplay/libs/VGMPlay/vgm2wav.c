/*
 *  This file is part of VGMPlay <https://github.com/vgmrips/vgmplay>
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <wchar.h>

#include <fcntl.h>

#include "./vgm2wav.h"

#ifndef _MSC_VER
// This turns command line options on (using getopt.h) unless you are using MSVC / Visual Studio, which doesn't have it.
#define VGM2WAV_HAS_GETOPT
#include <getopt.h>
#endif

#include "chips/mamedef.h"
#include "stdbool.h"
#include "VGMPlay.h"
#include "VGMPlay_Intf.h"

#define SAMPLESIZE sizeof(WAVE_16BS)

UINT8 CmdList[0x100]; // used by VGMPlay.c and VGMPlay_AddFmts.c
bool ErrorHappened;   // used by VGMPlay.c and VGMPlay_AddFmts.c
extern VGM_HEADER VGMHead;
extern UINT32 SampleRate;
extern bool EndPlay;

extern UINT32 VGMMaxLoop;
extern UINT32 FadeTime;

bool WriteSmplChunk;

INLINE int fputLE16(UINT16 Value, FILE* hFile)
{
	int RetVal;
	int ResVal;

	RetVal = fputc((Value & 0x00FF) >> 0, hFile);
	RetVal = fputc((Value & 0xFF00) >> 8, hFile);
	ResVal = (RetVal != EOF) ? 0x02 : 0x00;
	return ResVal;
}

INLINE int fputLE32(UINT32 Value, FILE* hFile)
{
	int RetVal;
	int ResVal;

	RetVal = fputc((Value & 0x000000FF) >> 0, hFile);
	RetVal = fputc((Value & 0x0000FF00) >> 8, hFile);
	RetVal = fputc((Value & 0x00FF0000) >> 16, hFile);
	RetVal = fputc((Value & 0xFF000000) >> 24, hFile);
	ResVal = (RetVal != EOF) ? 0x02 : 0x00;
	return ResVal;
}


int vgm2wav(char *vgm_filepath, char *out_filepath) {
	WAVE_16BS *sampleBuffer;
	UINT32 bufferedLength;
	FILE *outputFile;

	long int wavRIFFLengthPos;
	long int wavDataLengthPos;
	int sampleBytesWritten = 0;

	// Initialize VGMPlay before parsing arguments, so we can set VGMMaxLoop and FadeTime
	VGMPlay_Init();
	VGMPlay_Init2();

	VGMMaxLoop = 2;
	FadeTime = 5000;
	WriteSmplChunk = true;

	int c;

	if (!OpenVGMFile(vgm_filepath)) {
		fprintf(stderr, "vgm2wav: error: failed to open vgm_file (%s)\n", vgm_filepath);
		return 1;
	}


	outputFile = fopen(out_filepath, "wb");
	if (outputFile == NULL) {
		fprintf(stderr, "vgm2wav: error: failed to open wav_file (%s)\n", outputFile);
		return 1;
	}

	if (WriteSmplChunk && VGMHead.lngLoopSamples == 0) {
		WriteSmplChunk = false;
	}

	fwrite("RIFF", 1, 4, outputFile);

	wavRIFFLengthPos = ftell(outputFile);
	fputLE32(-1, outputFile);

	fwrite("WAVE", 1, 4, outputFile);

	fwrite("fmt ", 1, 4, outputFile);
	fputLE32(16, outputFile);
	fputLE16(1, outputFile);
	fputLE16(2, outputFile);
	fputLE32(SampleRate, outputFile);
	fputLE32(SampleRate * 2 * 2, outputFile);
	fputLE16(2 * 2, outputFile);
	fputLE16(16, outputFile);

	if (WriteSmplChunk) {
		fwrite("smpl", 1, 4, outputFile);
		fputLE32(60, outputFile);
		fputLE32(0, outputFile);
		fputLE32(0, outputFile);
		fputLE32(0, outputFile);
		fputLE32(0, outputFile);
		fputLE32(0, outputFile);
		fputLE32(0, outputFile);
		fputLE32(0, outputFile);
		fputLE32(1, outputFile);
		fputLE32(0, outputFile);

		fputLE32(0, outputFile);
		fputLE32(0, outputFile);
		fputLE32(VGMHead.lngTotalSamples - VGMHead.lngLoopSamples, outputFile);
		fputLE32(VGMHead.lngTotalSamples, outputFile);
		fputLE32(0, outputFile);
		fputLE32(0, outputFile);
	}

	fwrite("data", 1, 4, outputFile);

	wavDataLengthPos = ftell(outputFile);
	fputLE32(-1, outputFile);

	PlayVGM();

	sampleBuffer = (WAVE_16BS*)malloc(SAMPLESIZE * SampleRate);
	if (sampleBuffer == NULL) {
		fprintf(stderr, "vgm2wav: error: failed to allocate %lu bytes of memory\n", SAMPLESIZE * SampleRate);
		return 1;
	}

	while (!EndPlay) {
		UINT32 bufferSize = SampleRate;
		bufferedLength = FillBuffer(sampleBuffer, bufferSize);
		if (bufferedLength) {
			UINT32 numberOfSamples;
			UINT32 currentSample;
			const UINT16* sampleData;

			sampleData = (UINT16*)sampleBuffer;
			numberOfSamples = SAMPLESIZE * bufferedLength / 0x02;
			for (currentSample = 0x00; currentSample < numberOfSamples; currentSample++) {
				fputLE16(sampleData[currentSample], outputFile);
				sampleBytesWritten += 2;
			}
		}
	}

	fflush(outputFile);
	StopVGM();

	CloseVGMFile();

	VGMPlay_Deinit();

	if (wavRIFFLengthPos >= 0) {
		fseek(outputFile, wavRIFFLengthPos, SEEK_SET);
		if (WriteSmplChunk) {
			fputLE32(sampleBytesWritten + 28 + 68 + 8, outputFile);
		} else {
			fputLE32(sampleBytesWritten + 28 + 8, outputFile);
		}
	}
	if (wavDataLengthPos >= 0) {
		fseek(outputFile, wavDataLengthPos, SEEK_SET);
		fputLE32(sampleBytesWritten, outputFile);
	}

	return 0;
}

int main(int argc, char *argv[]) {
	char *vgm_filepath = argv[1];
	char *out_filepath = argv[2];

	// vgm_file:../../tests/nakama.vgmOpenVGMFile
	printf("\n\nvgm_file:");
	printf(vgm_filepath);

	return vgm2wav(vgm_filepath, out_filepath);

	// return vgm2wav(vgm_filepath, "../../tests/nakama-2.wav");

}
