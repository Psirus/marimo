# Run as a script

You can run marimo notebooks as scripts at the command line, just like
any other Python script. For example,

```bash
python my_marimo_notebook.py
```

Running a notebook as a script is useful when your notebook has side-effects,
like writing to disk. Print statements and other console outputs will show
up in your terminal.


!!! note "Saving notebook outputs"

    To run as a script while also saving HTML of the notebook outputs, use

    ```bash
    marimo export html notebook.py -o notebook.html
    ```

    You can also pass command-line arguments to your notebook during export.
    Separate these args from the command with two dashes:

    ```bash
    marimo export html notebook.py -o notebook.html -- -arg value
    ```

    Exporting to other formats, such as ipynb, is also possible:

    ```bash
    marimo export ipynb notebook.py -o notebook.ipynb -- -arg value
    ```

## Command-line arguments

When run as a script, you can access your notebook's command-line arguments
through `sys.argv`, just like any other Python program. This also
means you can declare your notebook's command-line arguments using Python
libraries like [`argparse`](https://docs.python.org/3/library/argparse.html)
and [`simple-parsing`](https://github.com/lebrice/SimpleParsing).

These examples shows how to conditionally assign values to variables based on
command-line arguments when running as a script, and use default values when
running as a notebook.

### argparse

/// marimo-embed-file
    filepath: examples/running_as_a_script/with_argparse.py
///

### simple-parsing

/// marimo-embed-file
    filepath: examples/running_as_a_script/with_simple_parsing.py
///
