# first-project
This is my first Git Repository.
<br>
Author - Rakesh (first git repo)

# Load a small text-generation model (google/flan-t5-small) and create a helper function
from transformers import pipeline

print("Loading model (this can take ~30 sec). Be patient...")
generator = pipeline("text2text-generation", model="google/flan-t5-small")
print("Model ready! You can now call generate_text(prompt).")

def generate_text(prompt):
    out = generator(prompt, max_length=120)
    return out[0]['generated_text']
    
