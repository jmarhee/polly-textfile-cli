# AWS Polly Textfile CLI

This package takes a filepath, breaks it into < 250 character sentences for text-to-speech processing by AWS Polly, and then locally, merges the chunks back into a single mp3 file.

## Requirements

This requires an [AWS account](https://aws.amazon.com). You will need to set the following environmental variables:

```
AWS_DEFAULT_REGION=us-east-2
AWS_SECRET_ACCESS_KEY=${YOUR_SECRET_KEY}
AWS_ACCESS_KEY_ID=${YOUR_ACCESS_KEY}
```

or if you have `awscli` installed, run `aws configure` to provide these details to generate a config file.

You will also need `ffmpeg` [installed on your machine](https://ffmpeg.org/download.html). 

## Installation

Install from PyPi:

```bash
pip3 install polly-textfile-cli
```

or from this repo:

```bash
pip3 install git+https://github.com/jmarhee/polly-textreader-cli.git
```

or clone and install, if developing with this package:

```bash
git clone https://github/jmarhee/polly-textreader-cli.git
cd polly-textreader-cli
pip3 install -e .
```

then test that the `polly-textfile` package is available in your `PATH`:

```bash
which polly-textfile
```

and proceed.

## Usage

Run the following command:

```bash
polly-textfile --path your-text-file.txt --name output-name-no-extension
```

Upon completion, you'll have the component files (`your-output-name-part-$i.mp3`) and the concatenated audio file (`your-output-name.mp3`). 
