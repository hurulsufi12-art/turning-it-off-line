# Have You Tried Turning It Off?

[![make.fun](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/hurulsufi12-art/turning-it-off-line/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/hurulsufi12-art/turning-it-off-line/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)

Entry for the make.fun bounty [Have You Tried Turning It Off?](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b) — one funny line a hopeless tech support agent says to a desperate customer.

## The line

> The system is down, but don't worry. I turned my headset off and on again, and I feel brand new.

96 characters, pure ASCII, one line. The agent applies the sacred reboot ritual to his own headset instead of the system — cheerful uselessness, customer never the butt of the joke.

## How it works

`main.py` is a stdlib-only copier: it writes the locked line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT` when set) as UTF-8 with no trailing newline, and validates the 1–199 character gate before writing.

```sh
python3 main.py
```

## Tests

```sh
python3 -m unittest discover -s tests -v
```

12 tests, all passing. The tests live outside this entry directory (in the bounty workspace, `tests/`), so they are not part of the submitted repo.

## License

MIT — see [LICENSE](LICENSE).
