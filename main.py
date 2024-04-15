import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

key=os.getenv("OPENAI_API_KEY")

llm=ChatOpenAI(model="gpt-3.5-turbo",openai_api_key=key, temperature=0.7)
output_parser = StrOutputParser()
prompt_template=PromptTemplate.from_template(
    "I'm seeking culinary expertise from an experienced chef well-versed in diverse cuisines. Considering options for Food {food}, Allergies {allergies}, and Cuisine {cuisine}, I'm eager to discover a new recipe. Could you suggest something delightful along with its recipe and macronutrient breakdown?"
)   
# Function to generate recipe based on inputs
def generate_recipe(food_type, allergies, cuisine):
    # Your recipe generation logic goes here
    # For simplicity, let's just return a dummy recipe for now
    #chain = prompt_template | llm | output_parser
    prompt = prompt_template.invoke({"food": food_type, "allergies": allergies, "cuisine": cuisine}).to_string()
    response = llm.invoke(prompt)
    final_response = output_parser.invoke(response)
    return final_response

# Main function to build Streamlit app
def main():
    st.title("What to eat today")

    # Dropdown for food type
    food_type = st.selectbox("Select Food Type", ["Vegetarian", "Non-Veg", "Vegan"])

    # Text box for allergies
    allergies = st.text_input("Enter any allergies (e.g., peanuts)")

    # Dropdown for cuisine
    cuisine = st.selectbox("Select Cuisine", ["Indian", "Thai", "Japanese", "Italian"])

    # Button to generate recipe
    if st.button("Surprise me!"):
        recipe = generate_recipe(food_type, allergies, cuisine)
        st.success("Here's your recipe:")
        st.write(recipe)

if __name__ == "__main__":
    main()