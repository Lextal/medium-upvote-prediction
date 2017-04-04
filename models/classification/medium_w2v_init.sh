ft=~/repo/fastText/fasttext

wd=~/data/medium/weak
test=~/data/medium/test.txt

model_dir=~/models

vecs=~/models/pretrained/w2v_medium.vec

model=${model_dir}/medium_init_001
$ft supervised -input ${wd}/train_001.txt -output ${model} -lr 0.1 -dim 300 -loss hs -epoch 200 -minCount 100 -minCountLabel 1 -thread 24 -label __rt* -pretrainedVectors $vecs
echo "test on 0.01%"
$ft test ${model}.bin $test 2

# =========
model=${model_dir}/medium_init_005
$ft supervised -input ${wd}/train_005.txt -output ${model} -lr 0.1 -dim 300 -loss hs -epoch 200 -minCount 100 -minCountLabel 1 -thread 24 -label __rt* -pretrainedVectors $vecs
echo "test on 0.05%"
$ft test ${model}.bin $test 2

# =========
model=${model_dir}/medium_init_01
$ft supervised -input ${wd}/train_01.txt -output ${model} -lr 0.1 -dim 300 -loss hs -epoch 200 -minCount 100 -minCountLabel 1 -thread 24 -label __rt* -pretrainedVectors $vecs
echo "test on 0.1%"
$ft test ${model}.bin $test 2

# =========
model=${model_dir}/medium_init_05
$ft supervised -input ${wd}/train_05.txt -output ${model} -lr 0.1 -dim 300 -loss hs -epoch 200 -minCount 100 -minCountLabel 1 -thread 24 -label __rt* -pretrainedVectors $vecs
echo "test on 0.5%"
$ft test ${model}.bin $test 2

# =========
model=${model_dir}/medium_init_1
$ft supervised -input ${wd}/train_1.txt -output ${model} -lr 0.1 -dim 300 -loss hs -epoch 200 -minCount 100 -minCountLabel 1 -thread 24 -label __rt* -pretrainedVectors $vecs
echo "test on 1%"
$ft test ${model}.bin $test 2

# =========

