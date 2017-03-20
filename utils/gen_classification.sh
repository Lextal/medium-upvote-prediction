src_dir=$1

echo "Performing train/test split"
python train_test_split.py ${src_dir}/medium.json ${src_dir}/train.json ${src_dir}/test.json ${src_dir}/index

echo "Generating training dataset for fasttext"
python data_loader.py ${src_dir}/train.json > ${src_dir}/train.txt

echo "Generating validation dataset for fasttext"
python data_loader.py ${src_dir}/test.json > ${src_dir}/test.txt
