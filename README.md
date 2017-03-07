# medium-upvote-prediction

/utils for storing preprocessing and extraction stuff

/models for training scripts

/analysis for visualizations

Primary considerations for models:

We prepare one script with fixed state (for reproducibility) for splitting the dataset into train and test samples.

Models are dir-based, every directory contains at least all necessary descriptions for reproducing related results.

Let's make everything independent from actual datasets (if possible), because this experiment is going to be amazing for a variety of well-known datasets. If anything we are going to try here works, it will be enough for publication. 
