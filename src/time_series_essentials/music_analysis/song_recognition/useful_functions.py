#
# load useful libraries
#
import librosa

#
# Define a function that produces a chromagram for a track for a specific octave
#
# By performing this analysis one octave at a time and then
# appending the results together (in a downstream functino),
# we obtain a chromagram vector that covers every note on the
# piano seperately per time step.
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
