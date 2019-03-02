# Helper scripts

Edit environment.sh to change branch/tag names.

Create branch:

```
dev/branch_name  # optional, preview the branch name
python3 dev/branch.py
```

Create tag:

```
dev/tag_name  # optional, preview the tag name
dev/tag_message  # optional, preview the tag message
python3 dev/tag.py
```

Test build:

```
dev/test_build
```

Check style:

```
python3 -m pip install -r dev/requirements_dev.txt # once
python3 dev/check_style.py
```
