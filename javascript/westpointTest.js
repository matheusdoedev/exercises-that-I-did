// Write a function that creates an array of 20 random numbers between 1 to 100 and returns the lowest and highest number present in the array.

const main = (params) => {
  const numbers = generateRandomNumbers();

  if (!(numbers instanceof Array)) {
    throw Error("numbers is not an array.");
  }

  const lowestNumber = findLowestNumber(numbers);

  const highestNumber = findHighestNumber(numbers);

  return [lowestNumber, highestNumber];
};

const findLowestNumber = (numbers) => {
  let lowestNumber;

  numbers.forEach((number) => {
    if (!lowestNumber || number < lowestNumber) {
      lowestNumber = number;
    }
  });

  return lowestNumber;
};

const findHighestNumber = (numbers) => {
  let highestNumber;

  numbers.forEach((number) => {
    if (!highestNumber || number > highestNumber) {
      highestNumber = number;
    }
  });

  return highestNumber;
};

const generateRandomNumbers = () => {
  const randomNumbers = [];

  for (let count = 0; count < 20; count++) {
    const number = Math.round(Math.random() * 100);

    randomNumbers.push(number);
  }

  return randomNumbers;
};

main();
