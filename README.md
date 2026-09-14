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
      - name: Build
        run: |
          pip install --upgrade pip
          pip install buildozer Cython==0.29.36
          buildozer init
          sed -i 's/#p4.fork = 0/p4.fork = auto/' buildozer.spec
          buildozer -v android debug
      - uses: actions/upload-artifact@v3
        with:
          name: apk
          path: bin/*.apk
