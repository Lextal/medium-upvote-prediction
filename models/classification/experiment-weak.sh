lr=0.1
dim=50
epoch=10

test_path=~/data/medium/test.txt
k=2
train=$1
log_file=$2

lr=0.1
dim=300
epoch=200

./train.sh $lr $dim $epoch $train 
model_path=~/models/weak_dim_${dim}_lr_${lr}_epoch_${epoch}.bin
output=$(./test.sh $model_path $test_path $k)
echo "dim=${dim},lr=${lr},epoch=${epoch},train=${train}" >> $log_file
echo "${output}" >> $log_file
echo "experiment on lr=${lr} finished"
