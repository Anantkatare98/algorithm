def cocktail_sort(arr):
	n = len(arr)
	swapped = True
	start = 0
	end = n - 1
	while swapped:
		# Move from left to right
		swapped = False
		for i in range(start, end):
			if arr[i] > arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]
				swapped = True
		if not swapped:
			break
		end -= 1
		# Move from right to left
		swapped = False
		for i in range(end - 1, start - 1, -1):
			if arr[i] > arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]
				swapped = True
		start += 1

# Example usage
arr = [5, 2, 9, 3, 7, 6]
cocktail_sort(arr)
print(arr)

function cocktail_sort(arr) {
	let n = arr.length;
	let swapped = true;
	let start = 0;
	let end = n - 1;

	while (swapped) 
	{
	
		// Move from left to right
		swapped = false;
		for (let i = start; i < end; i++) {
			if (arr[i] > arr[i + 1]) {
				[arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
				swapped = true;
			}
		}

		if (!swapped) break;

		end -= 1;

		// Move from right to left
		swapped = false;
		for (let i = end - 1; i >= start; i--) {
			if (arr[i] > arr[i + 1]) {
				[arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
				swapped = true;
			}
		}

		start += 1;
	}

	return arr;
}

// Example usage
let arr = [5, 2, 9, 3, 7, 6];
cocktail_sort(arr);
console.log(arr);
