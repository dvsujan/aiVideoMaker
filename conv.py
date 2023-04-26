from llama_cpp import Llama


def generate_script(prompt):
    llm = Llama(model_path='./models/ggml-alpaca-7b-q4.bin')

    Question = prompt

    output = llm(f"{Question} in 5 bullet points")
    print(output['choices'][0]['text'])
    
    del llm
    print("Script Generation Donw.")
    return output['choices'][0]['text']


def parse_script(script):
    if script[0].isdigit():
        script = script.split('\n')
        script = [i for i in script if i]
        return script
    else:
        script = script.split('.')
        script = [i for i in script if i]
        return script


if __name__ == "__main__":
    # script = generate_script(input("enter input to generate script "))
    # script = open("script.txt", "r").read()
    # script = parseScript(script)
    script = '''
1. The United States is the third-largest country by land area, after Russia and Canada. It covers 3,724,568 square miles (9,641,404 km�) or 27.1% of the world's land area.[3]
2. The United States is one of two countries that have a bicameral legislature; the other being Canada. The U.S. is also unique in having three branches of government: executive, judicial and legislative.
3. The United States has 50 states (plus'''

    script =  script.split('\n'); 
    script =  script[1:];
    script = "\n".join(script)

    script = "".join(script)

    print(script)
