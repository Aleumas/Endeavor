Inspiration
Transferring knowledge from a definition to test questions goes beyond mere memorization of the definition or concept. While flashcards and flashcard apps are useful for memorizing concepts, they often fall short of expanding our overall understanding of the terms we aim to remember. Endeavor, in this context, strives to offer multiple perspectives to facilitate a comprehensive understanding of a concept or term. This approach not only enhances memorization but also makes the application of our understanding more meaningful and effortless.

What it does
The platform gives users the ability to create study sessions by specifying a name, duration, subject, questions, and more. After the session's creation, the user can start answering questions and upon completion, feedback on their responses will be given.

The platform has three standout features:

Curveballs
Users can select an option to add a curveball question to their quiz. By doing so, a question of a new, slightly more challenging level is added to the end of the quiz.

Formative Feeback
Using colors, users can gauge their level of understanding of each response. Additionally, artificial intelligence provides formative feedback, which has been shown to improve learning.

Concept Tree
A visual representation of the generated formative feedback displaying areas of strength and weakness. (The idea is that, over time, the tree will grow, and the color of the leaves will change -- indicating a level of understanding for a given subject/topic)

By repeating study sessions, users can better identify and target misunderstandings as they happen -- leading to better learning outcomes and fostering a growth mindset.

How we built it
I first created the frontend of the platform using a JavaScript framework (Vue.js) and a component library (PrimeVue). I then implemented the feedback and curveball mechanisms using an AI toolkit (LangChain) and an API backend framework (FastAPI) -- all in Python. The concept tree feature was created using natural language processing (spaCy) to extract key terms from user responses (which are used to construct the tree).

Challenges we ran into
Most of the challenges that I ran into, came from the development of the formative feedback feature. I found that the Large Language Model (LLM) was initially both slow and inaccurate. I found that introducing more than three inputs for an LLM to process, with the expectation of parsing its output, turned out to be a bad idea. I realized that LLM's can get confused, so I ended up breaking down my requests into smaller chunks that the LLM could understand accurately.

Accomplishments that we're proud of
I am proud that I was able to complete and submit this project. Although I have been in more than three different hackathons, I have never been able to complete my projects before the deadline.

I am proud that I pushed myself when developing this software. LLMs and natural language processing are both technologies that I have never used before.

What we learned
Through developing this project, I learned how to use new technologies (LLMs and natural language processing). I learned a lot about learning and the growth mindset while doing my early research.

What's next for Endeavour
I was only able to get a barely functioning product out, so there are many things that need to be added.

a database that will store user auth info and user study sessions (currently, everything is stored in a global store)

refine the feedback that the LLM generates (the prompt that I am using to generate the feedback could be improved by using Prompt Engineering best practices)

make the platform a little bit more engaging (maybe adding achievements or other game-like features)

