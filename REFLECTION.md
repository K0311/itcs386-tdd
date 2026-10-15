# Part B: Reflection

## 1. Number of tests and production code
I wrote 9 tests in Part A. The production code contains N non-blank,
non-comment lines. The ratio of tests to production code lines is 9:46.

## 2. Longest red bar
The longest red bar was in A7. The problem was confuse to verify the same-unit reduction test.
I solved it by add def add_rate(self, from_unit, to_unit, rate):

## 3. Fake It, Triangulation, and Obvious Implementation
I used Fake It in A1 by setting the amount to 600. This helped me check
that the test and the implementation were connected correctly.

I used Triangulation in A2. The second example expected 400, so I had
to replace the fixed value with a multiplication formula.

I used Obvious Implementation in A8 by multiplying both sides of the
sum. The rule was clear, so a short implementation was enough.

These choices were appropriate because small steps helped when the
design was uncertain, while direct implementation worked for a clear rule.

## 4. Remaining test-list items
All the original test-list items are complete, including the optional
sum multiplication. Hashing is still listed, but it is outside the
current requirements.

I would defer hashing until quantities need to be used in sets or as
dictionary keys. I would remove it from the current lab scope because
there is no current behavior that needs it.

## 5. Quantity.reduce

I might not have added Quantity.reduce in an initial design because
same-unit reduction first looks unnecessary. However, it allows
Converter to handle both Quantity and Sum through the same operation.

It also gives Quantity responsibility for converting its own amount
using the rate provided by Converter

## 6. Test-after versus test-first development
In Part 0, I tested existing code, so I focused on expected results,
exceptions, and boundary values.

In Part A, the tests helped shape the interface before I implemented
the behavior. The multiplication tests led to returning new objects,
and the mixed-unit test led to the conversion-rate design.
