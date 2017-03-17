src_dir=$1

min_freq_labels=$2
n_labels=$3

#echo "Performing train/test split"
#python train_test_split.py ${src_dir}/medium.json ${src_dir}/train.json ${src_dir}/test.json ${src_dir}/index

echo "Generating training dataset for fasttext"
python rare_words.py ${src_dir}/train.txt ${min_freq_labels} ${n_labels} > ${src_dir}/weak_train.txt

echo "Generating validation dataset for fasttext"
python rare_words.py ${src_dir}/test.txt ${min_freq_labels} ${n_labels} > ${src_dir}/weak_test.txt
