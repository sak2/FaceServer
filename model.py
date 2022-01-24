from main import DeepFace

obj = DeepFace.analyze(img_path="img.png", actions=['age', 'gender', 'race', 'emotion'])
print((obj['age'], obj['gender'], obj['dominant_race'], obj['dominant_emotion'], obj))
