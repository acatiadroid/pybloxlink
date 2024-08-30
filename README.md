<div align="center">
    <h1>PyBloxlink</h1>
    <h3>An async API wrapper for the <a href="https://blox.link">blox.link</a> API.</h3>
    <img src="https://img.shields.io/pypi/v/pybloxlink.svg">
</div>

## Useful links
* [API Reference](https://acatiadroid.github.io/pybloxlink/api.html)
* [PyPI Page](https://pypi.org/project/pybloxlink/)
* [Examples](https://acatiadroid.github.io/pybloxlink/examples.html)

## About
PyBloxlink is an async API wrapper for the [Bloxlink](https://blox.link) API.

Notable features:
* Async ready.
* Up to date.
* Provides full API coverage.
* User-friendly errors for handling status codes of failed HTTP requests.

## Installation
To install a full release of the library, run the command below:

```
pip install -U pybloxlink
```

## Don't forget...
It is important that you close the client session once you are done with using PyBloxlink. If you do not, you're likely going to get `Unclosed conntor`/`Unclosed client session` errors.

This is to ensure there are no pending tasks awaiting completion.

Closing the client is as simple as using `Bloxlink.close` (coro).

## Examples
Some examples can be found here: https://acatiadroid.github.io/pybloxlink/examples.html

## Help
If you need help, you can either make an [issue](https://github.com/acatiadroid/pybloxlink/issues/new) or join the Bloxlink server: https://discord.gg/bloxlink

## License
This is licensed under MIT. Read the license [here](https://github.com/acatiadroid/pybloxlink/blob/main/LICENSE.txt).

## Contributing
Contributions are welcome! Check out the [contributing guidelines](https://github.com/acatiadroid/pybloxlink/blob/main/.github/CONTRIBUTING.md) beforehand.
