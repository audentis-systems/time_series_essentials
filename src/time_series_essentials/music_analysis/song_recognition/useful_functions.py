#
# load useful libraries
#
import librosa

#
# Define a function that produces a chromagram for a track for a specific octave
#
def process_octave(y, octave_number, sr = 22050, hop_length = 512 * 200, lowest_pitch = 16.35):  # get a more precise number for C0
    chromagram = librosa.feature.chroma_cens(
        y = y,
        sr = sr,
        fmin = lowest_pitch * (octave_number + 1),
        n_octaves = 1,
        hop_length = hop_length,
    )
    return chromagram
