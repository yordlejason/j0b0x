# Instruction

### 1. Install the dependencies 

#### `pip install -r requirements.txt`



### 2. Run 

#### `python3 -i run.py`



### 3. Pass in the arguments to 

#### `solver(:n, :grid)` 



If you want to take a look at the words found from the grid, you can instantiate the Solver and call `get_words()` method. Here is the example:



```python
>>> from Solver import Solver
>>> solver = Solver(n, grid)
>>> solver.get_words(:n, :grid)

```

