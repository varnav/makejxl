#!/bin/bash -ex

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

if [ $(grep -c avx2 /proc/cpuinfo) == 0 ]
  then echo "AVX2 support required"
  exit
fi
set -ex

export RUSTFLAGS="-C target-feature=+avx2,+fma"
export CFLAGS="-mavx2 -mfma -ftree-vectorize -pipe"
export MAKEFLAGS=-j$(nproc --ignore=2)
export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get -y install python3-pip git wget ca-certificates cmake pkg-config libbrotli-dev libgif-dev libjpeg-dev libopenexr-dev libpng-dev libwebp-dev clang

cd /tmp/
rm -rf libjxl
git clone https://github.com/libjxl/libjxl.git --recursive
cd libjxl
rm -rf build
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF ..
cmake --build . -- -j$(nproc --ignore=2)

cp tools/cjxl /usr/bin/
