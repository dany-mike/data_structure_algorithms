function reverseString(input) {
  if (input <= 0) {
    console.log("Input 0: --- " + input);
    // Returns are made like in a stack last input return first and first input return last
    return input;
  } else {
    const output = reverseString(input - 1);
    console.log(output);
    return output;
  }
}

reverseString(39);
