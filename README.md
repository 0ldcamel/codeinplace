<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="[https://github.com/github_username/repo_name](https://github.com/0ldcamel/codeinplace)">
    <img src="images/CiP2024.png" alt="Logo" width="583" height="80"></a>
</div>

# Attending Stanford's Code In Place 2024

## Using graphics module in VS Code:
[Using the graphics module in VS Code](https://codeinplace.stanford.edu/cip4/forum?post=ad0f48a5-9e07-41bc-a228-6076b676de98) is an excellence answer by Micheal C.

`canvas.get_new_key_presses()` actually returns a list of key presses, not just a single keypress.  And the elements of that list aren't strings -- they're KeyPress objects, which have a `.keysym` member containing the key name.  Here's an example of how to get the actual key names for each keypress:

```
for key in canvas.get_new_key_presses():
    print(key.keysym)
```

## Second level heading 2
