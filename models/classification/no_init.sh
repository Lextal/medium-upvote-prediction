ft=~/repo/fastText/fasttext

wd=~/data/medium/weak
test=~/data/medium/test.txt

model_dir=~/models

vecs=~/models/rare50.vec

mc=10

model=${model_dir}/no_init_001
$ft supervised -input ${wd}/train_001.txt -output ${model} -lr 0.1 -dim 300 -loss hs -epoch 200 -minCount $mc -minCountLabel 1 -thread 24 -label __rt* 
echo "test on 0.01%"
$ft test ${model}.bin $test 2

# =========
model=${model_dir}/no_init_005
$ft supervised -input ${wd}/train_005.txt -output ${model} -lr 0.1 -dim 300 -loss hs -epoch 200 -minCount $mc -minCountLabel 1 -thread 24 -label __rt*
echo "test on 0.05%"
$ft test ${model}.bin $test 2

# =========
model=${model_dir}/no_init_01
$ft supervised -input ${wd}/train_01.txt -output ${model} -lr 0.1 -dim 300 -loss hs -epoch 200 -minCount $mc -minCountLabel 1 -thread 24 -label __rt*
echo "test on 0.1%"
$ft test ${model}.bin $test 2

# =========
model=${model_dir}/no_init_05
$ft supervised -input ${wd}/train_05.txt -output ${model} -lr 0.1 -dim 300 -loss hs -epoch 200 -minCount $mc -minCountLabel 1 -thread 24 -label __rt* 
echo "test on 0.5%"
$ft test ${model}.bin $test 2

# =========
model=${model_dir}/no_init_1
$ft supervised -input ${wd}/train_1.txt -output ${model} -lr 0.1 -dim 300 -loss hs -epoch 200 -minCount $mc -minCountLabel 1 -thread 24 -label __rt* 
echo "test on 1%"
$ft test ${model}.bin $test 2

# =========

