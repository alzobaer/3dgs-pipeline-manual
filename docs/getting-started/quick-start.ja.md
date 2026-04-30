# クイックスタート

30分で3DGSパイプラインを動作させましょう。

---

## 前提条件

開始前に以下を確認してください：

- **OS：** Ubuntu 22.04 LTS以降
- **GPU：** CUDAに対応したNVIDIA GPU（RTX 6000 Ada または同等品を推奨）
- **ストレージ：** 空き容量100GB以上
- **メモリ：** RAM 32GB以上（64GB以上を推奨）
- **インターネット接続：** 依存パッケージのダウンロード用

---

## Step 1：CUDAのインストール（5分）

本パイプラインにはCUDA 12.4が必要です。

```bash
# CUDA 12.4のダウンロードとインストール
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-4

# インストールの確認
nvcc --version
nvidia-smi
```

**期待される出力：** CUDA 12.4とGPU情報が表示される

---

## Step 2：COLMAPのインストール（5分）

COLMAPはStructure-from-Motion（SfM）による三次元復元に使用します。

```bash
# 依存パッケージのインストール
sudo apt-get update
sudo apt-get install -y \
    git \
    cmake \
    build-essential \
    libboost-all-dev \
    libeigen3-dev \
    libsuitesparse-dev \
    libfreeimage-dev \
    libgoogle-glog-dev \
    libgflags-dev \
    libglew-dev \
    qtbase5-dev \
    libqt5opengl5-dev

# COLMAPのクローンとビルド
git clone https://github.com/colmap/colmap.git
cd colmap
mkdir build
cd build
cmake .. -DCMAKE_CUDA_ARCHITECTURES=native
make -j$(nproc)
sudo make install

# インストールの確認
colmap -h
```

**期待される出力：** COLMAPのヘルプメッセージが表示される

---

## Step 3：3D Gaussian Splattingのインストール（10分）

3DGSリポジトリをクローンしてセットアップします。

```bash
# リポジトリのクローン
git clone https://github.com/graphdeco-inria/gaussian-splatting.git
cd gaussian-splatting

# conda環境の作成
conda create -n 3dgs python=3.10 -y
conda activate 3dgs

# CUDA 12.4対応のPyTorchをインストール
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124

# 依存パッケージのインストール（cstdintエラーの修正付き）
pip install -r requirements.txt --no-build-isolation

# サブモジュールのビルド
pip install submodules/diff-gaussian-rasterization --no-build-isolation
pip install submodules/simple-knn --no-build-isolation

# インストールの確認
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA利用可能: {torch.cuda.is_available()}')"
```

**期待される出力：**
```
PyTorch: 2.x.x+cu124
CUDA利用可能: True
```

---

## Step 4：FFmpegのインストール（2分）

FFmpegは動画からフレームを抽出するために必要です。

```bash
sudo apt-get install -y ffmpeg

# インストールの確認
ffmpeg -version
```

---

## Step 5：サンプルデータでテスト（5分）

すべてが正しく動作するかテストします。

### テスト動画のダウンロード

```bash
# テストディレクトリの作成
mkdir -p ~/3dgs-test
cd ~/3dgs-test

# テスト動画がある場合はここに配置
# ない場合は次のステップでテストデータを作成
```

### フレームの抽出

```bash
# 5fpsでフレームを抽出
ffmpeg -i your_video.mp4 -vf "fps=5" -qscale:v 2 frames/frame_%04d.jpg

# 抽出されたフレーム数を確認
ls frames/ | wc -l
# 60秒の動画の場合、約329フレームが表示されるはず
```

### COLMAPの実行

```bash
# 出力ディレクトリの作成
mkdir -p colmap_output

# COLMAPの特徴点抽出
colmap feature_extractor \
    --database_path colmap_output/database.db \
    --image_path frames/ \
    --ImageReader.single_camera 1 \
    --ImageReader.camera_model PINHOLE \
    --SiftExtraction.use_gpu 1

# COLMAPの完全マッチング
colmap exhaustive_matcher \
    --database_path colmap_output/database.db \
    --SiftMatching.use_gpu 1

# COLMAPのマッパー実行
mkdir -p colmap_output/sparse
colmap mapper \
    --database_path colmap_output/database.db \
    --image_path frames/ \
    --output_path colmap_output/sparse \
    --Mapper.ba_global_max_num_iterations 20 \
    --Mapper.max_num_models 1
```

### 3DGS学習の実行

```bash
# conda環境の有効化
conda activate 3dgs

# メモリ設定
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

# 学習の実行
cd ~/gaussian-splatting
python train.py \
    -s ~/3dgs-test \
    -m ~/3dgs-test/output \
    --iterations 30000

# 学習には約18〜30分かかります
```

### 結果の確認

```bash
# 出力を確認
ls ~/3dgs-test/output/point_cloud/iteration_30000/

# point_cloud.ply が存在するはず
```

---

## 期待される結果

以下のステップが完了していれば成功です：

✅ CUDA 12.4がインストールされ動作している  
✅ COLMAPがインストールされ機能している  
✅ 3DGS環境がセットアップされている  
✅ FFmpegがフレーム抽出に対応している  
✅ テスト用三次元復元が完了している  

**品質指標（本研究のデータセット）：**
- PSNR：約23.80 dB（良好）
- 学習時間：約18〜30分
- ファイルサイズ：約200 MB（点群）

---

## よくある問題

### 問題1：CUDAバージョンの不一致

**症状：** PyTorchが異なるCUDAバージョンを表示する

**解決策：**
```bash
pip uninstall torch torchvision
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
```

### 問題2：COLMAPのセグメンテーションフォルト

**症状：** マッパー実行中にCOLMAPがクラッシュする

**解決策：**
```bash
# バンドル調整のイテレーションを制限
--Mapper.ba_global_max_num_iterations 20
--Mapper.max_num_models 1
```

### 問題3：メモリ不足（OOM）

**症状：** GPUのメモリが不足する

**解決策：**
```bash
# フレームレートを下げる（フレーム数を減らす）
ffmpeg -i video.mp4 -vf "fps=3" ...  # 5fpsの代わりに3fps

# または解像度を下げる
ffmpeg -i video.mp4 -vf "fps=5,scale=1920:1080" ...  # 4Kの代わりに1080p
```

### 問題4：モジュールが見つからないエラー

**症状：** Pythonがサブモジュールを見つけられない

**解決策：**
```bash
# --no-build-isolation フラグを使用
pip install submodules/diff-gaussian-rasterization --no-build-isolation
pip install submodules/simple-knn --no-build-isolation
```

---

## 次のステップ

環境のセットアップが完了したら：

1. **[独自データの処理](../data-prep/video-requirements.md)** - 動画の撮影と準備
2. **[完全なパイプラインの実行](../pipeline/overview.md)** - 全ワークフローの実行
3. **[研究内容の確認](../my-research/contributions.md)** - 結果と手法の確認
4. **[トラブルシューティング](../troubleshooting/common-issues.md)** - よくある問題の解決

---

## 確認チェックリスト

完全なパイプラインに進む前に：

- [ ] CUDA 12.4がインストール済み（`nvcc --version`）
- [ ] GPUが認識されている（`nvidia-smi`）
- [ ] COLMAPが動作している（`colmap -h`）
- [ ] conda環境が作成済み（`conda activate 3dgs`）
- [ ] CUDAありのPyTorchが動作（`python -c "import torch; print(torch.cuda.is_available())"`）
- [ ] FFmpegがインストール済み（`ffmpeg -version`）
- [ ] テスト用三次元復元が完了
- [ ] 点群が生成されている

---

**所要時間：** 合計30分  
**難易度：** 中級  
**前提知識：** 基本的なLinuxコマンドライン操作

---

*困ったときは[トラブルシューティングガイド](../troubleshooting/common-issues.md)を確認するか、研究室へ連絡してください。*
