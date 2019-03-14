# dexif - Delete EXIF information script

## how to use

1. `git clone git@github.com:hamadatakaki/dexif.git`
2. `cd dexif`
3. `mkdir images`
4. `mv` the images directory to `images`
5. `pipenv install`
6. `pipenv run python run.py`

## how to mv filter by prefix 'dst\_'

```
$ ls | grep -E "^dst_" | awk '{print $1 " ../dst"}' | xargs -n 2 mv
```
