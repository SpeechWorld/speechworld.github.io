
# find audios | grep ours | while read line;do
# 	renamed=`echo $line | sed 's/ours/official/g'`
# 	cp $line $renamed
# done

# find audios | grep ours | while read line;do
# 	rm $line
# done

# pip install -U openai-whisper

cd /home/feiteng/Geek/OpenSource/speech/valle/egs/ljspeech
ln -s ~/Geek/OpenSource/speech/lifeiteng.github.com/valle/audios

# for prefix_mode in `seq 1 2`;do
for prefix_mode in `seq 1 1`;do
      exp_dir=expX8/valle_Dim256H8L6_LR05_PrefixMode${prefix_mode}V2

      # python3 bin/trainer.py --max-duration 72 --filter-max-duration 14 \
      #       --num-buckets 6 --dtype "float32" --save-every-n 10000 \
      #       --model-name valle --norm-first true --add-prenet false \
      #       --decoder-dim 256 --nhead 8 --num-decoder-layers 6 --prefix-mode ${prefix_mode} \
      #       --base-lr 0.05 --warmup-steps 200 \
      #       --num-epochs 120 --start-epoch 1 --start-batch 0 --accumulate-grad-steps 1 \
      #       --exp-dir ${exp_dir}

      python3 bin/infer.py --output-dir demos \
          --top-k -1 --temperature 1.0 \
          --model-name valle --norm-first true --add-prenet false \
          --decoder-dim 256 --nhead 8 --num-decoder-layers 6 --prefix-mode ${prefix_mode} \
          --text-prompts "" \
          --audio-prompts "" \
          --text ~/Geek/OpenSource/speech/lifeiteng.github.com/valle/ljspeech.txt \
          --checkpoint ${exp_dir}/epoch-120.pt
done



cd /home/feiteng/Geek/OpenSource/speech/valle/egs/libritts
ln -s ~/Geek/OpenSource/speech/lifeiteng.github.com/valle/audios

# for prefix_mode in `seq 1 2`;do
for prefix_mode in `seq 1 1`;do
    # exp_dir=expX8/valle_Dim512H8L6_LR05_PrefixMode${prefix_mode}V2FixLen
    # mkdir -p ${exp_dir}
    # cp expX8/valle_Dim512H8L6_LR05/checkpoint-1050000.pt ${exp_dir}

    # python3 bin/trainer.py --max-duration 48 --filter-max-duration 14 \
    #       --num-buckets 6 --dtype "float32" --save-every-n 5000 \
    #       --model-name valle --norm-first true --add-prenet false \
    #       --decoder-dim 512 --nhead 8 --num-decoder-layers 6 --prefix-mode ${prefix_mode} \
    #       --base-lr 0.05 --warmup-steps 200 \
    #       --num-epochs 25 --start-epoch 1 --start-batch 1050000 --accumulate-grad-steps 1 \
    #       --exp-dir ${exp_dir}

    # python3 bin/infer.py --output-dir demos \
    #     --top-k -1 --temperature 1.0 \
    #     --model-name valle --norm-first true --add-prenet false \
    #     --decoder-dim 512 --nhead 8 --num-decoder-layers 6 --prefix-mode ${prefix_mode} \
    #     --text-prompts "" \
    #     --audio-prompts "" \
    #     --text ~/Geek/OpenSource/speech/lifeiteng.github.com/valle/libritts.txt \
    #     --checkpoint ${exp_dir}/checkpoint-1070000.pt

    exp_dir=exp_0331/valle_Prefix1_Dim1024H16L12_ShareEmb_BF16_BestValid

    python3 bin/infer.py --output-dir demos \
          --top-k -1 --temperature 1.0 \
          --model-name valle --share-embedding true --norm-first true --add-prenet false \
          --decoder-dim 1024 --nhead 16 --num-decoder-layers 12 --prefix-mode 1 \
          --text-prompts "" \
          --audio-prompts "" \
          --text ~/Geek/OpenSource/speech/lifeiteng.github.com/valle/libritts.txt \
          --checkpoint ${exp_dir}/best-valid-loss.pt
done
