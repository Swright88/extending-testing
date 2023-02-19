# Refactoring Exercise

In the previous sections, you learned how to work with spreadsheets and how to
implement parameterised testing. In this section, you'll bring everything
together by refactoring some tests.

## Your Starting Point

This time, you'll use the codebase inside the `exercise_1` directory. If you
look in `AppTest.java` you'll see that some tests have already been written and
your job will be to refactor them.

## The Missing Piece of This Jigsaw

The one thing we're yet to cover is this - reading from an excel file in a
DataProvider method. To make this work, once you've created the spreadsheet,
you'll need to grab all the test inputs from the file and return them as a 2D
array.

## Tasks

- Create a spreadsheet of your test inputs and expected urls
- Use your own name for all test cases where the data is valid
- Create a DataProvider method
- Inside the DataProvider method, generate a 2D array from the spreadsheet and
  return it
- Replace the test methods with one single test method that uses the
  DataProvider method

## Extension

Create a new class specifically for generating the 2D array. Give it one public
method called `readSpreadsheet` that returns a 2D array and use it in your
DataProvider method.

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fextending-testing&prefill_File=phase8%2F04_refactoring_exercise.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fextending-testing&prefill_File=phase8%2F04_refactoring_exercise.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fextending-testing&prefill_File=phase8%2F04_refactoring_exercise.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fextending-testing&prefill_File=phase8%2F04_refactoring_exercise.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fextending-testing&prefill_File=phase8%2F04_refactoring_exercise.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
