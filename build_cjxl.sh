#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

if [ $(grep -c avx2 /proc/cpuinfo) == 0 ]
  then echo "AVX2 support required"
  exit
fi

set -ex


export DEBIAN_FRONTEND=noninteractive

export RUSTFLAGS="-C target-feature=+avx2,+fma"
export CFLAGS="-mavx2 -mfma -ftree-vectorize -pipe"

export CC=clang-7 CXX=clang++-7

apt-get update
apt-get -y install git wget ca-certificates cmake pkg-config libbrotli-dev libgif-dev libjpeg-dev libopenexr-dev libpng-dev libwebp-dev clang-7

cd /tmp/
rm -rf jpeg-xl
git clone  --recursive --depth=1 https://gitlab.com/wg1/jpeg-xl.git
cd jpeg-xl
rm -rf build
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF ..
cmake --build . -- -j$(nproc)

cp tools/cjxl /usr/bin/