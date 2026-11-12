# CMPE101 - Practice Set 1

Day 11 of my Python practice: loops, digits, lists, functions, and matrices.

[Open or download the original question PDF](CMPE101_Practice_Set1.pdf)

The PDF contains 15 exercises. The 13 supplied solutions are saved using their original question numbers and descriptive filenames. Q11 and Q14 have no supplied solution. The implementations are preserved, with spacing normalized; known limitations are listed below.

## Questions and solutions

| Question | Exercise | What it asks | Solution |
| --- | --- | --- | --- |
| 1 | A Number Sequence | Print `-3 11 25 39 53 67 81` on one line. | [q1_number_sequence.py](q1_number_sequence.py) |
| 2 | Zero the Negatives | Replace negative entries with zero in the received list; return nothing. | [q2_zero_negatives.py](q2_zero_negatives.py) |
| 3 | Sum of Odd Numbers | Read a positive integer N and sum the odd numbers from 1 through N. | [q3_sum_of_odd_numbers.py](q3_sum_of_odd_numbers.py) |
| 4 | Fixed Points | Count indices i where `numbers[i] == i`. | [q4_fixed_points.py](q4_fixed_points.py) |
| 5 | Digits to a Number | Read N digits and combine them using only +, *, and %; no strings or exponentiation. | [q5_digits_to_a_number.py](q5_digits_to_a_number.py) |
| 6 | Running Sum | Return a new list of cumulative sums. | [q6_running_sum.py](q6_running_sum.py) |
| 7 | Sum of Two Squares | Print every ordered pair of positive integers whose squares sum to N, or 0 if none exist. | [q7_sum_of_two_squares.py](q7_sum_of_two_squares.py) |
| 8 | Remove Consecutive Duplicates | Return a new list with one element per run of equal neighbours. | [q8_remove_consecutive_duplicates.py](q8_remove_consecutive_duplicates.py) |
| 9 | Rotate Right | Return a new list rotated right by k places, including k larger than the list length. | [q9_rotate_right.py](q9_rotate_right.py) |
| 10 | Min and Max So Far | Return the running minimum and maximum lists without min() or max(). | [q10_running_min_max.py](q10_running_min_max.py) |
| 11 | IKI + IKI = DORT | Find digit assignments with distinct digits for different letters and nonzero I and D. | Not supplied |
| 12 | Merge Two Sorted Lists | Merge two sorted lists without sort(), sorted(), or extend(). | [q12_merge_sorted_lists.py](q12_merge_sorted_lists.py) |
| 13 | Product of the Others | Return the product of all other elements for each position, without division. | [q13_product_except_self.py](q13_product_except_self.py) |
| 14 | Last One at the Table | Return the removal order when every K-th person leaves a circular table of N people. | Not supplied |
| 15 | Matrix Tools | Transpose a matrix without zip and sum both diagonals of a square matrix, counting its centre once. | [q15_matrix_tools.py](q15_matrix_tools.py) |

## Run a solution

Python 3 is the only requirement. From the repository root, run, for example:

```sh
python Day-11-CMPE101-Example-Homeworks/q1_number_sequence.py
```

On Windows, `py` can be used instead of `python`. Q3, Q5, and Q7 request keyboard input. Other scripts print their included examples. Q5 first asks for the digit count, then accepts one digit per prompt.

## Notes on the supplied implementations

These files record the supplied work and should not be treated as fully corrected reference solutions.

- **Q2:** Updates the global `data` variable instead of the `numbers` parameter. The included example works, but passing a different list can fail or change the wrong list.
- **Q5:** Produces the example number, but uses `**` and subtraction, which the exercise's operator restriction does not permit. Building the number with `total = total * 10 + digit` would meet that restriction.
- **Q6:** Changes and returns the original nonempty list; the exercise asks for a new list.
- **Q7:** Starts both counters at zero. The exercise requires positive values, so perfect-square inputs produce extra pairs containing zero; for N = 1 the required output is 0.
- **Q8:** Passes the PDF examples, but returns `[]` for `[1]` and `[1]` for `[1, 2]`. It does not reliably retain the final run.
- **Q9:** Rotates the received list in place; the exercise asks for a new list.
- **Q12:** Concatenates the lists and bubble-sorts them. It avoids the forbidden methods and gives the expected output, but takes quadratic time rather than using the two-index merge described in the PDF.
- **Q13:** Computes the products without division, while also replacing the input elements. Copy the input before calling it if you need to keep its original values.

The question PDF is included unchanged beside this README. Its exercise statements and hints are reference material for this practice set.

## Verification

All 13 scripts reproduce their PDF examples (16 runs total). Additional checks confirmed the Q2, Q6, Q7, Q8, and Q9 limitations above. README links resolve, and the included PDF matches the original file byte for byte. Passing the examples does not imply full compliance with every exercise requirement.
