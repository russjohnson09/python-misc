# git clean -dxf -- .
# make

# cd /c/Users/russj/dev/python-misc/libs/sound/vgmplay/libs/VGMPlay
# make WINDOWS=1
# ./vgm2wav
# ./vgm2wav ../../tests/nakama.vgm ../../tests/nakama.wav
# ./vgm2wav ../../tests/02\ Game\ Start\ Music.vgz ../../tests/galaga.wav

# ./vgm2wav.exe ../../tests/nakama.vgm ../../tests/nakama.wav


########################
#
# VGMPlay Makefile
# (for GNU Make 3.81)
#
########################

# TODO: Make this look less horrible.

# (notice that you can just pass these as arguments when running make)

# set to 1 if you build on Windows using MinGW.
ifndef WINDOWS
WINDOWS = 0
endif

# disable Hardware OPL Support [enabled by default]
ifndef DISABLE_HWOPL_SUPPORT
DISABLE_HWOPL_SUPPORT = 1
endif

# set to 1 if you want to use libao instead of OSS for sound streaming under Linux [enabled by default]
# ifndef USE_LIBAO
# USE_LIBAO = 1
# endif

USE_LIBAO = 0

# set to 1 for swprintf fix on older MinGW versions
ifndef OLD_SWPRINTF
OLD_SWPRINTF = 0
endif

# Byte Order
#   0 = undefined (use endian-safe code, might be slightly slower)
#   1 = Little Endian (Intel) [default]
#   2 = Big Endian (Motorola)
# ifndef BYTE_ORDER
# BYTE_ORDER = 1
# endif


#CC = gcc -std=c23


CC = gcc -std=c11
ifndef PREFIX
PREFIX = /usr/local
#PREFIX = $(HOME)/.local
endif
MANPREFIX = $(PREFIX)/share/man

# -- VGMPlay specific Compile Flags --
MAINFLAGS := -DCONSOLE_MODE -DADDITIONAL_FORMATS -DSET_CONSOLE_TITLE
ifeq ($(WINDOWS), 1)
# MinGW defines __WINDOWS__, Visual Studio defines WIN32
MAINFLAGS += -DWIN32
endif
ifeq ($(OLD_SWPRINTF), 1)
MAINFLAGS += -DOLD_SWPRINTF
endif
# ifeq ($(USE_LIBAO), 1)
# MAINFLAGS += -DUSE_LIBAO
# endif
EMUFLAGS := -DENABLE_ALL_CORES

# # -- Byte Order Optimizations --
# ifeq ($(BYTE_ORDER), 1)
# # Intel Byte Order
# MAINFLAGS += -DVGM_LITTLE_ENDIAN
# EMUFLAGS += -DVGM_LITTLE_ENDIAN
# else
# ifeq ($(BYTE_ORDER), 2)
# # Motorola Byte Order
# MAINFLAGS += -DVGM_BIG_ENDIAN
# EMUFLAGS += -DVGM_BIG_ENDIAN
# else
# # undefined byte order
# endif
# endif

ifeq ($(DISABLE_HWOPL_SUPPORT), 1)
MAINFLAGS += -DDISABLE_HW_SUPPORT
endif


# CFLAGS := -g -Wall $(CFLAGS)
CFLAGS := -O3 -g0 -Wno-unused-variable -Wno-unused-value -Wno-unused-but-set-variable $(CFLAGS)


# libm (math library) and libz (zlib)
LDFLAGS := -lm -lz $(LDFLAGS)

ifeq ($(WINDOWS), 1)
# for Windows, add kernel32 and winmm (Multimedia APIs)
LDFLAGS += -lkernel32 -lwinmm
else	# if UNIX
ifeq ($(MACOSX), 1)
# You might want to include additional paths using -I/some/path here,
# in case some libraries (like libao) can't be found.
#CFLAGS += -I/some/path
else
# for Linux, add librt (clock stuff) and libpthread (threads)
LDFLAGS += -lrt -lpthread -pthread

endif
MAINFLAGS += -pthread -DSHARE_PREFIX=\"$(PREFIX)\"
endif

# ifeq ($(USE_LIBAO), 1)
# LDFLAGS += -lao
# endif

# add Library Path, if defined
ifdef LD_LIBRARY_PATH
LDFLAGS += -L $(LD_LIBRARY_PATH)
endif

SRC = .
OBJ = obj
EMUSRC = $(SRC)/chips
EMUOBJ = $(OBJ)/chips


OBJDIRS = \
	$(OBJ) \
	$(EMUOBJ)
MAINOBJS = \
	$(OBJ)/VGMPlay.o \
	$(OBJ)/VGMPlay_AddFmts.o \
	$(OBJ)/ChipMapper.o
ifeq ($(WINDOWS), 1)
ifeq ($(DISABLE_HWOPL_SUPPORT), 0)
MAINOBJS += $(OBJ)/pt_ioctl.o
endif
endif

# libs\sound\vgmplay\VGMPlay\chips\fm.h
# 	$(EMUOBJ)/2610intf.o \

# #define BUILD_YM2610  0


# SN76489_Init
# libs\sound\vgmplay\VGMPlay\chips\sn764intf.c
# 	$(EMUOBJ)/sn76489.o \

# TODO reduce the supported chips
EMUOBJS = \
	$(EMUOBJ)/sn76489.o \
	$(EMUOBJ)/262intf.o \
	$(EMUOBJ)/2151intf.o \
	$(EMUOBJ)/2610intf.o \
	$(EMUOBJ)/2203intf.o \
	$(EMUOBJ)/2413intf.o \
	$(EMUOBJ)/2608intf.o \
	$(EMUOBJ)/2612intf.o \
	$(EMUOBJ)/3526intf.o \
	$(EMUOBJ)/3812intf.o \
	$(EMUOBJ)/8950intf.o \
	$(EMUOBJ)/adlibemu_opl2.o \
	$(EMUOBJ)/adlibemu_opl3.o \
	$(EMUOBJ)/ay8910.o \
	$(EMUOBJ)/ay_intf.o \
	$(EMUOBJ)/c140.o \
	$(EMUOBJ)/c352.o \
	$(EMUOBJ)/c6280.o \
	$(EMUOBJ)/c6280intf.o \
	$(EMUOBJ)/dac_control.o \
	$(EMUOBJ)/es5503.o \
	$(EMUOBJ)/es5506.o \
	$(EMUOBJ)/emu2149.o \
	$(EMUOBJ)/emu2413.o \
	$(EMUOBJ)/fm2612.o \
	$(EMUOBJ)/fm.o \
	$(EMUOBJ)/fmopl.o \
	$(EMUOBJ)/gb.o \
	$(EMUOBJ)/iremga20.o \
	$(EMUOBJ)/k051649.o \
	$(EMUOBJ)/k053260.o \
	$(EMUOBJ)/k054539.o \
	$(EMUOBJ)/multipcm.o \
	$(EMUOBJ)/nes_apu.o \
	$(EMUOBJ)/nes_intf.o \
	$(EMUOBJ)/np_nes_apu.o \
	$(EMUOBJ)/np_nes_dmc.o \
	$(EMUOBJ)/np_nes_fds.o \
	$(EMUOBJ)/okim6258.o \
	$(EMUOBJ)/okim6295.o \
	$(EMUOBJ)/Ootake_PSG.o \
	$(EMUOBJ)/opll.o \
	$(EMUOBJ)/opm.o \
	$(EMUOBJ)/panning.o \
	$(EMUOBJ)/pokey.o \
	$(EMUOBJ)/pwm.o \
	$(EMUOBJ)/qsound_ctr.o \
	$(EMUOBJ)/qsound_mame.o \
	$(EMUOBJ)/qsound_intf.o \
	$(EMUOBJ)/rf5c68.o \
	$(EMUOBJ)/saa1099.o \
	$(EMUOBJ)/segapcm.o \
	$(EMUOBJ)/scd_pcm.o \
	$(EMUOBJ)/scsp.o \
	$(EMUOBJ)/scspdsp.o \
	$(EMUOBJ)/sn76496.o \
	$(EMUOBJ)/sn764intf.o \
	$(EMUOBJ)/upd7759.o \
	$(EMUOBJ)/vsu.o \
	$(EMUOBJ)/ws_audio.o \
	$(EMUOBJ)/x1_010.o \
	$(EMUOBJ)/ym2151.o \
	$(EMUOBJ)/ym2413.o \
	$(EMUOBJ)/ym2612.o \
	$(EMUOBJ)/ym3438.o \
	$(EMUOBJ)/ymdeltat.o \
	$(EMUOBJ)/ymf262.o \
	$(EMUOBJ)/ymf271.o \
	$(EMUOBJ)/ymf278b.o \
	$(EMUOBJ)/ymz280b.o \
	$(EMUOBJ)/ay8910_opl.o \
	$(EMUOBJ)/sn76496_opl.o \
	$(EMUOBJ)/ym2413hd.o \
	$(EMUOBJ)/ym2413_opl.o


VGM2WAV_OBJS = \
	$(OBJ)/vgm2wav.o

all: vgm2wav

vgm2wav:	$(EMUOBJS) $(MAINOBJS) $(VGM2WAV_OBJS)
	@echo Linking vgm2wav ...
	@$(CC) $(VGM2WAV_OBJS) $(MAINOBJS) $(EMUOBJS) $(LDFLAGS) -o vgm2wav
	@echo Done.

# compile the chip-emulator c-files
$(EMUOBJ)/%.o:	$(EMUSRC)/%.c
	@echo Compiling chip-emulator files $< ...
	@mkdir -p $(@D)
	@$(CC) $(CFLAGS) $(EMUFLAGS) -c $< -o $@

# cmake can hopefully simplify this part
# compile the main c-files
$(OBJ)/%.o:	$(SRC)/%.c
	@echo Compiling main $< ...
	@mkdir -p $(@D)
	@$(CC) $(CFLAGS) $(MAINFLAGS) -c $< -o $@