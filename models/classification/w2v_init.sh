ft=~/repo/fastText/fasttext

wd=~/data/medium/weak
test=~/data/medium/test.txt

model_dir=~/models

model=${model_dir}/w2v_init_1
$ft supervised -input ${wd}/train_1.txt -output ${model} -lr 0.1 -dim 300 -loss hs -epoch 200 -minCount 100 -minCountLabel 1 -thread 24 -label __rt* -pretrainedVectors ~/models/pretrained/w2v_medium.vec
echo "test on 1%"
$ft test ${model}.bin $test 2

# =========
model=${model_dir}/w2v_init_5
$ft supervised -input ${wd}/train_5.txt -output ${model} -lr 0.1 -dim 300 -loss hs -epoch 200 -minCount 100 -minCountLabel 1 -thread 24 -label __rt* -pretrainedVectors ~/models/pretrained/w2v_medium.vec
echo "test on 5%"
$ft test ${model}.bin $test 2

# =========
model=${model_dir}/w2v_init_10
$ft supervised -input ${wd}/train_10.txt -output ${model} -lr 0.1 -dim 300 -loss hs -epoch 200 -minCount 100 -minCountLabel 1 -thread 24 -label __rt* -pretrainedVectors ~/models/pretrained/w2v_medium.vec
echo "test on 10%"
$ft test ${model}.bin $test 2

