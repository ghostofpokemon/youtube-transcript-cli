Certainly! You can add a badge to your `README.md` file that indicates the package version on PyPI. This can be done using services like shields.io. Here's how you can add a PyPI version badge and an installation command to your `README.md`:

```markdown
# YouTube Transcript CLI

[![PyPI Version](https://img.shields.io/pypi/v/youtube-transcript-cli.svg)](https://pypi.org/project/youtube-transcript-cli/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Welcome to the YouTube Transcript CLI! This tool allows you to fetch and display transcripts of YouTube videos right from your terminal. Whether you're a developer, researcher, or just curious, this tool has got you covered!

## Features

- **Fetch Transcripts**: Get transcripts for any YouTube video.
- **Multiple Languages**: Specify your preferred language for the transcript.
- **Save to File**: Save the transcript to a file for later use.
- **No Print Option**: Fetch transcripts without printing them to the terminal.

## Installation

You can install the YouTube Transcript CLI from PyPI using pip:

```bash
pip install youtube-transcript-cli
```

## Usage

Once installed, you can use the `cap` command to fetch transcripts. Here are some examples:

### Fetch and Print Transcript

```bash
cap https://www.youtube.com/watch?v=Y-KztRvRyl0
```

### Fetch and Save Transcript to a File

```bash
cap https://www.youtube.com/watch?v=Y-KztRvRyl0 --save transcript.txt
```

### Fetch Transcript in a Different Language

```bash
cap https://www.youtube.com/watch?v=Y-KztRvRyl0 --languages es
```

### Fetch Transcript Without Printing to Terminal

```bash
cap https://www.youtube.com/watch?v=Y-KztRvRyl0 --save transcript.txt --no-print
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by [Your Name](https://github.com/ghostofpokemon)
