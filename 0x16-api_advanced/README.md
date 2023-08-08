# 0x16-API_Advanced

## Background Context

API-related questions are common in interviews, spanning from basic endpoint queries to recursive functions and result formatting/sorting. The Reddit API offers an ideal playground for honing these skills. With numerous endpoints, many not requiring authentication, this practice can bolster your technical interview performance and enhance personal projects.

## Overview

This repository contains Python scripts demonstrating Reddit API interactions. Covering subreddit information, hot posts retrieval, keyword occurrence counting, and more, these examples provide practical insights into API calls, JSON parsing, recursion, and data manipulation.

## Learning Objectives

By engaging with this project, you will achieve the following learning objectives:

1. **Reading API Documentation**: Navigate and understand API documentation to identify endpoints and parameters.

2. **Pagination Handling**: Master pagination to efficiently retrieve substantial data.

3. **JSON Parsing**: Proficiently parse JSON responses to extract relevant information.

4. **Recursive API Calls**: Learn to use recursion for successive API calls, like fetching all posts in a subreddit.

5. **Sorting Dictionaries**: Acquire the skill to sort dictionary data by values, vital for meaningful result presentation.

## Resources

To excel in achieving these objectives, leverage these resources:

- [Reddit API Documentation](https://www.reddit.com/dev/api/): Explore official documentation for endpoints, parameters, and response formats.

- [Query String](https://en.wikipedia.org/wiki/Query_string): Understand the query string format for API requests.

## Scripts

This repository features the following scripts, addressing distinct API interaction aspects:

1. `subs.py`: Query the Reddit API for subscriber counts in a subreddit.

2. `top_ten.py`: Retrieve and display titles of the first 10 hot posts in a subreddit.

3. `recursive & count.py`: Recursively count keyword occurrences in post titles, presenting sorted counts.

## Usage

1. Clone or download this repository to your local machine.

2. Install required libraries using VS Code's integrated terminal:

```bash
pip install requests
```

3. Open any provided script in VS Code.

4. Customize variables like subreddit names or keyword lists.

5. Run a script using VS Code's built-in terminal:

```bash
python script_name.py
```

## Contributing

Contributions are welcome! If you have suggestions, enhancements, or additional examples, open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

By engaging with this repository, you'll gain valuable API interaction skills that aid technical interviews, projects, and overall development.

---