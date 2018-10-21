Hair Color Detect
====

This script checks whether anime/manga images have white hair characters.

The detection logic use [lbpcascade_animeface](https://github.com/nagadomi/lbpcascade_animeface).

## Task List

- [x] Execute code.
- [ ] Translate comment from Japanese to English.
- [ ] Adding a file extension other than jpg.
- [ ] Adding Test Code.

## Requirement
opencv

## Usage
1. Please put on images in images/ directory.
2. Please execute the following command.

```
$ python cli.py ./images/
```

## Install

```
$ git clone https://github.com/pesuchin/haircolor_detect.git
$ python setup.py install
```

## Contribution
Coding rule is flake8 in this repogitory.

1. Fork this repository.
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[pesuchin](https://github.com/pesuchin)