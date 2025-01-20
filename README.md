# VERA: Voice-based Railway Enquiry System

## Overview
VERA is an extension of [Indic-Voice-Enabled-Finance-Assistant](https://github.com/rounit57/Indic-Voice-Enabled-Finance-Assistant) , designed to provide railway inquiry services through voice-based interactions in Indian languages. It integrates REST APIs to fetch train-related data and customizes LLM responses using intent classification for improved user experience.

## Features
- **Voice Input Processing:** Converts user audio queries to text using ASR (Automatic Speech Recognition).
- **Intent Classification:** Determines the intent of the query to identify the required functionality (PNR Enquiry, Train Availability, or Live Status).
- **Information Gathering:** Asks the user for missing information (e.g., source station, destination station, date of journey).
- **API Integration:** Fetches train-related data from RapidAPI, which provides dummy results.
- **Humanoid Response Generation:** Converts JSON API responses into human-friendly text using LLM.
- **Voice Output:** Converts the generated text into speech using TTS (Text-to-Speech).

## Workflow
1. **User Query Processing:**
   - User provides an audio input.
   - The system converts the audio into text using ASR.

2. **Intent Detection:**
   - The LLM processes the text to identify the intent (e.g., "I want to go to Chennai" is classified as Train Availability).
   - Extracts necessary details such as source station, destination station, and date of journey.
   - If any required details are missing, the system prompts the user to provide them.

3. **API Call:**
   - Once all required details are available, the system fetches the data from the RapidAPI (dummy API).

4. **Response Generation:**
   - The raw JSON response from the API is processed by the LLM to generate a user-friendly text response.
   - The response is then converted to speech using TTS.

5. **Output to User:**
   - The final response is delivered via both text and voice formats.

## Technologies Used
- **ASR (Automatic Speech Recognition):** To convert audio to text.
- **LLM (Large Language Model):** For intent classification and response generation.
- **RapidAPI:** For fetching train details (dummy API).
- **TTS (Text-to-Speech):** To provide voice responses.

## Example Query Flow
```
User: "I want to go to Chennai."
System: "Please provide your source station and date of journey."
User: "From Delhi on 25th Jan."
System: (Fetches data from RapidAPI and provides response)
"Trains available from Delhi to Chennai on 25th Jan are XYZ Express at 10:00 AM, ABC Express at 5:00 PM."
```

## Future Enhancements
- Support for more inquiry functionalities.
- Integration with real-time railway APIs.
- Support for additional Indian languages.

## Repository Structure
```
VERA/
│-- README.md (this file)
│-- backend/
│   ├── asr_module.py
│   ├── intent_classifier.py
│   ├── api_handler.py
│   ├── response_generator.py
│   ├── tts_module.py
│-- frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│-- requirements.txt
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/rounit57/vera.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Contributing
Feel free to open issues or contribute via pull requests to enhance VERA.

