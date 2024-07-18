# 🐚 APIinaShell

An API deployed using fastapi running LlamaCpp as the backend to do LLM inference. The purpose of the script is to abstract the complexity of deploying a LlamaCpp API instance on a global scale.

## 📦 Dependencies
- llama_cpp_python
- fastapi
- requests
- uvicorn

Install with `pip`.

## 🗺️ How to 
To start using the api, you need to ensure that LlamaCpp is installed.
- Download a fresh GGUF converted model from [Huggingface](https://huggingface.co/models?sort=trending&search=gguf) and provide the path to it in the script.
- In a command prompt, run `uvicorn apiinashell:app --reload --host <ip address> --port <port number>`.
This should start the api server at the configured address.
- Open a browser and browse to the address displayed in the command prompt by appending 📰 /docs. You should see the :dependabot: api interface.
- You can then enter a string to test it out. See video :

## 🎥 Short Films
https://github.com/perpendicularai/APIinaShell/assets/146530480/87491a67-4691-4574-90ae-ed55d4126b58

