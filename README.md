# bytekode-2021
### Making Privacy More Accessible

## What This Is
This is a tool that auto detect faces, license plates(cars), and paperwork(confidential/personal documents), and furthermore blurrs them out. This is generally used for individuals who have to edit videos/photos that is going to be posted online. Privacy is quite valued to many people, and therefore   

## What Inspired Me
My cousin is a video editor for a club at his university, and he often has to stay up late to blur out confidential content e.g) school work, license plate on cars. I then wanted to create something that could automate those tasks for him; and I believe the use of object detection is prominent to complete this task. 

## What I Used
I had two options when doing this, one was to use YOLO from tensorflow and the other one was obviously opencv. After careful considerations I decided that I will not be implementing deep learning into this project and will use opencv by utilizing cascade classifiers. Besides from the default classifier made by opencv to detect faces, I trained my own cascade classifier for both the licence plate and document detector. 

## Challenges I Ran Into
Before training a sucessful cascade classifer, I've failed a couple dozen times; and I could not find out the cause. So I had to list out all the possible factors that influence the success rate and eliminate them by implementing it one by one. Through the process of elimination, I came to two conclusions. **Number 1:** When choosing positive/negative cases, the positives has to be very similar in terms of the general features (shape, size, color, etc) if you decide to train with a limited amount of cases (anything below 500). And here comes **Number 2:**, the vice versa of 1, if you decide to have positive test cases that has a large diversity amongst its features, you should have a large amount of cases (at least 1000). 
