# Usage

`my_package` is a folder in which you have your python code. This folder contains a `__init__.py` file which actually makes it **importable** - just like a package.

For example, if you want to use `my_package` into your code, you can do the following

```python
import my_package

my_package.console('a console message!')
```

Currently, this is do-able, if the above piece of code is written in a file which is able to reference the `my_package` folder directly. Means to say, if the above piece of code is
written in file called `useme.py` and is located right outside the `my_package` folder, then the above code will work fine.

But, like all other python package, if you want to globally install your package and use
it from anywhere in the system, then _this_ is where your python packages are saved


```sh
# path for python3.6 packages in ubuntu
/home/vivek/anaconda3/lib/python3.6/site-packages/
```

So, if you copy the `my_package` folder into the above directory, then you can **import**
the package from anywhere in your system, within your python code.

**NOTE**: You can see any package's source code from within the `site-packages` folder