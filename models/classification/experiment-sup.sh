lr=0.1
dim=50
epoch=10

test_path=~/data/medium/test.txt
k=2

log_file=$1

lr=0.25
dim=300
epoch=10

./train.sh $lr $dim $epoch 
model_path=~/models/sup_dim_${dim}_lr_${lr}_epoch_${epoch}.bin
output=$(./test.sh $model_path $test_path $k)
echo "dim=${dim},lr=${lr},epoch=${epoch}" >> $log_file
echo "${output}" >> $log_file
echo "experiment on lr=${lr} finished"
