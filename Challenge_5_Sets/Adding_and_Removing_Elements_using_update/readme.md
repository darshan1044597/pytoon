# Challenge 6: Adding and Removing Elements (Using Update and Discard)

## Concept
Using `.update()` and `.discard()` for bulk modifications
## Objective
Modify a set efficiently
## What you need to do:
- Create a set called `letters` with the items `'a'`, `'b'`, and `'c'`.
- Add the letters `'d'`, `'e'`, and `'f'` using `.update()`.
- Remove the letter `'b'` using `.discard()` (this won’t cause an error if `'b'` is not in the set).
- Print the updated set.

### Example Code:

```python
# Create a set with letters
letters = {'a', 'b', 'c'}
# Add multiple letters at once using the update() method
letters.update({'d', 'e', 'f'})
# Remove the letter 'b' using discard() 
letters.discard('b')
# Print the updated set
print(letters)
