
import main


# CRITICAL: You are using the SDL disk i/o audio driver!
# CRITICAL:  Writing to file [sdlaudio.raw].
    #   - name: Install ALSA utilities
    #     # run: sudo apt-get update && sudo apt-get install -y alsa-utils
    #     run: sudo apt-get install -y alsa-utils

    # Using a dummy device for github actions ^^
def test_main():
    main.main(500)
    # import main