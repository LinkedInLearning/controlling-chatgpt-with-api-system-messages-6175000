# Controlling ChatGPT with Custom Instructions or API System Messages
This is the repository for the LinkedIn Learning course `Controlling ChatGPT with Custom Instructions or API System Messages`. The full course is available from [LinkedIn Learning][lil-course-url].

![course-name-alt-text][lil-thumbnail-url] 

Custom Instructions in ChatGPT allow you to provide additional context and even format the type of response you want from the system every time you interact with it. In the OpenAI Chat Completions API you can access the same functionality using the System and Assistant messages. In this short course, learn how to take advantage of these features to get more consistent and customizable responses from both systems.

## Instructions
This repository provides examples of how to use message roles and the `instructions` parameter to control the output of OpenAI's language models.

> [!NOTE]
> The easiest way to run and interact with the examples is by opening this repository in GitHub Codespaces.

The examples are found in two folders:
- `./CompletionsAPI` has examples using GitHub Models and the Completions API.
- `./ResponsesAPI` has examples using OpenAI's API and the Responses API.

### Setting up the Completions API examples
If you're running the repository in GitHub Codespaces, the examples in `./CompletionsAPI` will work out of the box without any further setup. GitHub Models are automatically authenticated in the Codespace and the completions will generate when called.

### Setting up the Responses API examples
To run the examples in `./ResponsesAPI` you first need to add an OpenAI API key to your environment:

1. Go to [https://platform.openai.com](https://platform.openai.com) and sign in or sign up
2. Generate a new key at [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
3. Copy the key (you only get to see it once).
4. In Codespaces, open Terminal
5. Set up a new environment variable like this:
```bash
export OPENAI_API_KEY="your_api_key_here"
```

### Running the examples
The examples are self-contained and run in Terminal with the Python command:

1. Open Terminal
2. Navigate to one of the folders:
```bash
cd CompletionsAPI
```
3. Run a script using Python:
```bash
python basic-response.py
```

You are free to experiment by modifying and expanding these examples in any way you like!

[0]: # (Replace these placeholder URLs with actual course URLs)

[lil-course-url]: https://www.linkedin.com/learning/
[lil-thumbnail-url]: https://media.licdn.com/dms/image/v2/D4E0DAQG0eDHsyOSqTA/learning-public-crop_675_1200/B4EZVdqqdwHUAY-/0/1741033220778?e=2147483647&v=beta&t=FxUDo6FA8W8CiFROwqfZKL_mzQhYx9loYLfjN-LNjgA
