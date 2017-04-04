ft=~/repo/fastText/fasttext

dir=~/data/medium
models_dir=~/models

train=$dir/rare.txt

# permanent settings
minCount=1000
minCountLabel=10
wordNgrams=2
loss=hs
thread=24
label=__rt*

# hyperparams
lr=0.25
dim=300
epoch=20
model=$models_dir/rare20
echo "using train file at ${train}"
# model-specific settings

$ft supervised -input $train -output $model -lr $lr -dim $dim -epoch $epoch -minCount $minCount -minCountLabel $minCountLabel -wordNgrams $wordNgrams -loss $loss -thread $thread -label $label 
