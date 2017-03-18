# medium-upvote-prediction

/utils for storing preprocessing and extraction stuff

/models for training scripts

/analysis for visualizations

### Primary considerations for models:

We prepare one script with fixed state (for reproducibility) for splitting the dataset into train and test samples.

Models are dir-based, every directory contains at least all necessary descriptions for reproducing related results.

### List of experiments (global):
	1. Fully supervised tag prediction
	2. Weakly supervised tag prediction
	3. Virality prediction (range of likes)
	4. Synthetic labeling and reweighting for task-specific document representations
