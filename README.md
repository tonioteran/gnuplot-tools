# gnuplot tools

The idea is to create generalized scripts for people to freely reuse in their projects.

## Python parsing tools:

Modify original ``.dat`` files to include frame of reference info for gnuplot to plot them.

## Uncertainty ellipsoids:

Take in the eigenvalues of the covariance matrix, and plot a 3d ellipsoid denoting the uncertainty of a position state.

## Frames of reference:

Explain input/output. Idea: take in quats, convert into rot matrices, and transform endopoints of unit vectors. Use python to translate them to their corresponding coordinate, and append them to a ``.dat`` file.


