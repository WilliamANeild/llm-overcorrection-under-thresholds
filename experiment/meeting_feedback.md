# Lab Meeting Feedback - Study 3 Revision Yield

Paste your Zoom transcript and notes below this line.



---

Liam Neild
13:08:14
Okay. So it kind of just details sort of what we wanted to go over last time, then also some of the changes that I hopefully implemented correctly.
Ali Emami
13:08:21
Awesome. Oh, yeah, let's let's transcribe. I just I'll turn on AI companion for you.
I think you can start it because you're the host.
Liam Neild
13:08:29
Yeah, I think… I think it's going right now, but um…
Ali Emami
13:08:32
Oh, it's going right now? Awesome, so you'll have the notes. Okay, great. Sorry.
Liam Neild
13:08:35
Yeah, exactly, exactly.
Um, but yeah, so it pretty much aims to find, or measure, um, quality with a calibrated judge. Um, I, I, I was asking myself, like, the two sentences, like, because we keep asking, um.
So when you ask an AI like ChatGPT to revise its own work, it almost always says yes and makes changes, even when the work was already good enough. This paper measures how that cost is wasted effort and the quality loss across six major AI models across 40 real tasks and tests a way to really fix it.
Ali Emami
13:09:03
I love that you're doing the two sentences, because it helps me jog my memory, and then I think I just want to focus on two things in that pitch. It was almost perfect. Only two things that I sort of flagged in my head was the first thing I saw when he said, revise its own work. This is just rhetorical. I think, like, it doesn't matter how we word it.
in terms of the study, but is it its own work, or your work with it? Yeah, you have to kind of watch out, because when it's its own work, it just assumes there's no autonomy on your end.
Liam Neild
13:09:23
Or out.
Okay, okay.
Ali Emami
13:09:31
Um, but that… that hopefully shouldn't affect anything that you're doing, but it is important that in the paper, and generally, you frame it as, like… because it could be your work, too. It's like, you're the first one that gives the email draft or something as well, so it shouldn't be just it. Now, the one that is a little bit load-bearing.
Liam Neild
13:09:45
Absolutely.
Ali Emami
13:09:49
Is when you said…
and quality loss.
So, I'm a bit confused there, because is that… is it that you're expecting that the quality should be lost, or…
That there's nothing gained.
Liam Neild
13:10:02
That's something that I've been playing around with because.
Well, we'll get to it a little bit more in the, uh, grading, uh, sort of, like, framework that I sort of wanted to lay out, um, but something that I sort of laid out was that overcorrection can sometimes mean that AI sometimes just hallucinate and add other things, and that would, in turn, make your thing worse.
You're right, quality costs.
Ali Emami
13:10:21
Yeah, but then you're sort of… you're saying this paper measures how much. Now, if you're saying it measures how much you're going in, you don't know that that's going to happen. I think you should be a little bit more open-ended in the question for which there will be an answer. For example, um, and…
Liam Neild
13:10:32
Okay.
Ali Emami
13:10:36
It's like you're looking at quality itself, not quality loss, because it could have went the other direction.
Liam Neild
13:10:43
Mm-hmm.
Ali Emami
13:10:43
Because I personally would have thought it's wasted effort and more like quality. It's like diminishing gains in quality.
Liam Neild
13:10:52
That makes sense.
Ali Emami
13:10:52
Right? So, uh, wasted effort and quality… I don't… I think there's a word for it, but quality…
trajectory or something across six major models, but that, I think, will be important, so you should keep that in mind.
Liam Neild
13:11:00
Yes.
Absolutely. Um, so the models I ended up going with were obviously the three that we started with, um, just GPT-4o, Claude, Gemini, and then I… for the open source ones, I could have gone with, like, a Gemma, but I decided that would be two Google models, so I just went with these three, um…
Ali Emami
13:11:11
Nice.
Good.
Liam Neild
13:11:18
I don't know if there's.
Ali Emami
13:11:19
No, that looks good.
Liam Neild
13:11:20
You go there. Um, so here's sort of what the, uh, rough, like, protocol or recipe would look like.
so first would be the judge calibration. I sort of incorporated what we would look… what we were looking for last time with, um…
If we took a smaller sample size, ran all of them as judges, and then also did a human evaluation, then continued to use whatever judge.
worked best with the humans, or was most highly correlated, so that's sort of what this is sort of detailing. This six-level scale, I'll talk about a little bit later, it's sort of what you were talking about earlier with.
Ali Emami
13:11:38
Mmhm.
Liam Neild
13:11:50
Between the binary, I kind of made it into six levels. I can go to that later, but I think going here would be next. Um, so here's sort of the bulk of the content, just like the working conversations. Um, so it's 40 tasks, um, across creative to code. I've got all of those laid out a little bit lower down here.
Ali Emami
13:12:05
Mm-hmm, mm-hmm.
Liam Neild
13:12:06
I don't know if you want to go through those, but they're pulled just from, like, other fields that would sort of…
make itself a little more valuable to maybe… or maybe a little more feasible for things. Um, so the… the probe that I went with, or that we kind of talked about earlier, was…
Uh, would you like to keep this as your final version, or would you like to revise it? Um, I feel like that was the most neutral thing, but obviously that'.
Ali Emami
13:12:28
That is really neutral. That's not bad because I actually personally never say, would you like to keep it as a final version? Because it gives you the, it's actually almost too fair because it gives the opportunity for the model to be like, no, this is actually good. So if I looked at it, I wouldn't.
Like, if you said, would you like to revise it?
I would have wondered, maybe that's fair, that's a good probe, but, um…
Yeah, I think it's an interesting kind of junction here, where it's like, you chose that, you could have edited it, and then the question is, like, why did you choose that? It's a good one, I don't think it's bad, I.
Or would you like to revise it? I kind of like it. It's just… is it how you would have worded it? Like, I feel like I would say something like…
Liam Neild
13:13:13
In a real like conversation.
Ali Emami
13:13:14
Yeah, yeah, like, I… and I've used them almost too much these days, but I, like, I'll have a draft of some… yeah.
Liam Neild
13:13:19
Honestly…
In all honesty, I probably don't use that, and I'm not really…
Um, I don't know. I guess, like, I usually go with, what do you think about it? Or, like, but that's obviously very not revision. That's obviously very not neutral, because I don't care about my token.
Ali Emami
13:13:32
Yeah, and that becomes hard if, like, it gives you outputs that are not easily, yeah, revision related. I get it.
Liam Neild
13:13:37
But I think that sort of goes into our question that we were talking about earlier, like, my tendency is that I'm more willing to, like, waste tokens. I have the whatever… I have whatever tokens left, and I'm usually not, like, hitting that threshold, so that might actually be a product of…
my economics or whatever, like my token use. I'm not of the probe or whatever.
Ali Emami
13:13:55
Uh-huh.
I'd like to keep this as a final version, or would you like to revise it? Actually, it's fine. No, for now, let me humor that. It's not bad, it's actually really cool that you say, like, it has two ch.
Um, okay.
Liam Neild
13:14:09
So now, I mean, you can go kind of two directions. We sort of talked about that one shot ceiling. This hasn't changed much from last time. It just sort of, I think it worded a little bit differently than I wanted it to here, actually. But the instructions would pretty much just be, would you like to keep this as your final version or not?
Um, but I, I think the, this is what I wanted to play around with, um, and sort of ask your opinion on because we wanted to see if it keeps revising, how many times does it really go to maybe with the least neutral or the most neutral? How many times does it go until it really just says like, this is good, this is good, especially across.
Ali Emami
13:14:40
Wait, yeah, what exactly is Phase 3? I'm a bit confused, because that's Phase 1.
Liam Neild
13:14:44
Yeah. Yeah, you're right. So I guess that doesn't make sense. It's not really connected. This was just something you and I were talking about, and it'd be interesting to keep in the paper. But following the logical flow of the entire experiment, phase two would probably be the next thing to go through.
Ali Emami
13:14:56
Okay.
Liam Neild
13:14:57
So I guess I'll go back to that.
Ali Emami
13:14:58
No, but that was interesting. Yeah, come back to that because there was something there. You're right. Okay.
Liam Neild
13:15:01
Yeah, we can totally come back to that. I guess for this, it would be just now we would use a fresh instance of the judge that we selected in phase 0.
Um, and grade all of them. Um, here is sort of, I think we talk about this, um, in more detail a little bit later. Um, but here's sort of the scale that I wanted to go through that made it a little bit less binary. Um, so it's just all the little, like, I mean, it goes adequate, incomplete, or whatever.
Ali Emami
13:15:20
Mmhm.
Mm-hmm.
Liam Neild
13:15:27
But then I tried to make it as specific as possible. I think in the real, um, UI that I made for, like, the grading or whatever, um, it's a little bit more specific than this, so inadequate is…
Inadequate would be doesn't address the task or so wrong it needs to be completely restarted. A user couldn't build on this at all.
Ali Emami
13:15:47
No, this isn't bad. And then, like, are you expecting that if we're gonna do maybe some validation of the judge with humans, like, maybe on the sample of 20, this is somewhat what… or exactly the rubric you'd give humans?
Liam Neild
13:15:58
Yeah.
Exactly, this would be the rubric I would give humans. I mean, of course, this would be a little expanded on, it's just not worth putting it in the box, because pretty much. But yes, this is the six, or sorry, this is the…
Ali Emami
13:16:06
Okay, yeah, yeah, I feel you, okay.
Nice.
Liam Neild
13:16:12
The six level scale that here.
Ali Emami
13:16:14
Good job, good job, so far so good, okay?
Liam Neild
13:16:17
This is sort of how I wanted to break down in terms.
Ali Emami
13:16:18
No, it's actually really sensible. I actually really like it. I like the choice. Because I agree that one to three suggests that there are revisions. Four to five, they are different within not needing revisions, but one of them is clearly better than the other. Six is overcorrection signal.
Liam Neild
13:16:22
Um…
Ali Emami
13:16:34
Oh, I didn't check that one out. Let's see, unrequested complexity tool. Now, you said unrequested, that's interesting, because if you're just looking at output, then how would they…
How would they compare to the request?
Liam Neild
13:16:47
I think that's a great idea. It's sort of…
dependent on each scenario, um, so I guess unrequested would be, like.
I don't mean… I think it…
Ali Emami
13:16:57
So you could say overly complex, so you don't have to actually relate it to the question, because that way, right now, it looks like it's depending on the question itself.
Liam Neild
13:17:07
Okay.
Um, okay.
I'm gonna put that in my notes just so I can fix that guy.
Ali Emami
13:17:13
Unless the judgment has to be paired with the task, which becomes okay. Like, I don't know, because I think if you're giving a judge this rubric, they kind of, I guess, need to know what the task is.
Liam Neild
13:17:27
Yeah.
Ali Emami
13:17:28
So, it could be okay, actually, if the task…
Liam Neild
13:17:29
Oh.
is…
Ali Emami
13:17:33
Like, write me an email, and then maybe then they can judge it with respect to the request, and then they'll say it's unrequested complexity.
Liam Neild
13:17:34
Excuse the river.
That makes sense. Maybe if there's a custom rubric to each.
Or like a somewhat tailored.
Ali Emami
13:17:45
No, not that it's a custom rubric. Maybe, I mean, that's also a thing, but I'm saying, here, there's no way that you would be able to determine unrequested unless you see the task.
Liam Neild
13:17:54
Okay, got it.
Ali Emami
13:17:55
Yeah.
Liam Neild
13:17:56
All right. I'll look over that. OK. Now we would go back to the one-shot ceiling because that's the build. These are all sub-experiments that we talked about. Reversibility, we spoke about. The one-shot ceiling, this is something I'm playing around with, but I don't think I've nailed it quite yet.
Ali Emami
13:18:01
Okay.
Okay.
So you're basically just asking a model to do it once, and you want to see its potential.
Liam Neild
13:18:14
No.
Ali Emami
13:18:22
Just the sheer performance on the one time that it did it.
Liam Neild
13:18:25
No, um, sorry, that is kind of what this is saying, but no, sorry. Um, we were talking about this earlier. So, remember when, like, we would go through a Claude task and sometimes be like.
Ali Emami
13:18:34
Oh…
Liam Neild
13:18:36
no, this is good enough, send it. And I… we run into this most with Claude, and that's something that I really appreciated about it, but you… I wanted… we wanted to see how.
maybe with the… let's imagine with the least neutral probe as opposed to this, like, can this be revised? How many times could I ask it, can this be revised, until each model eventually says, yeah, like, no, no, no, just send it, just send it, just submit it, or whatever.
Ali Emami
13:18:56
Yeah.
Liam Neild
13:18:57
Um, so that's sort of what I wanted to get out with this, but I feel both the… this part, this… what I… what I… exactly I ask it, because I don't think I can ask this exact thing, would you like to revise this as your final version?
Ali Emami
13:19:06
No, I see what you're saying. So…
I see. But I thought what was happening… I think there should be some sort of study here, but let's get it right. So, um, the main thing that you're doing is you're giving a task.
And the task itself.
like, is there a system prompt for each that's separate from the instruction, produce the best possible, or is it you straight up just say, like, you give it the task, and then after it gives you the output, you give it that probe? Would you like to keep this?
Liam Neild
13:19:36
what I was imagining was the second version of that, where it would just be, um, the question…
like, um, the question written out, and then just the probe. It would… there was no Simpson prop, like, always artist, or make it the most complete product. There was never…
Ali Emami
13:19:43
Mm-hmm.
Okay.
Okay, and then one shot is that it's, like, your… it's another paradigm where the user can…
Maybe try this out, which is don't…
Keep asking for revisions, but just straight up once a…
Do it once.
The thing is, we have to think about if it's worth the extra experiment because uh.
If the purpose of this is for you to see if revisions even.
Um, helped. You would be able to do that with respect to the first output.
Liam Neild
13:20:18
Yeah, this, this, that sort of reversibility, um, that's, that's exactly what you're talking about.
Ali Emami
13:20:21
Fresh instance sees… I think you remembered something that I just don't remember in terms of one shot, and I'll get to it, but reversibility is fresh instance sees turn 1 output and turn 5. Oh, fresh instance as in judge, right?
Liam Neild
13:20:34
Yeah, sure. So I think I actually put fresh instance, but it could be, yeah, the judge Whatever one we use would be.
Ali Emami
13:20:43
Yeah, and I like the randomized AB, which works, because then maybe you'll run it twice. And actually, what you should do is, you should run it, like, 20 times, actually, and then you see the total win rate between one or the other, and then you also shuffle.
And you randomize. And then you can truly see if one was better than the other. And it'd be, that's already, the reversibility, I buy it. I'm a buyer for that. That's actually like the point. That's about the diminishing return. And you may have found, or maybe you're going to start seeing that maybe five is significantly worse than one.
Liam Neild
13:21:02
Mm-hmm.
Mm, okay.
Ali Emami
13:21:15
Um, and by the way, it looks like people are starting to catch on to our idea here. Not exactly the same thing, but apparently there's a, like, both Twitter and LinkedIn, I saw this, but people are saying.
Straight up, stop trying to give lessons to Claude Code, like, to say, save this as a lesson, save this into memory, it makes the performance worse. You should just tell it, don't let it know you, don't let it personalize to you, it'll do it worse, because it's trying to, I think, juggle multiple things, like, oh, how do I get…
Liam's expertise to, like… and if you just straight up don't do that, the models do better. This is within that theme, which is sometimes less is more.
Um, but yeah, I think, like, this is a really good one, reversibility. I just don't… one shot confuses me a bit, because I'm like, I feel like you're scratching that itch with reversibility, but what does one shot do? Is one shot more like…
Liam Neild
13:22:04
It's sort of, to put it weirdly.
Ali Emami
13:22:06
Oh, maybe you're telling the model, look, you don't have another chance.
Liam Neild
13:22:11
Oh, well, okay.
Hmm, let me see. So it's really…
Ali Emami
13:22:14
Because how about, could it be this? Is it that models have been pretty much RLHFed into a place where they expect that secondary revision question, so they might not give you their best shot.
Here, you're trying to put them in a place where you're going to give me your best shot so that I could see if, maybe for an economic user, this could be better for them to prompt you this way.
Liam Neild
13:22:39
Interesting. In my mind, what it was, was, um, so disconnected. It's a little bit disconnected from the rest of the experiment. It's just, like, a sub-experiment that you and I found somewhat interesting, like, over one conversation. It was just, like.
Asking the model, can this be revised? Every single response, no matter the response, and seeing at what point it actually stops.
Ali Emami
13:23:01
Mm-hmm.
Liam Neild
13:23:03
Like, it literally doesn't matter the experiment, it would literally, like, it doesn't matter which one of the, uh…
like, uh, tasks. We wanted to see across all the different kinds of tasks when it literally.
Ali Emami
13:23:14
But what do you mean by stop? It only does it once.
Liam Neild
13:23:17
What if, um… the first time we asked, can this be revised? Yes. Can this be revised? Yes. How many times can we go giving zero input and just saying, can this be revised, over and over?
Ali Emami
13:23:27
Oh, that's what that is? If that's what that is, that's great, but it's just that it wasn't worded like it suggests that. I don't know why you're saying produce the best possible version…
Liam Neild
13:23:28
That's right. That's right.
Okay.
Ali Emami
13:23:36
Take your time.
Um, I thought, basically, the purpose of this study is to do Phase 1 repeatedly until.
You basically…
You want to see when the model stops.
Liam Neild
13:23:51
Yes.
Ali Emami
13:23:53
So, it's just phase one, it's like, it's just phase one, um, where…
You're just making sure you're going to…
Oh, I see what I'm trying to say. Basically, what if phase one, they never do stop and they go up to three or four or five and five is like your cutoff window for what you're like measuring. This phase, this experiment is just going to say, I'm not going to.
Liam Neild
13:24:13
Yeah. Okay.
Ali Emami
13:24:17
look at quality, I just want to see, like, when they'll each stop.
Liam Neild
13:24:21
Yeah, exactly. That's exactly it.
Ali Emami
13:24:23
That's a good study. That's a good study.
Liam Neild
13:24:25
Also across the entire spectrum of.
Ali Emami
13:24:28
Yes, also across the entire spectrum. This is more of a meta thing. You're right, it's a different issue, and it's more like… it's kind of like a model confidence on each task kind of thing.
Liam Neild
13:24:30
Is it…
Exactly. Is it more confident in code? Is each model different?
Ali Emami
13:24:39
Yeah, I love this. I love this. It actually adds another leg to the study and makes it more rich. So I actually really like it. Okay, great.
Liam Neild
13:24:48
Now, I think this was another sub question, also tangentially related to everything else. It was just to see if the model or whatever judge we use, whatever we find in phase zero, if we give it the ability to give targeted feedback.
That would produce better results than would you like to revise? This one I'm sort of playing around with because it also seems like.
Of course, there's gonna be better feedback, um, or…
There could not be because if one model is just saying something, why wouldn't the original instance of the model be able to just find that exact issue for itself?
Ali Emami
13:25:24
Yeah, but I kind of like your… I like your mentality here, because you're trying to be not just probing, you're trying to solve… I don't know if here you're trying to solve the problem, but it seems like it's directed there. It's like, you're trying to say.
What if you have, like, a multi-agent setup? I use that term lightly here. It's not exactly multi-agent, but something where there is a judge that looks at the output and determines, according to the rubric, if it even needs revision, and then it would override what the model would say and say, listen, it's good enough.
Liam Neild
13:25:53
Yeah, exactly.
Ali Emami
13:25:53
But I think here you're saying, but I think that's not exactly my idea here. You're doing something else, which is neat. You're saying, does directed feedback produce better? Oh, no, no, this is cooler. I see. You're saying, does directed feedback produce better revisions than would you like to revise?
Liam Neild
13:26:11
So, as a…
Ali Emami
13:26:11
You're using the feedback of the evaluator.
Liam Neild
13:26:14
Mm-hmm.
Ali Emami
13:26:17
No, I like it. I really like it. Because…
Yeah, I really like it, because what… if… let's say you find that quality doesn't increase with, would you like to just revise? You're saying it's really the laziness of that, where if you're just saying, would you like to revise? It's not targeted enough, so the model might start to fix something that wasn't an issue and not actually fix the problem.
Liam Neild
13:26:40
Exactly.
Ali Emami
13:26:40
So I think I like this idea as well. Very nice.
Liam Neild
13:26:44
In my mind, what the actual, um, results, or the actual experiment will yield, will be that it either doesn't change it at all, because why would an evaluator be able to give better advice than the original instance? They're looking at the same.
Ali Emami
13:26:56
Good, but that's a good, that's a deep question. Paradoxically, it might be that it does.
Liam Neild
13:26:58
Or…
Or it actually does, and something that's just…
Ali Emami
13:27:04
Because models are more focused on sycophancy and so many, that's what I was trying to say. It's like one thing is about trying to tailor it to what Liam tends to think and what the lessons it learns are. It doesn't actually think about, I just need to solve this one problem. But that's what the user needs at that point.
Liam Neild
13:27:05
Eyes down.
It's…
Ali Emami
13:27:20
I think you actually will be surprised to find this might work.
Liam Neild
13:27:21
It's, yeah.
Especially if I give, like, a good, like, uh, sort of put the judge in sort of, like, an eyes, or, like, a bird's-eye-view kind of perspective with, like, a prompt, like, um, just give objective, like, feedback on how to make, improve this, or something. I feel like just that.
Ali Emami
13:27:34
Yes.
Yeah, yeah, exactly. It's bird's eye view as in, it's unbiased as in, I often do it the same, by the way. This is what, I mean, eventually when this becomes a paper, you might learn from the lessons of your results to write the paper this way. I will never, if I'm editing something, say, this is my, I mean, actually, I'm lying if I say I never do this, sometimes I do, but if I really want to make sure I get something perfect.
I will give a paper. In fact, I do it even the other extreme. I give my paper, and I say, I am a reviewer of this paper. Help me synthesize a review. Often, reviewers are negative. So then I'll get that negative review, and then I'll adjust it. If I said.
I'm about to submit this paper in 5 minutes. I know, of course, I'm being facetious, but you see how if you say that.
It's actually probably not going to revise your paper.
Liam Neild
13:28:25
Exactly. It's going to go for maybe one thing as opposed to seven.
Ali Emami
13:28:28
It's gonna say it's great. Yeah, one thing, it's great. And yeah, exactly, it wants to say that it helped, so it says a few little things, and then it says you're done. I mean, that itself, by the way, is.
I think your study is probably going to raise tons of interesting questions like this, because you did it in terms of number of revisions, the revision itself, but what if it's about situation that you, um, contextualize the model in? So, like, I'm about to submit a paper versus, like.
I'm at the, you know, the beginning phases of writing. The model's probably going to do better for you if you do that.
Liam Neild
13:28:57
Right?
I actually really like that as a sub-experiment. Maybe I should add on. Just like a…
When giving at the very start of a system prompt or just prompt overall, if you give it a situation that is.
Ali Emami
13:29:11
Yeah, maybe to make it simple, Liam, because if you do that, you might open Pandora's box too much in terms of, oh, but how does it all relate? You could do it in terms of what we say agent versus patient of the task, meaning agent is the one that needs the task done.
Liam Neild
13:29:11
We hear you.
Yeah, that might be it.
Ali Emami
13:29:27
I mean, I'm using these terms a bit loosely, but patient is the one that receives the task. So I've gotten the email, and I have to fix this sometimes, because sometimes I'm, like, typing really quickly to Claude. I'll say, this is an email draft, and then it'll be like, yeah, they didn't write you a good email.
Liam Neild
13:29:29
No, I understand.
Ali Emami
13:29:44
And I'm like, no, no, no, I'm the one writing it. And then it goes, no, no, it's a great email. So, like, so maybe it's about the recipient versus the.
Liam Neild
13:29:47
Okay.
Okay.
That's really funny, actually.
Ali Emami
13:29:53
Yeah, yeah. So actually mine was, what was mine? Yeah, anyways, it was really what I was saying actually happened. But so I think maybe you could do it that way is that it's the recipient versus the sender and you can show that there's that bias. This is really big. This is all really, really good study and I love how you organized it.
Um, and then self-reflection is the last one, plus maybe, I guess, the one that I suggested here, Phase 7.
Liam Neild
13:30:13
This is…
Yeah, exactly. This was somewhat related to reversibility, but a little bit different.
Ali Emami
13:30:17
And yeah.
Liam Neild
13:30:23
I think of them the exact same, and potentially combining them. It just asks, like, in the sixth turn, as opposed to in a new instance, versus, like, looking.
Ali Emami
13:30:33
I like it. I like it. Yeah. I like it because this is, I love that. And this is the right term. You can either evaluate using self-reflection or you can do it objectively with that kind of reversibility thing. And this one, in my opinion.
Liam Neild
13:30:34
Just ask which one you actually use it.
Yeah.
Ali Emami
13:30:49
We'll make the model biased to always prefer the last one.
Liam Neild
13:30:52
You think this… you think this, uh…
This line right here.
Ali Emami
13:30:56
Oh, but you're saying self, right? So self means that the model Yeah, yeah, is aware of the fact that these are all these orders. Yes, yes, yes. Yeah.
Liam Neild
13:30:59
Yeah, yeah, yeah.
Yeah, so it's in the running conversation of actually working on it.
Ali Emami
13:31:08
Yeah, I like it, I like it, because it's looking at… there's, like, different biases you're testing, essentially, and we can even call them biases in the paper, but there's, like, self-preference bias.
Liam Neild
13:31:17
Yes.
Ali Emami
13:31:18
And that's actually what this is. It prefers itself, and so because of it, yeah. Then there's, um…
Liam Neild
13:31:20
Does it defend itself?
Ali Emami
13:31:25
the bias of, I think, just… that's actually called sycophancy. It's like sycophancy in terms of if it's you that needs it versus, like, you're the recipient of it, and you're gonna test sycophancy that way. And then, um…
Then there's… I guess there's another… I mean, the whole revision thing, I don't know if necessarily that's a bias, but that's the problem that you're trying to address, is that it's, like, not useful, but I think it's all there. And what I also like is that…
this phase thing doesn't look like everything correlates nicely, but it will when we look at the results later. Like.
Liam Neild
13:31:57
Yeah.
Ali Emami
13:31:58
Yeah.
Liam Neild
13:31:59
The phases are really, like, the main experiment is just 0, 1, and 2. The rest of them are subjects.
Ali Emami
13:32:02
Yeah, these are probably for you in terms of temporally when you're going to conduct these. Like, you're going to do this, this. Yeah, and then ultimately, we'll look at the results, and we'll paint a picture that might be based on, like.
Liam Neild
13:32:06
Yeah, exactly.
Ali Emami
13:32:13
Three or four questions.
Liam Neild
13:32:14
Exactly.
Ali Emami
13:32:15
Yeah.
Liam Neild
13:32:16
um…
Ali Emami
13:32:17
But it looks like you're a go. I think this is all fantastic. Usually in studies you do something called ablation where you remove components, but I think yours has enough.
Different.
studies that you may not need to do that, and I think it's because then you make too many calls, and then it gets really expensive. But, by the way, I'll give you an API key, because I think my next question was… or maybe you have other things that you were going to talk about. Maybe, was it the tasks? Yeah, before we get to…
Okay.


























































Key Outcomes
Liam presented a refined experimental design to measure wasted effort and quality trajectory when AI models revise their own outputs. The study will use six models (GPT-4o, Claude, Gemini, Llama, Mistral, Qwen) across 40 real tasks spanning creative to code domains, with a six-level grading scale replacing binary evaluation. Ali approved the core methodology and all sub-experiments, confirming the study is ready to proceed. [Citation][Citation][Citation]
Decisions Made
- Probe wording: Use "Would you like to keep this as your final version, or would you like to revise it?" as the neutral prompt for all main experiments [Citation][Citation]
- Quality framing: Change "quality loss" to "quality trajectory" or "diminishing gains in quality" in the two-sentence pitch, since direction is unknown pre-study [Citation][Citation]
- Six-level rubric: Finalized scale where 1-3 indicate revision needed, 4-5 are acceptable without revision (with quality differences), and 6 signals overcorrection (unrequested complexity, too long, drifted from ask) [Citation][Citation]
- Model selection: Confirmed three commercial (GPT-4o, Claude, Gemini) and three open-source models (Llama, Mistral, Qwen), avoiding duplicate vendors [Citation]
- Judge sees task: Evaluator must have access to original task to assess "unrequested complexity" in the rubric [Citation][Citation]
- Reversibility design: Use randomized A/B testing with fresh judge instance comparing turn 1 vs turn 5 outputs, run ~20 times to calculate win rates [Citation]
Experimental Phases
Phase 0: Judge Calibration
- Run smaller sample with all models as judges plus human evaluation [Citation]
- Select judge with highest correlation to human ratings [Citation]
- Use six-level scale for all evaluations [Citation][Citation]
Phase 1: Core Working Conversations
- 40 tasks across creative to code domains [Citation]
- Apply neutral probe after each model output [Citation]
- Track revision patterns across all six models [Citation][Citation]
Phase 2: Fresh Judge Evaluation
- Judge evaluates all outputs from Phase 1 using six-level rubric [Citation]
Phase 3: One-Shot Ceiling (Model Confidence)
- Repeatedly ask "can this be revised?" with zero additional input until model stops revising [Citation][Citation][Citation]
- Measures model confidence thresholds across task types (e.g., more confident in code vs creative) [Citation]
- Disconnected from quality measurement; focuses on meta-behavior [Citation][Citation]
Phase 4: Reversibility Study
- Fresh judge instance performs randomized A/B comparison of turn 1 vs turn 5 outputs [Citation][Citation]
- Run 20 times with shuffled order to calculate true win rates [Citation]
- Tests if later revisions are significantly worse than initial outputs [Citation]
Phase 5: Directed Feedback
- Judge provides targeted feedback instead of generic "would you like to revise?" probe [Citation][Citation]
- Tests whether objective, bird's-eye-view feedback produces better revisions than self-initiated changes [Citation][Citation][Citation]
- Hypothesis: May work better because evaluator is unbiased by sycophancy or personalization attempts [Citation][Citation]
Phase 6: Self-Reflection
- At turn 6, ask model within same conversation which version (1 or 5) it prefers [Citation]
- Tests self-preference bias vs objective reversibility results [Citation][Citation]
Phase 7: Agent vs Patient Framing (Sycophancy Test)
- Compare outcomes when model believes it's the sender vs recipient of work [Citation][Citation]
- Example: "This is an email draft I wrote" vs "This is an email I received" [Citation]
- Tests if contextual framing affects revision behavior [Citation]
Open Design Questions
- Probe authenticity: Liam noted he wouldn't naturally use "would you like to keep this as your final version" in real conversations; typically asks "what do you think about it?" but that's too non-neutral for the study [Citation]
- Token economics influence: Liam's willingness to "waste tokens" may be a product of his usage patterns rather than the probe itself [Citation]
- Directed feedback paradox: Unclear whether evaluator can give better advice than original instance since both see same information; may succeed due to reduced sycophancy focus [Citation][Citation]
Research Context
- Emerging validation: People on Twitter/LinkedIn reporting that telling Claude not to save lessons or personalize actually improves performance, aligning with "less is more" theme [Citation]
- RLHF implications: Models may be trained to expect secondary revision questions, potentially not giving best output initially [Citation]
- Multi-agent relevance: Study explores whether evaluator-in-the-loop setup could override model's self-revision tendencies [Citation]
Action Items
- Liam: Revise rubric language from "unrequested complexity" to "overly complex" if judge won't have task context, or keep as-is since judge needs task to evaluate [Citation][Citation]
- Liam: Clarify Phase 3 documentation to emphasize it's repeated probing with zero input until model stops, not one-shot performance [Citation]
- Ali: Provide API key for experiment execution [Citation]
Next Steps
- Review task list details (documented but not discussed in this meeting) [Citation][Citation]
- Begin implementation of calibration phase [Citation]




Quick recap
Ali and Liam discussed the proper way to safely handle API keys, particularly when using them with AI tools like Claude. They shared experiences about AI models potentially sharing conversation data with third parties, including examples of how Claude detected and restricted access when sensitive information like Zoom meeting keys was shared. Ali explained the recommended practice of using a .env file to securely store API keys and make tool calls, which helps prevent the information from being shared with the AI model itself. The conversation concluded with Ali generating and sharing a new API key for Liam to use for testing purposes.
Next steps
Liam
- Conduct a smoke test with the provided API key and let Ali know the results.
Summary
API Key Security Best Practices
Ali and Liam discussed the safe handling of API keys, particularly when using them with AI tools like Claude. Ali explained the importance of using a .env file to securely store and manage API keys, as sharing them directly in chat could lead to security issues and potential billing problems. They also talked about the potential for AI models to share user data with third parties. Ali shared his API key with Liam and advised setting a limit on usage to prevent excessive charges. Liam mentioned a previous incident where he accidentally shared his Zoom host key, which prompted a discussion about the importance of prioritizing sensitive information.

