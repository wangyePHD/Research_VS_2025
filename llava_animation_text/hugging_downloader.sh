model_name=$1
export HF_ENDPOINT=https://hf-mirror.com




# Download the model
huggingface-cli download --token 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  --resume-download $model_name --local-dir ./checkpoints/$model_name --local-dir-use-symlinks False

