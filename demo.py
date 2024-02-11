from gpt4all import GPT4All

# model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf") 
model = GPT4All("mistral-7b-openorca.Q4_0.gguf") 

prompt_template = "You are an AI assistant that helps me read research papers. Rewrite the following in plain English and explain it like you would to a child: \n\n"

research_statement = """
Laser based optical tools can easily slice through different sections of this complex three dimensional
flow field giving a detailed comparison among different nozzles. 
In this study we utilize the planar laser induced fluorescence (PLIF) technique 
using acetone as the seeding agent within the supersonic jet. 
Though Mie scattering of laser from seeded particles produces strong 
signals that are readily visualized through digital cameras, 
it is difficult to distinguish between seeded and entrained particles when such interactions occur. 
PLIF is sensitive only to that particular seeding particle that can produce 
florescent emissions upon excitation from a definite wavelength of light. 
This is an advantage when conducting experiments to study mixing since the 
tagging of the flow and spread of the passive tracers is unambiguously captured. 
Acetone PLIF has been applied in the study of supersonic free jets [25], [26] 
and supersonic flows in tunnels as well [27].


"""
output = model.generate(prompt_template + research_statement)

print(output)