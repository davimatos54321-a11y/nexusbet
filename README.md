name: App
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.10"
      - run: |
          sudo apt update
          sudo apt install -y openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
          pip install --upgrade pip
          pip install buildozer Cython==0.29.36
          buildozer init
          sed -i 's/#p4.fork = 0/p4.fork = auto/' buildozer.spec
          sed -i 's/requirements = python3,kivy/requirements = python3,kivy,math,datetime/' buildozer.spec
          buildozer -v android debug
      - uses: actions/upload-artifact@v3
        with:
          name: apk
          path: bin/*.apk
