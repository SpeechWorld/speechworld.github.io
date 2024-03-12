ljspeech = {
    "61-70970-0024": {
        "text": "In addition, the proposed legislation will insure.",
        "prompt_text":
        "During the period the Commission was giving thought to this situation,",
        "prompt_audio": "audios/ljspeech/LJ049-0185_24K.wav",
        "libritts_audio":
        "audios/ljspeech/LJ049-0185_24K_prompted_libritts.wav"
    },
    "908-157963-0027": {
        "text":
        "During the period the Commission was giving thought to this situation,",
        "prompt_text": "In addition, the proposed legislation will insure.",
        "prompt_audio": "audios/ljspeech/LJ049-0124_24K.wav",
        "libritts_audio":
        "audios/ljspeech/LJ049-0124_24K_prompted_libritts.wav"
    },
}

with open("ljspeech.txt", "w") as f:
    for key, value in ljspeech.items():
        # text-prompts audio-prompts text path
        f.write(
            f'{value["prompt_text"]}\t{value["prompt_audio"]}\t{value["text"]}\t{value["libritts_audio"]}\n'
        )

librispeech = {
    "61-70970-0024": {
        "text":
        "They moved thereafter cautiously about the hut groping before and about them to find something to show that Warrenton had fulfilled his mission.",
        "prompt_text":
        "He slowly descended the ladder and found himself soon upon firm rock.",
        "prompt_audio": "audios/librispeech/61-70970-0024/prompt.wav",
        "libritts_audio": "audios/librispeech/61-70970-0024/libritts.wav"
    },
    "908-157963-0027": {
        "text": "And lay me down in thy cold bed and leave my shining lot.",
        "prompt_text": "milked cow and tames the fire.",
        "prompt_audio": "audios/librispeech/908-157963-0027/prompt.wav",
        "libritts_audio": "audios/librispeech/908-157963-0027/libritts.wav"
    },
    "1089-134686-0004": {
        "text":
        "Number ten, fresh nelly is waiting on you, good night husband.",
        "prompt_text":
        "faced up and down, waiting, but he could wait no longer.",
        "prompt_audio": "audios/librispeech/1089-134686-0004/prompt.wav",
        "libritts_audio": "audios/librispeech/1089-134686-0004/libritts.wav"
    },
    "1221-135767-0014": {
        "text":
        "Yea, his honourable worship is within, but he hath a godly minister or two with him, and likewise a leech.",
        "prompt_text": "windows, the wooden shutters to close over them.",
        "prompt_audio": "audios/librispeech/1221-135767-0014/prompt.wav",
        "libritts_audio": "audios/librispeech/1221-135767-0014/libritts.wav"
    },
}

# import whisper
# model = whisper.load_model("large-v2")
# for key in librispeech:
#   result = model.transcribe(librispeech[key]["prompt_audio"])
#   print(f'{key} {result["text"]}')
#   librispeech[key]["prompt_text"] = result["text"]

environment = {
    "1": {
        "text": "I think it's like you know um more convenient too.",
        "prompt_text":
        "What'd you like about one flew over the cuckoo's nest?",
        "prompt_audio": "audios/fisher/1_pt.wav",
        "libritts_audio": "audios/fisher/1_libritts.wav"
    },
    "2": {
        "text":
        "Um we have to pay have this security fee just in case she would damage something but um.",
        "prompt_text": "We have Japanese fighting fish.",
        "prompt_audio": "audios/fisher/2_pt.wav",
        "libritts_audio": "audios/fisher/2_libritts.wav"
    },
    "3": {
        "text":
        "Everything is run by computer but you got to know how to think before you can do a computer.",
        "prompt_text": "This is where that line has been.",
        "prompt_audio": "audios/fisher/3_pt.wav",
        "libritts_audio": "audios/fisher/3_libritts.wav"
    },
    "4": {
        "text": "As friends thing I definitely I've got more male friends.",
        "prompt_text": "say, oh my god, I've got really bad PMS.",
        "prompt_audio": "audios/fisher/4_pt.wav",
        "libritts_audio": "audios/fisher/4_libritts.wav"
    },
}

emotion = {
    "anger": {
        "text": "We have to reduce the number of plastic bags.",
        "prompt_text": "Her face was against his breast.",
        "prompt_audio": "audios/emov_db/anger_pt.wav",
        "libritts_audio": "audios/emov_db/anger_libritts.wav"
    },
    "sleepiness": {
        "text": "We have to reduce the number of plastic bags.",
        "prompt_text": "Shut down and tune in.",
        "prompt_audio": "audios/emov_db/sleepiness_pt.wav",
        "libritts_audio": "audios/emov_db/sleepiness_libritts.wav"
    },
    "neutral": {
        "text": "We have to reduce the number of plastic bags.",
        "prompt_text": "Do you know that you are shaking my confidence in you?",
        "prompt_audio": "audios/emov_db/neutral_pt.wav",
        "libritts_audio": "audios/emov_db/neutral_libritts.wav"
    },
    "amused": {
        "text": "We have to reduce the number of plastic bags.",
        "prompt_text": "That's what Carnegie did.",
        "prompt_audio": "audios/emov_db/amused_pt.wav",
        "libritts_audio": "audios/emov_db/amused_libritts.wav"
    },
    "disgust": {
        "text": "We have to reduce the number of plastic bags.",
        "prompt_text": "map she said",
        "prompt_audio": "audios/emov_db/disgust_pt.wav",
        "libritts_audio": "audios/emov_db/disgust_libritts.wav"
    },
}

# import whisper

# model = whisper.load_model("large-v2")

with open("libritts.txt", "w") as f:
    for key, value in librispeech.items():
        # result = model.transcribe(librispeech[key]["prompt_audio"])
        # print(f'{key} {result["text"]}')
        # librispeech[key]["prompt_text"] = result["text"]

        # text-prompts audio-prompts text path
        f.write(
            f'{value["prompt_text"]}\t{value["prompt_audio"]}\t{value["text"]}\t{value["libritts_audio"]}\n'
        )

    for key, value in environment.items():

        # result = model.transcribe(environment[key]["prompt_audio"])
        # print(f'{key} {result["text"]}')
        # environment[key]["prompt_text"] = result["text"]

        # text-prompts audio-prompts text path
        f.write(
            f'{value["prompt_text"]}\t{value["prompt_audio"]}\t{value["text"]}\t{value["libritts_audio"]}\n'
        )

    for key, value in emotion.items():

        # result = model.transcribe(emotion[key]["prompt_audio"])
        # print(f'{key} {result["text"]}')
        # emotion[key]["prompt_text"] = result["text"]

        # text-prompts audio-prompts text path
        f.write(
            f'{value["prompt_text"]}\t{value["prompt_audio"]}\t{value["text"]}\t{value["libritts_audio"]}\n'
        )
